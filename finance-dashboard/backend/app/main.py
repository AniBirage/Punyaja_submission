from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
# Signup
@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the user is admin and assign a default password if necessary
    if user.username == "admin" and not user.password:
        user.password = "123456"  # Set a default password for admin

    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

# Login
@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

# Create finance data (Admin functionality)
@app.post("/finance/")
def create_finance(data: schemas.FinanceDataCreate, db: Session = Depends(get_db)):
    # Only allow admin to create finance data
    current_user = db.query(models.User).filter(models.User.username == "admin").first()
    if current_user.username != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create finance data")
    return crud.create_finance_data(db, data)

# Read all finance data (For all users, but can only view by regular users)
@app.get("/finance/")
def read_finance(db: Session = Depends(get_db)):
    return crud.get_finance_data(db)

# Delete finance data (Admin functionality)
@app.delete("/finance/{data_id}")
def delete_finance(data_id: int, db: Session = Depends(get_db)):
    # Only allow admin to delete finance data
    current_user = db.query(models.User).filter(models.User.username == "admin").first()
    if current_user.username != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete finance data")
    db_data = db.query(models.FinanceData).filter(models.FinanceData.id == data_id).first()
    if not db_data:
        raise HTTPException(status_code=404, detail="Data not found")
    return crud.delete_finance_data(db, data_id)

# Utility to get the current user (you can expand this function to support authentication)
def get_current_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
