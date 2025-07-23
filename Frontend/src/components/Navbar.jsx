import React from "react";
import { use } from "react";
// import { useAuth } from "../context/AuthContext";
import { useSelector } from "react-redux";

export default function Navbar() {
  // const { user, logout } = useAuth();
  const {user} = useSelector((state)=>state.user);
  return (
    <nav className="bg-blue-600 text-white p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">ExpenseIQ</h1>
      <div>
        {user && <span className="mr-4">Hello, {user.username}</span>}
        {/* {user && (
          <button onClick={logout} className="bg-red-500 px-3 py-1 rounded">Logout</button>
        )} */}
      </div>
    </nav>
  );
}