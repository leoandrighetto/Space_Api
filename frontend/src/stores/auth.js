import { defineStore } from "pinia";
import api from "../services/api";

const STORAGE_KEY = "spaceapi_token";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem(STORAGE_KEY) || "",
    user: null,
    loading: false,
    error: "",
  }),
  getters: {
    isAuthenticated: (state) => Boolean(state.token),
  },
  actions: {
    async login(username, password) {
      this.loading = true;
      this.error = "";
      try {
        const { data } = await api.post("/auth/login", { username, password });
        this.token = data.access_token;
        localStorage.setItem(STORAGE_KEY, this.token);
      } catch (err) {
        this.error = err.response?.data?.error || "Falha ao entrar";
        throw err;
      } finally {
        this.loading = false;
      }
    },
    async register(username, password) {
      this.loading = true;
      this.error = "";
      try {
        await api.post("/auth/register", { username, password });
      } catch (err) {
        this.error = err.response?.data?.error || "Falha ao registrar";
        throw err;
      } finally {
        this.loading = false;
      }
    },
    logout() {
      this.token = "";
      localStorage.removeItem(STORAGE_KEY);
    },
  },
});
