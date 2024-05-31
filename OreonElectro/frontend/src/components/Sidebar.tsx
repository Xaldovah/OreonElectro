import React from 'react';

const Sidebar: React.FC = () => {
  return (
    <aside className="col-md-3 p-4 border-right">
      <div className="mb-4">
        <h5 className="font-weight-bold mb-3">Customer Review</h5>
        <ul className="list-unstyled">
          <li>⭐️⭐️⭐️⭐️⭐️ 5.0</li>
          <li>⭐️⭐️⭐️⭐️ 4.0</li>
          <li>⭐️⭐️⭐️ 3.5</li>
        </ul>
      </div>
      <div className="mb-4">
        <h5 className="font-weight-bold mb-3">Price</h5>
        <ul className="list-unstyled">
          <li>Under 10000</li>
          <li>10000 - 20000</li>
          <li>30000 - 40000</li>
          <li>40000 - 50000</li>
          <li>Over 50000</li>
        </ul>
      </div>
      <div className="mb-4">
        <h5 className="font-weight-bold mb-3">Discount</h5>
        <ul className="list-unstyled">
          <li>5% or More</li>
          <li>10% or More</li>
          <li>20% or More</li>
          <li>30% or More</li>
          <li>50% or More</li>
        </ul>
      </div>
      <div className="mb-4">
        <h5 className="font-weight-bold mb-3">Electronics</h5>
        <ul className="list-unstyled">
          <li>Accessories</li>
          <li>Cameras</li>
          <li>Wearable Technology</li>
        </ul>
      </div>
    </aside>
  );
};

export default Sidebar;
