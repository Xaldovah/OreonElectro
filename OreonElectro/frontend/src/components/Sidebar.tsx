import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { FaMobileAlt, FaDesktop, FaHeadphones, FaFilm, FaCamera, FaCube, FaTv, FaLightbulb } from 'react-icons/fa';

const Sidebar: React.FC = () => {
  return (
    <div className="d-flex flex-column p-3 bg-light" style={{ height: '100vh', width: '250px' }}>
      <ul className="nav nav-pills flex-column mb-auto">
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaMobileAlt className="me-2" />
            Smartphones
          </a>
        </li>
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaDesktop className="me-2" />
            Computers
          </a>
        </li>
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaHeadphones className="me-2" />
            Headsets
          </a>
        </li>
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaFilm className="me-2" />
            Entertainment
          </a>
        </li>
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaCamera className="me-2" />
            Camera
          </a>
        </li>
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaCube className="me-2" />
            Accessories
          </a>
        </li>
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaTv className="me-2" />
            TV
          </a>
        </li>
        <li className="nav-item mb-3">
          <a href="#" className="nav-link text-dark">
            <FaLightbulb className="me-2" />
            Lighting
          </a>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
