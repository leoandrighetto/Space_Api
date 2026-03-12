<template>
  <v-container class="py-10 page-wrap">
    <div class="page-top">
      <v-btn variant="text" class="back-btn" @click="goBack">Voltar</v-btn>
      <v-btn variant="outlined" color="secondary" @click="fetchApod">Atualizar</v-btn>
    </div>
    <h2 class="page-title">APOD - Astronomy Picture of the Day</h2>

    <v-alert v-if="error" type="error" variant="tonal" class="mt-4">
      {{ error }}
    </v-alert>

    <div v-if="apod" class="mt-6">
      <div class="media-frame">
        <img v-if="apod.media_type === 'image'" :src="apod.hdurl || apod.url" :alt="apod.title" style="width: 100%; display: block;" />
        <iframe
          v-else
          :src="apod.url"
          title="APOD video"
          style="width: 100%; height: 480px; border: none;"
        />
      </div>
      <v-card class="space-card mt-6" variant="flat">
        <v-card-text>
          <h3>{{ apod.title }}</h3>
          <p><strong>Data:</strong> {{ apod.date }}</p>
          <p>{{ apod.explanation }}</p>
        </v-card-text>
      </v-card>
    </div>
  </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import api from "../services/api";

const apod = ref(null);
const error = ref("");
const router = useRouter();

const fetchApod = async () => {
  error.value = "";
  try {
    const { data } = await api.get("/api/apod");
    apod.value = data;
  } catch (err) {
    error.value = err.response?.data?.error || "Falha ao carregar APOD";
  }
};

const goBack = () => {
  router.back();
};

onMounted(fetchApod);
</script>
