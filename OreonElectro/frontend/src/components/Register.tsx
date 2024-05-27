import React, { useState, ChangeEvent, FormEvent } from 'react';
import axiosInstance from '../axiosConfig';

interface FormData {
  username: string;
  email: string;
  password: string;
  shipping_address: string;
  billing_address: string;
  phone_number: string;
}

const Register: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    username: '',
    email: '',
    password: '',
    shipping_address: '',
    billing_address: '',
    phone_number: '',
  });

  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('/api/customer/register/', formData);
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('userId', response.data.user_id);
    } catch (error: any) {
      setError(error.message);
    }
  };

  return (
    <div>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input type="text" name="username" onChange={handleChange} placeholder="Username" required />
        <input type="email" name="email" onChange={handleChange} placeholder="Email" required />
        <input type="password" name="password" onChange={handleChange} placeholder="Password" required />
        <textarea name="shipping_address" onChange={handleChange} placeholder="Shipping Address" required />
        <textarea name="billing_address" onChange={handleChange} placeholder="Billing Address" />
        <input type="tel" name="phone_number" onChange={handleChange} placeholder="Phone Number" required />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;
