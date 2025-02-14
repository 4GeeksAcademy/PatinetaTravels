import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../../styles/mainview.css";

export const MainView = () => {
  const [cities, setCities] = useState([]);
  const [search, setSearch] = useState("");
  const [filteredResults, setFilteredResults] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const mockCities = [
      {
        id: 1,
        name: "Barcelona",
        description: "Hoteles, restaurantes y sitios increíbles",
        image: "https://www.castlexperience.com/wp-content/uploads/2017/03/barcelona1.jpg",
      },
      {
        id: 2,
        name: "Madrid",
        description: "Descubre la capital de España",
        image: "https://www.solofondos.com/wp-content/uploads/2020/11/Madrid-Spain-city-night-buildings-road-lights_1920x1200.jpg",
      },
      {
        id: 3,
        name: "Valencia",
        description: "Conocida por su Ciudad de las Artes y las Ciencias",
        image: "https://www.fundacioncarolina.es/wp-content/uploads/2018/04/Espana_Valencia_CiudaddelasArtesylasCiencias_500px_55251876_Luca-Quadrio_500px-1.jpg",
      },
      {
        id: 4,
        name: "A Coruña",
        description: "Descubre la capital de Galicia",
        image: "https://www.coruna.gal/IMG/P_Contenido_1453790080210_1152702150702_1920_1280_U_5932917592e7554bd994414d6e49666.png",
      },
    ];
    setCities(mockCities);
  }, []);

  const handleSearch = (e) => {
    const query = e.target.value.toLowerCase();
    setSearch(query);
    if (query.trim() === "") {
      setFilteredResults([]);
    } else {
      const results = cities.filter((city) => city.name.toLowerCase().includes(query));
      setFilteredResults(results);
    }
  };

  const handleCityClick = (cityId) => {
    navigate(`/city/${cityId}`);
    setSearch("");
    setFilteredResults([]);
  };

  const handleFavorite = (city) => {
    setFavorites((prevFavorites) =>
      prevFavorites.includes(city) ? prevFavorites.filter((fav) => fav !== city) : [...prevFavorites, city]
    );
  };

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  return (
    <div className="container mainview-container">
      {/* Barra de búsqueda */}
      <div className="d-flex justify-content-between align-items-center mb-4">
        <div className="position-relative w-50">
          <input
            type="text"
            className="form-control rounded-pill px-3"
            placeholder="Buscar ciudades..."
            value={search}
            onChange={handleSearch}
          />
          {filteredResults.length > 0 && (
            <ul
              className="list-group position-absolute w-100 mt-1"
              style={{
                zIndex: 1000,
                maxHeight: "200px",
                overflowY: "auto",
                backgroundColor: "#fff",
              }}
            >
              {filteredResults.map((city) => (
                <li
                  key={city.id}
                  className="list-group-item list-group-item-action"
                  onClick={() => handleCityClick(city.id)}
                  style={{ cursor: "pointer" }}
                >
                  {city.name}
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* Dropdown de favoritos */}
        <div className="dropdown ml-3">
          <button
            className="btn btn-warning dropdown-toggle"
            type="button"
            onClick={toggleDropdown}
            aria-expanded={isDropdownOpen}
          >
            Favoritos ({favorites.length})
          </button>

          {isDropdownOpen && (
            <ul className="dropdown-menu dropdown-menu-end show mt-2" style={{ right: 0, left: "auto" }}>
              {favorites.length > 0 ? (
                favorites.map((city, index) => (
                  <li key={index} className="dropdown-item d-flex justify-content-between align-items-center">
                    <span onClick={() => handleCityClick(city.id)} style={{ cursor: "pointer", color: "blue" }}>
                      {city.name}
                    </span>
                    <button className="btn btn-danger btn-sm" onClick={() => handleFavorite(city)}>
                      <i className="fa fa-trash"></i>
                    </button>
                  </li>
                ))
              ) : (
                <li className="dropdown-item text-muted">No favorites added yet</li>
              )}
            </ul>
          )}
        </div>
      </div>

      <h2 className="text-center mb-4 mainview-title">Cities</h2>

      {/* Lista de ciudades */}
      <div className="row">
        {cities
          .filter((city) => city.name.toLowerCase().includes(search))
          .map((city) => (
            <div key={city.id} className="col-md-4 mb-4">
              <div className="card city-card">
                <img src={city.image} className="card-img-top city-image" alt={city.name} />
                <div className="card-body">
                  <h5 className="card-title">{city.name}</h5>
                  <p className="card-text">{city.description}</p>
                  <div className="d-flex justify-content-between">
                    <button className="btn btn-primary" onClick={() => handleCityClick(city.id)}>
                      More Information
                    </button>
                    <button
                      className={`btn ${favorites.includes(city) ? "btn-success" : "btn-outline-danger"}`}
                      onClick={() => handleFavorite(city)}
                    >
                      {favorites.includes(city) ? "❤️ Favorito" : "🤍 Agregar"}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))}
      </div>
    </div>
  );
};
