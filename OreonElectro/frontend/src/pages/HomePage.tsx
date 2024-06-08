import React from 'react';
import Navbar from '../components/Navbar';
import Hero from '../components/Hero';
import CustomerSupport from '../components/CustomerSupport';
import ProductList from '../components/ProductList';
import Sidebar from '../components/Sidebar';
import Footer from '../components/Footer';
import '../styles/custom.css';

const HomePage: React.FC = () => {
  return (
    <>
      <Navbar />
      <div className="container-fluid">
        <div className="row" style={{ minHeight: '70vh' }}>
          <div className="col-md-3 col-sm-12 p-3">
            <Sidebar />
          </div>
          <div className="col-md-9 col-sm-12 p-3">
            <Hero />
          </div>
        </div>
        <CustomerSupport />
        <div className="row">
          <div className="col-md-12">
            <ProductList />
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default HomePage;
