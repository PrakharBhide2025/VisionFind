import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => (
  <nav className="bg-blue-600 text-white p-4 flex justify-between">
    <Link to="/" className="font-bold">ImageSearch</Link>
    <div className="space-x-4">
      <Link to="/upload">Upload</Link>
      <Link to="/search">Search</Link>
      <Link to="/health">Health</Link>
    </div>
  </nav>
);

export default Navbar;
