import React from "react";
import { useLocation } from "react-router-dom";
import ImageCard from "../components/ImageCard";

const Results = () => {
  const { state } = useLocation();
  const images = state?.results || [];

  return (
    <div className="p-6 grid grid-cols-2 md:grid-cols-3 gap-4">
      {images.length > 0 ? (
        images.map((img, idx) => <ImageCard key={idx} src={img.url} alt={img.id} />)
      ) : (
        <p>No results found.</p>
      )}
    </div>
  );
};

export default Results;
