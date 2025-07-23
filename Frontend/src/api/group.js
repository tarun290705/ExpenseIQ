import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000/api' });

export const createGroup = (groupData) => API.post('/groups', groupData);
export const getGroups = () => API.get('/groups');
export const getGroupById = (groupId) => API.get(`/groups/${groupId}`);
export const addMember = (groupId, memberData) => API.post(`/groups/${groupId}/members`, memberData);