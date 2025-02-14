import React from "react";
import { useNavigate } from "react-router-dom";
import "../../styles/home.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Button, Carousel } from "react-bootstrap";

// Importación de imágenes
import PatinetaTravelImag1 from "../../img/1.jpg";
import PatinetaTravelImag2 from "../../img/2.jpg";
import PatinetaTravelImag3 from "../../img/3.jpg";
import PatinetaTravelImag4 from "../../img/4.jpg";
import PatinetaTravelImag5 from "../../img/5.jpg";

// Importación de iconos
import LoginLogo from "../../img/Login.jpg";
import SignInLogo from "../../img/SignIn.jpg";
import CitiesLogo from "../../img/cities.jpg";
import HotelLogo from "../../img/hotel.jpg";
import RestaurantsLogo from "../../img/restaurants.jpg";
import InterestPointLogo from "../../img/InterestPoint.jpg";

export const Home = () => {
	const navigate = useNavigate();

	return (
		<div className="container-fluid text-center home-container">
			{/* Carrusel de imágenes con desplazamiento automático */}
			<Carousel interval={4000} controls={false} indicators={false} pause="hover">
				<Carousel.Item>
					<img className="d-block w-100 home-image" src={PatinetaTravelImag1} alt="Slide 1" />
				</Carousel.Item>
				<Carousel.Item>
					<img className="d-block w-100 home-image" src={PatinetaTravelImag2} alt="Slide 2" />
				</Carousel.Item>
				<Carousel.Item>
					<img className="d-block w-100 home-image" src={PatinetaTravelImag3} alt="Slide 3" />
				</Carousel.Item>
				<Carousel.Item>
					<img className="d-block w-100 home-image" src={PatinetaTravelImag4} alt="Slide 4" />
				</Carousel.Item>
				<Carousel.Item>
					<img className="d-block w-100 home-image" src={PatinetaTravelImag5} alt="Slide 5" />
				</Carousel.Item>
			</Carousel>

			<p className="lead">Search, find and enjoy...</p>

			{/* Botones de Log In y Sign In */}
			<div className="d-flex justify-content-center my-4">
				<Button
					style={{ backgroundColor: "#4db6ac", color: "black", border: "2px solid black" }}
					className="mx-2 login-btn"
					onClick={() => navigate("/login")}
				>
					<img src={LoginLogo} alt="Log In" style={{ width: "30px", height: "30px", marginRight: "8px" }} /> Log In
				</Button>
				<Button
					style={{ backgroundColor: "#ff8a80", color: "black", border: "2px solid black" }}
					className="mx-2 signin-btn"
					onClick={() => navigate("/signup")}
				>
					<img src={SignInLogo} alt="Sign In" style={{ width: "30px", height: "30px", marginRight: "8px" }} /> Sign In
				</Button>
			</div>

			{/* Sección de categorías */}
			<div className="categories">
				<button className="category-button" onClick={() => navigate("/signup")}>
					<img src={CitiesLogo} alt="Cities" className="icon" />
					<p>Cities</p>
				</button>
				<button className="category-button" onClick={() => navigate("/signup")}>
					<img src={RestaurantsLogo} alt="Restaurants" className="icon" />
					<p>Restaurant</p>
				</button>
				<button className="category-button" onClick={() => navigate("/signup")}>
					<img src={HotelLogo} alt="Hotel" className="icon" />
					<p>Hotel</p>
				</button>
				<button className="category-button" onClick={() => navigate("/signup")}>
					<img src={InterestPointLogo} alt="Interest Point" className="icon" />
					<p>Interest Point</p>
				</button>
			</div>
		</div>
	);
};
