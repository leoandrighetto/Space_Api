<template>
  <v-container class="py-12">
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card class="space-card" variant="flat">
          <v-card-title>Criar conta</v-card-title>
          <v-card-text>
            <v-text-field v-model="username" label="Usuario" />
            <v-text-field v-model="password" label="Senha" type="password" />
            <v-alert v-if="auth.error" type="error" variant="tonal" class="mt-4">
              {{ auth.error }}
            </v-alert>
            <v-alert v-if="success" type="success" variant="tonal" class="mt-4">
              Conta criada. Agora faca login.
            </v-alert>
          </v-card-text>
          <v-card-actions class="pa-4">
            <v-btn color="primary" :loading="auth.loading" @click="handleRegister">
              Registrar
            </v-btn>
            <v-spacer />
            <v-btn variant="text" :to="{ name: 'login' }">Voltar</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "../stores/auth";

const auth = useAuthStore();
const username = ref("");
const password = ref("");
const success = ref(false);

const handleRegister = async () => {
  try {
    await auth.register(username.value, password.value);
    success.value = true;
  } catch {
    success.value = false;
  }
};
</script>
