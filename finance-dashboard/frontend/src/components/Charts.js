import React from "react";
import { Pie } from "react-chartjs-2";

const Charts = ({ data }) => {
  const income = data.filter((item) => item.type === "income").reduce((sum, item) => sum + item.amount, 0);
  const expense = data.filter((item) => item.type === "expense").reduce((sum, item) => sum + item.amount, 0);

  const chartData = {
    labels: ["Income", "Expense"],
    datasets: [
      {
        data: [income, expense],
        backgroundColor: ["#36A2EB", "#FF6384"],
      },
    ],
  };

  return <Pie data={chartData} />;
};

export default Charts;
