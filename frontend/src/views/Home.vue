<template>
  <div>
    <section class="hero fade-in">
      <v-container>
        <div class="hero-title">Space A.P.I</div>
        <div class="hero-subtitle">
          Bem-vindo ao projeto Space A.P.I. Aqui voce encontra imagens e dados
          impressionantes de agencias espaciais, reunidos em um unico painel.
          Explore as rotas e descubra as maravilhas do nosso universo.
        </div>
        <v-alert
          v-if="!auth.isAuthenticated"
          class="mt-6"
          type="info"
          variant="tonal"
        >
          Para acessar as rotas de imagens, faca login.
        </v-alert>
        <div class="card-grid">
          <v-card
            class="space-card home-card"
            variant="flat"
            role="button"
            tabindex="0"
            @click="goTo('apod')"
            @keydown.enter="goTo('apod')"
            @keydown.space.prevent="goTo('apod')"
          >
            <v-card-text>
              <h3>APOD - Nasa</h3>
              <p>Imagem astronomica do dia com explicacao oficial.</p>
            </v-card-text>
          </v-card>

          <v-card
            class="space-card home-card"
            variant="flat"
            role="button"
            tabindex="0"
            @click="goTo('epic')"
            @keydown.enter="goTo('epic')"
            @keydown.space.prevent="goTo('epic')"
          >
            <v-card-text>
              <h3>EPIC - Nasa</h3>
              <p>Fotos do planeta Terra capturadas pelo satelite DSCOVR.</p>
            </v-card-text>
          </v-card>

          <v-card
            class="space-card home-card"
            variant="flat"
            role="button"
            tabindex="0"
            @click="goTo('mars')"
            @keydown.enter="goTo('mars')"
            @keydown.space.prevent="goTo('mars')"
          >
            <v-card-text>
              <h3>Mars Rover</h3>
              <p>Galeria de imagens feitas pelos rovers da NASA em Marte.</p>
            </v-card-text>
          </v-card>
        </div>
      </v-container>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";

const auth = useAuthStore();
const router = useRouter();

const goTo = (name) => {
  router.push({ name });
};
</script>
