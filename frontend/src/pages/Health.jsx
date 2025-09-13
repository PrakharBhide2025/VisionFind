import React, { useEffect, useState } from "react";
import api from "../services/api";

const Health = () => {
  const [status, setStatus] = useState(null);

  useEffect(() => {
    api.get("/health").then(res => setStatus(res.data)).catch(() => setStatus({status: "DOWN"}));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">System Health</h1>
      {status ? (
        <pre className="bg-gray-100 p-4 rounded">{JSON.stringify(status, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Health;
