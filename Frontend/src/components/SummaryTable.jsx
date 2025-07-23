import React from "react";

export default function SummaryTable({ summary }) {
  return (
    <table className="w-full border mt-4">
      <thead>
        <tr className="bg-gray-100">
          <th className="p-2 border">Member</th>
          <th className="p-2 border">Balance</th>
        </tr>
      </thead>
      <tbody>
        {summary.map((item) => (
          <tr key={item.user}>
            <td className="p-2 border">{item.user}</td>
            <td className="p-2 border">{item.balance}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}