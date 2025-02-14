import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import "../../styles/cityview.css";

export const CityView = () => {
  const { cityId } = useParams(); // Obtiene el ID de la ciudad desde la URL
  const [city, setCity] = useState(null); // Información de la ciudad
  const [restaurants, setRestaurants] = useState([]);
  const [hotels, setHotels] = useState([]);
  const [interestPoints, setInterestPoints] = useState([]);

  useEffect(() => {
    // Simulación de datos de la ciudad y sus detalles (más adelante se conecta a la API)
    const mockData = {
      city: {
        id: cityId,
        name: "Barcelona",
        description: "Hoteles, restaurantes y sitios increíbles",
        image: "https://www.castlexperience.com/wp-content/uploads/2017/03/barcelona1.jpg",
      },
      restaurants: [
        { id: 1, name: "Restaurante A", description: "Comida mediterránea" },
        { id: 2, name: "Restaurante B", description: "Tapas españolas" },
      ],
      hotels: [
        { id: 1, name: "Hotel 1", description: "Hotel de lujo" },
        { id: 2, name: "Hotel 2", description: "Hotel boutique" },
      ],
      interestPoints: [
        { id: 1, name: "Sagrada Familia", description: "Famosa basílica" },
        { id: 2, name: "Parque Güell", description: "Parque emblemático" },
      ],
    };

    setCity(mockData.city);
    setRestaurants(mockData.restaurants);
    setHotels(mockData.hotels);
    setInterestPoints(mockData.interestPoints);
  }, [cityId]);

  if (!city) return <p>Cargando detalles de la ciudad...</p>;

  return (
    <div className="container cityview-container">
      {/* Información de la ciudad */}
      <div className="city-header">
        <img src={city.image} alt={city.name} className="city-image" />
        <h1>{city.name}</h1>
        <p>{city.description}</p>
      </div>

      {/* Restaurantes */}
      <h2>Restaurants</h2>
      <div className="row">
        {restaurants.map((restaurant) => (
          <div key={restaurant.id} className="col-md-4 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{restaurant.name}</h5>
                <p className="card-text">{restaurant.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Hoteles */}
      <h2>Hotel</h2>
      <div className="row">
        {hotels.map((hotel) => (
          <div key={hotel.id} className="col-md-4 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{hotel.name}</h5>
                <p className="card-text">{hotel.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Puntos de Interés */}
      <h2>interestPoint</h2>
      <div className="row">
        {interestPoints.map((point) => (
          <div key={point.id} className="col-md-4 mb-3">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{point.name}</h5>
                <p className="card-text">{point.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
