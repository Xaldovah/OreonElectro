import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import '../styles/custom.css';

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  discountPrice?: number;
  isNew?: boolean;
}

interface ProductCardProps {
  product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  return (
    <div className="product-card">
      <Link to={`/products/${product.id}`} className="text-decoration-none">
        <div className="product-image-wrapper">
          <img src={`http://localhost:8000${product.image}`} alt={product.name} className="img-fluid" />
        </div>
        <div className="product-details p-2">
          <h5 className="product-name">{product.name}</h5>
          <p className="product-price">
            {product.discountPrice ? (
              <div>
                <span className="text-muted text-decoration-line-through">${Number(product.price).toFixed(2)}</span>
                <span className="text-danger ml-2">${Number(product.discountPrice).toFixed(2)}</span>
              </div>
            ) : (
              <span>${Number(product.price).toFixed(2)}</span>
            )}
          </p>
          <Button variant="primary" className="add-to-cart-btn">Add to Cart</Button>
        </div>
      </Link>
    </div>
  );
};

export default ProductCard;
