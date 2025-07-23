import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000/api' });

export const uploadAttachment = (expenseId, file) => {
  const formData = new FormData();
  formData.append('file', file);
  return API.post(`/expenses/${expenseId}/attachments`, formData);
};
export const getAttachments = (expenseId) => API.get(`/expenses/${expenseId}/attachments`);