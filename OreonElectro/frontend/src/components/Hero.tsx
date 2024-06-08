import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'react-bootstrap';

const Hero: React.FC = () => {
  return (
      <Container className="text-center">
        <img src="/images/big_sale.jpg" alt="Wide Range of Mobile Phones" className="img-fluid mb-4" style={{ height: '200px' }} />
        <h1 className="display-4 font-weight-bold mb-4" style={{ fontSize: '2rem' }}>Wide Range of Mobile Phones!</h1>
        <button className="btn btn-warning btn-lg mb-5">Shop Now</button>
      </Container>
  );
}

export default Hero;
