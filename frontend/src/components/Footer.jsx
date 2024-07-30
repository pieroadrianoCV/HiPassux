import React from 'react';

const Footer = () => {
  return (
    <footer>
      <div className="container">
        <div className="links">
          <div>
            <h3>About Us</h3>
            <ul>
              <li>Our Story</li>
              <li>Blog</li>
              <li>Careers</li>
              <li>Press</li>
            </ul>
          </div>
          <div>
            <h3>Support</h3>
            <ul>
              <li>Help Center</li>
              <li>Community Guidelines</li>
              <li>Safety Tips</li>
              <li>Contact Us</li>
            </ul>
          </div>
          <div>
            <h3>Legal</h3>
            <ul>
              <li>Privacy Policy</li>
              <li>Terms of Service</li>
              <li>Cookie Policy</li>
              <li>Accessibility</li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
