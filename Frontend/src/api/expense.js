import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000/api' });

export const addExpense = (groupId, expenseData) => API.post(`/groups/${groupId}/expenses`, expenseData);
export const getExpenses = (groupId) => API.get(`/groups/${groupId}/expenses`);
