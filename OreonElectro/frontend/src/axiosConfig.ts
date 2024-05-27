import axios from 'axios';

const baseURL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

  const axiosInstance = axios.create({
  baseURL: baseURL,
});

export default axiosInstance;
