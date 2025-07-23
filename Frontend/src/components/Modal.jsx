import React from "react";

export default function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white p-6 rounded shadow-md">
        <button className="absolute top-4 right-4 text-lg" onClick={onClose}>×</button>
        {children}
      </div>
    </div>
  );
}