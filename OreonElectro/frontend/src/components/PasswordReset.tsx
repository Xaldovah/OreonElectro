import React, { useState, ChangeEvent, FormEvent } from 'react';
import axios from 'axios';

interface FormData {
  email: string;
}

const PasswordReset: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    email: '',
  });

  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/customer/password-reset/', formData);
      console.log(response.data);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div>
      {/* Display error message if an error occurred */}
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit}>
        <input type="email" name="email" onChange={handleChange} placeholder="Email" required />
        <button type="submit">Reset Password</button>
      </form>
    </div>
  );
};

export default PasswordReset;
