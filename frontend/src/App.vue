<template>
  <v-app class="app-shell">
    <v-app-bar elevation="0" color="transparent" class="app-nav">
      <v-container class="app-nav-content">
        <div class="app-nav-title">Space A.P.I</div>
      </v-container>
    </v-app-bar>

    <v-main>
      <div class="header-bar">
        <v-container class="header-content">
          <div class="header-brand">
            <img src="/logo.svg" alt="Space A.P.I" width="36" height="36" />
            <div>
              <div class="brand-title">SPACE A.P.I</div>
              <div class="brand-subtitle">Agencias Espaciais</div>
            </div>
          </div>
          <v-spacer />
          <div class="header-actions">
          <v-btn :to="{ name: 'home' }">Inicio</v-btn>
          <v-btn :to="{ name: 'apod' }">APOD</v-btn>
          <v-btn :to="{ name: 'epic' }">EPIC</v-btn>
          <v-btn :to="{ name: 'mars' }">Mars Rover</v-btn>
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
      </div>

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
import { useAuthStore } from "./stores/auth";

const auth = useAuthStore();
</script>
