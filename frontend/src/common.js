import axios from "axios";

export const HTTP = axios.create({
  baseURL: "http://localhost:8000/api/v1/",
});

export const AUTH = axios.create({
  baseURL: "http://localhost:8000/auth/",
});
