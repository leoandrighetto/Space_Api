<template>
  <v-container class="py-10">
    <div class="d-flex align-center justify-space-between">
      <h2>EPIC - Earth Polychromatic Imaging Camera</h2>
      <v-btn variant="outlined" color="secondary" @click="fetchEpic">Atualizar</v-btn>
    </div>

    <v-alert v-if="error" type="error" variant="tonal" class="mt-4">
      {{ error }}
    </v-alert>

    <div v-if="image" class="mt-6">
      <div class="media-frame">
        <img :src="image.url" :alt="image.caption" style="width: 100%; display: block;" />
      </div>
      <v-card class="space-card mt-6" variant="flat">
        <v-card-text>
          <h3>{{ image.caption }}</h3>
          <p><strong>Data:</strong> {{ image.date }}</p>
        </v-card-text>
      </v-card>
    </div>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import api from "../services/api";

const image = ref(null);
const error = ref("");

const fetchEpic = async () => {
  error.value = "";
  try {
    const { data } = await api.get("/api/epic");
    image.value = data.images?.[0] || null;
  } catch (err) {
    error.value = err.response?.data?.error || "Falha ao carregar EPIC";
  }
};

onMounted(fetchEpic);
</script>
