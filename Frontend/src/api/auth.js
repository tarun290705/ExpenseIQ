import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000/api' });

export const login = (email, password) => API.post('/auth/login', { email, password });
export const register = (username, email, password) => API.post('/auth/register', { username, email, password });
export const logout = () => API.post('/auth/logout');
