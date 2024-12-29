# Punyaja_submission (due to some issues with my Github account submitted it in my brothers account)


```markdown
# Finance Dashboard API

A simple API for managing user accounts and finance data, built with FastAPI. The application supports role-based access control, distinguishing between admin and regular user accounts.

## Features

- **User Authentication:**
  - Sign up and login with hashed passwords.
  - Role-based access control (`admin` and `user`).
- **Finance Data Management (Admin Only):**
  - Create, read, and delete finance records.
- **Default Admin User:**
  - A default admin account is created during setup.

## Getting Started

### Prerequisites

- Python 3.9 or later
- A virtual environment tool (optional but recommended)
- SQLite (default database)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AniBirage/Punyaja_submission.git
   cd finance-dashboard
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations:**

   The database is automatically initialized when the app starts. Ensure `models.py` defines the database structure correctly.

5. **Run the Application:**

   ```bash
   uvicorn backend.app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

### Default Admin User

- **Username:** `admin`
- **Password:** `defaultadminpassword`

You can change the default password by modifying the `create_default_admin` function in `main.py`.

## API Endpoints

### Authentication

| Method | Endpoint         | Description               |
|--------|-------------------|---------------------------|
| POST   | `/signup`         | Register a new user.      |
| POST   | `/login`          | Login and validate user.  |

### Finance Data (Admin Only)

| Method | Endpoint          | Description                      |
|--------|--------------------|----------------------------------|
| POST   | `/finance/`        | Create a new finance record.     |
| GET    | `/finance/`        | Retrieve all finance records.    |
| DELETE | `/finance/{id}`    | Delete a specific finance record.|



## Technologies Used

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** SQLite (default)
- **ORM:** SQLAlchemy
- **Authentication:** Password hashing with bcrypt

## Future Enhancements

- Add JWT-based authentication.
- Enhance database operations with advanced queries.
- Integrate unit and integration testing.
- Add frontend for user interaction.
