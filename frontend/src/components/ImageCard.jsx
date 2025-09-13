import React from "react";

const ImageCard = ({ src, alt }) => (
  <div className="rounded shadow p-2 bg-white">
    <img src={src} alt={alt} className="w-full h-auto rounded" />
  </div>
);

export default ImageCard;
