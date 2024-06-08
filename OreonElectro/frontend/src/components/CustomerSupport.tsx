import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'react-bootstrap';
import { FaHeadset, FaShippingFast, FaCreditCard } from 'react-icons/fa';

const CustomerSupport: React.FC = () => {
  return (
    <Container className="text-center my-5">
      <Row>
        <Col md={4}>
          <FaHeadset size={20} className="mb-3" />
          <h6><b>24/7 Online Support</b></h6>
          <p>We are here to help you anytime.</p>
        </Col>
        <Col md={4}>
          <FaShippingFast size={20} className="mb-3" />
          <h6><b>Fast Delivery</b></h6>
          <p>Get your products delivered quickly.</p>
        </Col>
        <Col md={4}>
          <FaCreditCard size={20} className="mb-3" />
          <h6><b>Fast Checkout</b></h6>
          <p>Seamless and secure checkout process.</p>
        </Col>
      </Row>
    </Container>
  );
};

export default CustomerSupport;
