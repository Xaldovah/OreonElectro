import React, { useState, useEffect, ChangeEvent, FormEvent } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

interface FormData {
  username: string;
  email: string;
  shipping_address: string;
  billing_address: string;
  phone_number: string;
  payment_method: string;
}

const CustomerDetail: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    username: '',
    email: '',
    shipping_address: '',
    billing_address: '',
    phone_number: '',
    payment_method: '',
  });

  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchDetails = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('/api/customer-detail/', {
          headers: { 'Authorization': `Token ${token}` }
        });
        setFormData(response.data);
      } catch (error) {
        setError(error.message);
      }
    };

    fetchDetails();
  }, []);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      const response = await axios.put('/api/customer/customer-detail/', formData, {
        headers: { 'Authorization': `Token ${token}` }
      });
      console.log(response.data);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input type="text" name="username" value={formData.username} onChange={handleChange} placeholder="Username" required />
        <input type="email" name="email" value={formData.email} onChange={handleChange} placeholder="Email" required />
        <textarea name="shipping_address" value={formData.shipping_address} onChange={handleChange} placeholder="Shipping Address" required />
        <textarea name="billing_address" value={formData.billing_address} onChange={handleChange} placeholder="Billing Address" required />
        <input type="tel" name="phone_number" value={formData.phone_number} onChange={handleChange} placeholder="Phone Number" required />
        <select name="payment_method" value={formData.payment_method} onChange={handleChange} required>
          <option value="">Select Payment Method</option>
          <option value="bank">Bank Transfer</option>
          <option value="mpesa">M-Pesa</option>
          <option value="paypal">PayPal</option>
          <option value="stripe">Stripe</option>
        </select>
        <button type="submit">Update Details</button>
      </form>
    </div>
  );
};

export default CustomerDetail;
