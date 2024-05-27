import React, { useState } from 'react';
import axios from 'axios';

const Logout: React.FC = () => {
  const [error, setError] = useState<string | null>(null);

  const handleLogout = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post('/api/customer/logout/', {}, {
        headers: { 'Authorization': `Token ${token}` }
      });

      localStorage.removeItem('token');
      localStorage.removeItem('userId');
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      {error && <p>{error}</p>}
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Logout;
