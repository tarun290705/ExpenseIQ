import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000/api' });

export const getGroupMembers = (groupId) => API.get(`/groups/${groupId}/members`);
export const updateMemberRole = (groupId, memberId, roleData) => API.put(`/groups/${groupId}/members/${memberId}/role`, roleData);