import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import { FaHeadset, FaShippingFast, FaCreditCard } from 'react-icons/fa';

const CustomerSupport: React.FC = () => {
  return (
    <Container className="text-center my-5">
      <Row>
        <Col md={4}>
          <FaHeadset size={50} className="mb-3" />
          <h5>24/7 Online Support</h5>
          <p>We are here to help you anytime.</p>
        </Col>
        <Col md={4}>
          <FaShippingFast size={50} className="mb-3" />
          <h5>Fast Delivery</h5>
          <p>Get your products delivered quickly.</p>
        </Col>
        <Col md={4}>
          <FaCreditCard size={50} className="mb-3" />
          <h5>Fast Checkout</h5>
          <p>Seamless and secure checkout process.</p>
        </Col>
      </Row>
    </Container>
  );
};

export default CustomerSupport;
