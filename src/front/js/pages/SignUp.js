import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "../../styles/loginform.css";
const SignUp = () => {
  const navigate = useNavigate();

  const [form, setForm] = useState({ name: "", email: "", password: "", confirmPassword: "",});

  const [errors, setErrors] = useState({});

  const validateEmail = (email) => {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  };

  const validateName = (name) => {
    const re = /^[a-zA-Z\s]+$/;
    return re.test(name);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });

    let newErrors = { ...errors };

    if (name === "email" && !validateEmail(value)) {
      newErrors.email = "⚠ Please enter a valid email!";
    } else {
      delete newErrors.email;
    }

    if (name === "name" && !validateName(value)) {
      newErrors.name = "⚠ Name should contain only letters!";
    } else {
      delete newErrors.name;
    }

    if (name === "confirmPassword" && value !== form.password) {
      newErrors.confirmPassword = "⚠ Passwords do not match!";
    } else {
      delete newErrors.confirmPassword;
    }

    setErrors(newErrors);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (Object.keys(errors).length > 0 || !form.name || !form.email || !form.password || !form.confirmPassword) {
      alert("❌ Please correct the errors before submitting!");
      return;
    }

    console.log("User registered:", form);
    alert("✅ Account created successfully!");
    navigate("/login");
  };

  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="card shadow-lg p-5 signup-card">
        <h2 className="text-center mb-4">Create an Account</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Name</label>
            <input type="text" name="name" className="form-control" placeholder="Your name" value={form.name} onChange={handleChange} required />
            {errors.name && <p className="text-danger mt-1">{errors.name}</p>}
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input type="email" name="email" className="form-control" placeholder="Your email" value={form.email} onChange={handleChange} required/>
            {errors.email && <p className="text-danger mt-1">{errors.email}</p>}
          </div>

          <div className="mb-3">
            <label className="form-label">Password</label>
            <input type="password" name="password" className="form-control" placeholder="Your password" value={form.password} onChange={handleChange} required />
          </div>

          <div className="mb-3">
            <label className="form-label">Confirm Password</label>
            <input type="password" name="confirmPassword" className="form-control" placeholder="Confirm your password" value={form.confirmPassword} onChange={handleChange} required />
            {errors.confirmPassword && <p className="text-danger mt-1">{errors.confirmPassword}</p>}
          </div>

          <button type="submit" className="btn btn-primary w-100 mb-3" disabled={Object.keys(errors).length > 0}>
            Sign Up
          </button>

          <button type="button" className="btn btn-outline-secondary w-100 mb-3" onClick={() => navigate("/login")}>
            You already have an account? Log In
          </button>

          <button type="button" className="btn btn-outline-dark w-100" onClick={() => navigate("/")}>
            ⬅ Back to Home
          </button>
        </form>
      </div>
    </div>
  );
};

export default SignUp;
