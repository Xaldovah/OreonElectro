import React, { useState, ChangeEvent, FormEvent } from 'react';
import axiosInstance from '../axiosConfig';
import { useNavigate } from 'react-router-dom';

interface FormData {
  username: string;
  password: string;
}

const Login: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    username: '',
    password: '',
  });

  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('/api/customer/login/', formData);
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('userId', response.data.user_id);
      navigate('/');
    } catch (error: any) {
      setError(error.message);
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center vh-100 bg-light">
      <div className="card shadow-sm p-4" style={{ maxWidth: '400px', width: '100%' }}>
        <h2 className="card-title text-center">Login</h2>
        {error && <p className="text-danger text-center">{error}</p>}
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="username" className="form-label">Username</label>
            <input
              type="text"
              name="username"
              id="username"
              onChange={handleChange}
              placeholder="Username"
              required
              className="form-control"
            />
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label">Password</label>
            <input
              type="password"
              name="password"
              id="password"
              onChange={handleChange}
              placeholder="Password"
              required
              className="form-control"
            />
          </div>
          <div className="d-grid">
            <button
              type="submit"
              className="btn btn-primary"
            >
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
