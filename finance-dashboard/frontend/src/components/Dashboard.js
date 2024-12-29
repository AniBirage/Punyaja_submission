import React, { useState, useEffect } from "react";
import { getFinanceData } from "../api";
import Charts from "./Charts";

const Dashboard = ({ token }) => {
  const [financeData, setFinanceData] = useState([]);

  const fetchData = async () => {
    const data = await getFinanceData(token);
    setFinanceData(data);
  };

  useEffect(() => {
    fetchData();
  }, [token]);

  return (
    <div>
      <h2>Dashboard</h2>
      <Charts data={financeData} />
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Amount</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          {financeData.map((item) => (
            <tr key={item.id}>
              <td>{item.title}</td>
              <td>{item.amount}</td>
              <td>{item.type}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dashboard;
