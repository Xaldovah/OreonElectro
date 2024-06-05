import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const axiosInstance = axios.create({
	baseURL: API_URL,
	headers: {
		'Content-Type': 'application/json',
	},
});

export const getProducts = () => axiosInstance.get('products/');
export const getProduct = (id: number) => axiosInstance.get(`products/${id}/`);
