import React, { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

const Search = () => {
  const [query, setQuery] = useState("");
  const navigate = useNavigate();

  const handleSearch = async () => {
    const res = await api.get("/search", { params: { q: query } });
    navigate("/results", { state: { results: res.data } });
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Search Images</h1>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border p-2 rounded"
        placeholder="Enter query"
      />
      <button onClick={handleSearch} className="ml-2 px-4 py-2 bg-blue-600 text-white rounded">Search</button>
    </div>
  );
};

export default Search;
