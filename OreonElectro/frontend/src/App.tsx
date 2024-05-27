import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Register from './components/Register';
import Login from './components/Login';
import Logout from './components/Logout';
import PasswordReset from './components/PasswordReset';
import CustomerDetail from './components/CustomerDetail';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container mx-auto mt-4">
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/password-reset" element={<PasswordReset />} />
          <Route path="/profile" element={<CustomerDetail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

