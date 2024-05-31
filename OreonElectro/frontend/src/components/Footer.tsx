import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-dark text-white py-4">
      <div className="container text-center">
        <p>&copy; 2024 OreonElectro. All rights reserved.</p>
        <div className="mt-2">
          <a href="/" className="text-white mx-2">Privacy Policy</a>
          <a href="/" className="text-white mx-2">Terms of Service</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
