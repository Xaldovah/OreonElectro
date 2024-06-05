import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axiosInstance from 'axios';

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  description: string;
  discountPrice?: number;
  isNew?: boolean;
}

const ProductDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [product, setProduct] = useState<Product | null>(null);

  useEffect(() => {
    async function fetchProduct() {
      try {
        const response = await axiosInstance.get(`http://localhost:8000/api/products/${id}`);
        setProduct(response.data);
      } catch (error) {
        console.error("Error fetching the product:", error);
      }
    }
    fetchProduct();
  }, [id]);

  if (!product) {
    return <div>Loading...</div>
  }

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-md-6">
          <img src={`http://localhost:8000${product.image}`} alt={product.name} className="img-fluid" />
        </div>
        <div className="col-md-6">
          <h1>{product.name}</h1>
          {product.discountPrice ? (
            <div>
              <span className="text-muted text-decoration-line-through">${Number(product.price).toFixed(2)}</span>
              <span className="text-danger ml-2">${Number(product.discountPrice).toFixed(2)}</span>
            </div>
          ) : (
            <span>${Number(product.price).toFixed(2)}</span>
          )}
          <p>{product.description}</p>
          <button className="btn btn-primary mt-auto">Add to Cart</button>
        </div>
      </div>
    </div>
  );
};

export default ProductDetail;
