import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
	return (
		<nav className="bg-gray-800 p-4">
		  <div className="container mx-auto">
		    <div className="flex justify-between">
		      <Link to="/" className="text-white font-bold">
		        OreonElectro
		      </Link>
		      <div className="flex space-x-4">
		        <Link to="/register" className="text-white">
		          Register
		        </Link>
		        <Link to="/login" className="text-white">
		          Login
		        </Link>
		      </div>
		    </div>
		  </div>
		</nav>
	);
};

export default Navbar;
