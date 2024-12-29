import React, { useState } from "react";
import { addFinanceData } from "../api";

const AddFinanceForm = ({ token, refreshData }) => {
  const [formData, setFormData] = useState({
    title: "",
    amount: "",
    type: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addFinanceData(formData, token);
    alert("Finance data added!");
    refreshData();
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Finance Data</h2>
      <input
        type="text"
        placeholder="Title"
        value={formData.title}
        onChange={(e) => setFormData({ ...formData, title: e.target.value })}
        required
      />
      <input
        type="number"
        placeholder="Amount"
        value={formData.amount}
        onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
        required
      />
      <select
        value={formData.type}
        onChange={(e) => setFormData({ ...formData, type: e.target.value })}
        required
      >
        <option value="" disabled>
          Select Type
        </option>
        <option value="income">Income</option>
        <option value="expense">Expense</option>
      </select>
      <button type="submit">Add</button>
    </form>
  );
};

export default AddFinanceForm;
