import React from 'react';

const Home: React.FC = () => {
  return (
    <div className="bg-gradient-to-r from-green-400 to-blue-500 min-h-screen flex items-center justify-center">
      <div className="text-center p-10 bg-white bg-opacity-75 rounded-lg shadow-lg">
        <h1 className="text-5xl font-bold text-gray-800 mb-4">Welcome to OreonElectro</h1>
        <p className="text-xl text-gray-600">Your One Stop Shop for all Electronics</p>
        <button className="mt-6 px-4 py-2 bg-yellow-400 text-white font-bold rounded-lg shadow-md hover:bg-yellow-500 transition duration-300">
          Shop Now
        </button>
      </div>
    </div>
  );
};

export default Home;

