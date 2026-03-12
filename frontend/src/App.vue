<template>
  <v-app class="app-shell">
    <v-navigation-drawer
      v-model="drawer"
      class="app-drawer"
      width="280"
      temporary
    >
      <div class="drawer-header">
        <img src="/logo.svg" alt="Space A.P.I" width="40" height="40" />
        <div>
          <div class="drawer-title">Space A.P.I</div>
          <div class="drawer-subtitle">Agencias Espaciais</div>
        </div>
      </div>
      <v-divider class="my-2" />
      <v-list nav density="comfortable">
        <v-list-item title="Inicio" :to="{ name: 'home' }" />
        <v-list-item title="APOD" :to="{ name: 'apod' }" />
        <v-list-item title="EPIC" :to="{ name: 'epic' }" />
        <v-list-item title="Mars Rover" :to="{ name: 'mars' }" />
      </v-list>
      <v-divider class="my-2" />
      <v-list nav density="comfortable">
        <v-list-subheader>Em breve</v-list-subheader>
        <v-list-item title="Missoes e Lançamentos" disabled />
        <v-list-item title="Mapa Celeste" disabled />
        <v-list-item title="Biblioteca de Estudos" disabled />
      </v-list>
      <v-divider class="my-2" />
      <v-list nav density="comfortable">
        <v-list-item
          v-if="!auth.isAuthenticated"
          title="Entrar"
          :to="{ name: 'login' }"
        />
        <v-list-item
          v-else
          title="Sair"
          @click="auth.logout"
        />
      </v-list>
    </v-navigation-drawer>

    <v-app-bar elevation="0" color="transparent" class="app-bar">
      <v-container class="header-content">
        <div class="header-left">
          <v-app-bar-nav-icon @click="drawer = !drawer" />
          <div class="brand">
            <img src="/logo.svg" alt="Space A.P.I" width="36" height="36" />
            <div>
              <div class="brand-title">SPACE A.P.I</div>
              <div class="brand-subtitle">Agencias Espaciais</div>
            </div>
          </div>
        </div>
        <div class="nav-actions d-none d-md-flex">
          <v-btn variant="text" :to="{ name: 'home' }">Inicio</v-btn>
          <v-btn variant="text" :to="{ name: 'apod' }">APOD</v-btn>
          <v-btn variant="text" :to="{ name: 'epic' }">EPIC</v-btn>
          <v-btn variant="text" :to="{ name: 'mars' }">Mars Rover</v-btn>
          <v-btn
            v-if="auth.isAuthenticated"
            variant="outlined"
            color="secondary"
            @click="auth.logout"
          >
            Sair
          </v-btn>
          <v-btn
            v-else
            variant="outlined"
            color="secondary"
            :to="{ name: 'login' }"
          >
            Entrar
          </v-btn>
        </div>
      </v-container>
    </v-app-bar>

    <v-main class="main-content">
      <router-view />
    </v-main>

    <v-footer class="pa-6" color="transparent">
      <v-container class="d-flex justify-space-between" style="font-size: 0.85rem;">
        <span>Space A.P.I - Explorando o universo com dados de agencias espaciais.</span>
        <span>Flask + Vue + Vuetify</span>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "./stores/auth";

const auth = useAuthStore();
const drawer = ref(false);
</script>
