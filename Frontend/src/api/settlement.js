import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000/api' });

export const getSettlements = (groupId) => API.get(`/groups/${groupId}/settlements`);
export const settleUp = (groupId, settlementData) => API.post(`/groups/${groupId}/settlements`, settlementData);