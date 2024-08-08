<template>
  <v-app>
    <v-main>
      <Header></Header>
      <router-view />
      <Footer></Footer>
    </v-main>
  </v-app>
</template>

<script setup>
import Header from './components/header-footer/header.vue';
import Footer from  './components/header-footer/footer.vue'
</script>


<style>


</style>
