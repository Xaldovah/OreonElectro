import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '@fortawesome/fontawesome-free/css/all.min.css';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-cyan shadow-sm">
      <div className="container-fluid">
        <Link className="navbar-brand fw-bold text-primary" to="/">OreonElectro</Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavDropdown">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                All Categories
              </a>
              <ul className="dropdown-menu">
                <li><Link className="dropdown-item" to="/category/smartphones">Smartphones</Link></li>
                <li><Link className="dropdown-item" to="/category/computers">Computers</Link></li>
                <li><Link className="dropdown-item" to="/category/headsets">Headsets</Link></li>
                <li><Link className="dropdown-item" to="/category/accessories">Accessories</Link></li>
              </ul>
            </li>
          </ul>
          <form className="d-flex mx-auto" role="search">
            <input className="form-control me-2" type="search" placeholder="Search for products" aria-label="Search" />
            <button className="btn btn-outline-primary" type="submit">Search</button>
          </form>
          <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link" to="/cart">
                <i className="fas fa-shopping-cart fa-lg text-primary"></i>
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/favorites">
                <i className="fas fa-heart fa-lg text-primary"></i>
              </Link>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#" id="userDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <i className="fas fa-user fa-lg text-primary"></i>
              </a>
              <ul className="dropdown-menu dropdown-menu-end" aria-labelledby="userDropdown">
                <li><Link className="dropdown-item" to="/register">Register</Link></li>
                <li><Link className="dropdown-item" to="/login">Login</Link></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
