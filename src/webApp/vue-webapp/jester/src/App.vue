<template>
  <div id="app">
    <Nav v-on:active-view='activeView'/>
    <Camera v-if="active_view === 1"/>
    <Info v-if="active_view === 3"/>
    <Gallery v-if="active_view === 2"/>
  </div>
</template>

<script>
import Nav from './components/Nav';
import Camera from './components/Camera';
import Info from './components/Info';
import Gallery from './components/Gallery';

export default {
  name: 'App',
  components: {
    Nav,
    Camera,
    Info,
    Gallery
  },
  data() {
    return {
      active_view: 1
    };
  },
  methods: {
        activeView(num) {
            this.active_view = num;
        }
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
