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
          <v-card class="space-card" variant="flat">
            <v-card-text>
              <h3>APOD - Nasa</h3>
              <p>Imagem astronomica do dia com explicacao oficial.</p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" :to="{ name: 'apod' }">Abrir APOD</v-btn>
            </v-card-actions>
          </v-card>

          <v-card class="space-card" variant="flat">
            <v-card-text>
              <h3>EPIC - Nasa</h3>
              <p>Fotos do planeta Terra capturadas pelo satelite DSCOVR.</p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" :to="{ name: 'epic' }">Abrir EPIC</v-btn>
            </v-card-actions>
          </v-card>

          <v-card class="space-card" variant="flat">
            <v-card-text>
              <h3>Mars Rover</h3>
              <p>Galeria de imagens feitas pelos rovers da NASA em Marte.</p>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" :to="{ name: 'mars' }">Abrir Mars Rover</v-btn>
            </v-card-actions>
          </v-card>
        </div>
      </v-container>
    </section>
  </div>
</template>

<script setup>
import { useAuthStore } from "../stores/auth";

const auth = useAuthStore();
</script>
