import React from 'react';
import { Card } from 'react-bootstrap';

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
    <Card className="h-100">
      <a href={`/products/${product.id}`} className="stretched-link">
        <Card.Img variant="top" src={`http://localhost:8000${product.image}`} alt={product.name} />
      </a>
      <Card.Body className="d-flex flex-column">
        <Card.Title>{product.name}</Card.Title>
        <Card.Text>
          {product.discountPrice ? (
            <div>
              <span className="text-muted text-decoration-line-through">${Number(product.price).toFixed(2)}</span>
              <span className="text-danger ml-2">${Number(product.discountPrice).toFixed(2)}</span>
            </div>
          ) : (
            <span>${Number(product.price).toFixed(2)}</span>
          )}
        </Card.Text>
        <button className="btn btn-primary mt-auto">Add to Cart</button>
      </Card.Body>
    </Card>
  );
};

export default ProductCard;
