import React, { useState, ChangeEvent, FormEvent } from 'react';
import axios from 'axios';

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

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/register/', formData);
      console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    // Will add registration form here
  );
};

export default Register;
