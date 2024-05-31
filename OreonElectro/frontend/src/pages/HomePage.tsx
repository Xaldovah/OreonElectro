import React from 'react';
import Navbar from '../components/Navbar';
import Hero from '../components/Hero';
import ProductList from '../components/ProductList';
import Sidebar from '../components/Sidebar';
import Footer from '../components/Footer';

const HomePage: React.FC = () => {
  return (
    <>
      <Navbar />
      <Hero />
      <div className="container-fluid">
        <div className="row">
          <div className="col-md-3">
            <Sidebar />
          </div>
          <div className="col-md-9">
            <ProductList />
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default HomePage;
