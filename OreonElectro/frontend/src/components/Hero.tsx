import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'react-bootstrap';

const Hero: React.FC = () => {
  return (
    <div className="bg-light py-5">
      <Container className="text-center">
        <img src="/images/big_sale.jpg" alt="Wide Range of Mobile Phones" className="img-fluid mb-4" />
        <h1 className="display-4 font-weight-bold mb-4">Wide Range of Mobile Phones!</h1>
        <button className="btn btn-warning bt-lg mb-5">Shop Now</button>
        <Row className="mt-4">
          <Col md={4}>
            <div className="border p-3">
              <img src="/images/headset.jpg" alt="headset" className="img-fluid mb-2" />
            </div>
          </Col>
          <Col md={4}>
            <div className="border p-3">
              <img src="/images/bluetooth.jpg" alt="bluetooth" className="img-fluid mb-2" />
            </div>
          </Col>
          <Col md={4}>
            <div className="border p-3">
              <img src="/images/smartphones.png" alt="smartphones" className="img-fluid mb-2" />
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Hero;
