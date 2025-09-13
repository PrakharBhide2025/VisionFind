import { useState, useEffect } from "react";
import api from "../services/api";

const useApi = (endpoint) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get(endpoint).then(res => {
      setData(res.data);
      setLoading(false);
    });
  }, [endpoint]);

  return { data, loading };
};

export default useApi;
