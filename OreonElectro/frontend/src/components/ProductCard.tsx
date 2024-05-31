import React from 'react';

interface Product {
  id: number;
  name: string;
  price: string;
  image: string;
  discountPrice?: string;
  isNew?: boolean;
}

interface ProductCardProps {
  product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  return (
    <div className="card">
      <img src={product.image} alt={product.name} className="card-img-top" />
      <div className="card-body">
        <h5 className="card-title">{product.name}</h5>
        <div className="card-text">
          {product.discountPrice ? (
            <div>
              <span className="text-muted text-decoration-line-through">${product.price}</span>
              <span className="text-danger ml-2">${product.discountPrice}</span>
            </div>
          ) : (
            <span>${product.price}</span>
          )}
        </div>
        <button className="btn btn-primary mt-2">Add to Cart</button>
      </div>
    </div> 
  );
};

export default ProductCard;
