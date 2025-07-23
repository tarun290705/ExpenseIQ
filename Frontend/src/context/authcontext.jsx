// src/context/AuthContext.js
import React, { createContext, useContext, useEffect, useState } from "react";
import { loginUser, logoutUser } from "../api/auth";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("token"));

  useEffect(() => {
    if (token && !user) {
      // Optionally fetch user info with token
      setUser({ email: "example@example.com" }); // Placeholder
    }
  }, [token]);

  const login = async (email, password) => {
    try {
      const data = await loginUser(email, password);
      setToken(data.token);
      localStorage.setItem("token", data.token);
      setUser({ email });
      return true;
    } catch (err) {
      console.error("Login failed", err);
      return false;
    }
  };

  const logout = () => {
    logoutUser();
    setUser(null);
    setToken(null);
    localStorage.removeItem("token");
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
