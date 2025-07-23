import React from "react";

export default function GroupCard({ group, onSelect }) {
  return (
    <div onClick={() => onSelect(group)} className="border p-4 rounded shadow hover:bg-gray-100 cursor-pointer">
      <h2 className="text-lg font-semibold">{group.name}</h2>
      <p>{group.members.length} members</p>
    </div>
  );
}