import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Upload from "../pages/Upload";
import Search from "../pages/Search";
import Results from "../pages/Results";
import Health from "../pages/Health";

const Router = () => (
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/upload" element={<Upload />} />
    <Route path="/search" element={<Search />} />
    <Route path="/results" element={<Results />} />
    <Route path="/health" element={<Health />} />
  </Routes>
);

export default Router;
