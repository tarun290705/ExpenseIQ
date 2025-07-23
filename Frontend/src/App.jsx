import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DashboardPage from './pages/DasboardPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import GroupPage from './pages/GroupPage';
import SettingsPage from './pages/SettingsPage';
import Navbar from './components/Navbar';
import {Provider} from 'react-redux'
import store from './redux/store';

function App() {
  return (
    <Provider store={store}>
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/group/:groupId" element={<GroupPage />} />
        <Route path="/settings" element={<SettingsPage />} />
      </Routes>
    </Router>
    </Provider>
  );
}

export default App;
