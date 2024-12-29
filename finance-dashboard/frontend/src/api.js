const BASE_URL = "http://127.0.0.1:8000";

export const signup = async (userData) => {
  const response = await fetch(`${BASE_URL}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
  });
  return response.json();
};

export const login = async (userData) => {
  const response = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
  });
  return response.json();
};

export const addFinanceData = async (financeData, token) => {
  const response = await fetch(`${BASE_URL}/finance/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(financeData),
  });
  return response.json();
};

export const getFinanceData = async (token) => {
  const response = await fetch(`${BASE_URL}/finance/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.json();
};
