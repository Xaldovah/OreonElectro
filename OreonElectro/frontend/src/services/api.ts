import axiosInstance from '../axiosConfig';

const API_URL = '/api/products/';


export const fetchProducts = async () => {
  try {
    const response = await axiosInstance.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching products, error');
    throw error;
  }
};
