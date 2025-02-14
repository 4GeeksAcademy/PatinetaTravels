import React from "react";
//Falta importar logo

const LoginForm = () => {
  return (
    <div className="d-flex justify-content-center align-items-center vh-100 bg-light">
      <div className="card p-4 shadow-lg" style={{ width: "22rem" }}>
        <div className="text-center mb-4">
          <img src="logo" alt="Patineta Travel Logo" className="w-50" />
        </div>
        <h2 className="text-center">Welcome!</h2>
        <form>
          <div className="mb-3">
            <label className="form-label">Email</label>
            <input type="email" className="form-control" placeholder="Your email" />
          </div>
          <div className="mb-3">
            <label className="form-label">Password</label>
            <input type="password" className="form-control" placeholder="Your password" />
          </div>
          <button type="submit" className="btn btn-primary w-100">
            Continue
          </button>
        </form>
        <p className="mt-3 text-center">
          Have an Account? <a href="#" className="text-danger fw-bold">Sign In</a>
        </p>
      </div>
    </div>
  );
};

export default LoginForm;