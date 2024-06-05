import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Spinner, Alert, Container, Row, Col, Button } from 'react-bootstrap';
import { getProduct } from '../api';

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
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await getProduct(Number(id));
        setProduct(response.data);
        setLoading(false);
      } catch (error) {
        setError('Error fetching the product');
        setLoading(false);
      }
    };

    if (id) fetchProduct();
  }, [id]);

  if (loading) return <Spinner animation="border" role="status"><span className="sr-only">Loading...</span></Spinner>;

  if (error) return <Alert variant="danger">{error}</Alert>;

  if (!product) return null;

  return (
    <Container className="mt-5">
      <Row>
        <Col md={6}>
          <img src={`http://localhost:8000${product.image}`} alt={product.name} className="img-fluid" />
        </Col>
        <Col md={6}>
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
          <Button className="mt-auto" variant="primary">Add to Cart</Button>
        </Col>
      </Row>
    </Container>
  );
};

export default ProductDetail;
