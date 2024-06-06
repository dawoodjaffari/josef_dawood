<template>
  <HeaderPage />
  <router-view></router-view>
  <FooterPage />
</template>

<script>
import HeaderPage from './components/HeaderPage.vue'
import FooterPage from './components/FooterPage.vue'

export default {
  name: 'App',
  components: {
    HeaderPage,
    FooterPage

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
