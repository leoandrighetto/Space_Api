<template>
  <v-container class="py-10">
    <div class="d-flex align-center justify-space-between">
      <h2>Mars Rover - Curiosity</h2>
      <v-btn variant="outlined" color="secondary" @click="fetchMars">Atualizar</v-btn>
    </div>

    <v-alert v-if="error" type="error" variant="tonal" class="mt-4">
      {{ error }}
    </v-alert>

    <v-row class="mt-6" v-if="photos.length">
      <v-col cols="12" sm="6" md="4" v-for="photo in photos" :key="photo.id">
        <v-card class="space-card" variant="flat">
          <img :src="photo.img_src" :alt="photo.camera" style="width: 100%; height: 220px; object-fit: cover;" />
          <v-card-text>
            <div style="font-weight: 600;">{{ photo.camera }}</div>
            <div style="font-size: 0.85rem; opacity: 0.8;">{{ photo.earth_date }}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "../services/api";

const photos = ref([]);
const error = ref("");

const fetchMars = async () => {
  error.value = "";
  try {
    const { data } = await api.get("/api/mars-rover?sol=1000");
    photos.value = data.photos || [];
  } catch (err) {
    error.value = err.response?.data?.error || "Falha ao carregar Mars Rover";
  }
};

onMounted(fetchMars);
</script>
