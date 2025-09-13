import React, { useState } from "react";
import api from "../services/api";

const Upload = () => {
  const [file, setFile] = useState(null);
  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    await api.post("/upload", formData);
    alert("Uploaded successfully!");
  };
  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Upload Image</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="ml-2 px-4 py-2 bg-blue-600 text-white rounded">Upload</button>
    </div>
  );
};

export default Upload;
