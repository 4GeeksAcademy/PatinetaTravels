import React from "react";
import { Link } from "react-router-dom";
import Logo from '../../img/PatinetaTravelLogo.png';

export const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link className="navbar-brand" to="/">
          <img src={Logo} alt="Patineta Travel" style={{ height: "50px" }} />
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <Link to="/" className="nav-link">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/mainview" className="nav-link">
                Cities
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/demo" className="nav-link">
                Demo
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};
