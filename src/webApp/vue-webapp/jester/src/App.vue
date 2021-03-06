<template>
  <div id="app">
    <Nav/>
  </div>
</template>

<script>
import Nav from './components/Nav';
export default {
  name: 'App',
  components: {
    Nav
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif; /* this is a nice font */
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

</style>
