import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col, Spinner, Alert } from 'react-bootstrap';
import { getProducts } from '../api';
import ProductCard from './ProductCard';
import '../styles/custom.css';

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  description: string;
}

const ProductList: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await getProducts();
        setProducts(response.data);
        setLoading(false);
      } catch (error) {
        setError('Error fetching products');
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (loading) return <Spinner animation="border" role="status"><span className="sr-only">Loading...</span></Spinner>;

  if (error) return <Alert variant="danger">{error}</Alert>;

  return (
    <Container>
      <Row>
        {products.map(product => (
          <Col md={4} key={product.id} className="mb-4">
            <ProductCard product={product} />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default ProductList;
