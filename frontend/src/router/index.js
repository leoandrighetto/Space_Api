import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../stores/auth";

import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Apod from "../views/Apod.vue";
import Epic from "../views/Epic.vue";
import Mars from "../views/Mars.vue";

const routes = [
  { path: "/", name: "home", component: Home },
  { path: "/login", name: "login", component: Login },
  { path: "/register", name: "register", component: Register },
  {
    path: "/apod",
    name: "apod",
    component: Apod,
    meta: { requiresAuth: true },
  },
  {
    path: "/epic",
    name: "epic",
    component: Epic,
    meta: { requiresAuth: true },
  },
  {
    path: "/mars",
    name: "mars",
    component: Mars,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to) => {
  const auth = useAuthStore();
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    return { name: "login", query: { redirect: to.fullPath } };
  }
  return true;
});

export default router;
