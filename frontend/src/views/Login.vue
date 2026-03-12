<template>
  <v-container class="py-12">
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card class="space-card" variant="flat">
          <v-card-title>Entrar</v-card-title>
          <v-card-text>
            <v-text-field v-model="username" label="Usuario" />
            <v-text-field v-model="password" label="Senha" type="password" />
            <v-alert v-if="auth.error" type="error" variant="tonal" class="mt-4">
              {{ auth.error }}
            </v-alert>
          </v-card-text>
          <v-card-actions class="pa-4">
            <v-btn color="primary" :loading="auth.loading" @click="handleLogin">
              Entrar
            </v-btn>
            <v-spacer />
            <v-btn variant="text" :to="{ name: 'register' }">Criar conta</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useAuthStore } from "../stores/auth";

const router = useRouter();
const route = useRoute();
const auth = useAuthStore();

const username = ref("");
const password = ref("");

const handleLogin = async () => {
  try {
    await auth.login(username.value, password.value);
    router.push(route.query.redirect || "/");
  } catch {
    // error handled in store
  }
};
</script>
