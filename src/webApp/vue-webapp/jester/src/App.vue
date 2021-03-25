<template>
  <div id="app">
    <Nav v-on:active-view='setActiveView'/>
    <Camera v-on:caputure-image='storeImage' v-on:recorded-video='storeVideo' v-if="active_view === 1"/>
    <Info v-if="active_view === 3"/>
    <Gallery v-bind:photo="photos" v-bind:video="videos" v-if="active_view === 2"/>
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
      active_view: 1,
      photos: [],
      videos: '', 
    };
  },
  methods: {
        setActiveView(num) {
            this.active_view = num;
        },
        storeImage(blob) {
          this.photos.push(blob); 
          if (this.photos.length > 2){
            //drop first element in array
            this.photos.shift()
          }
        },
        storeVideo(blob) {
          this.videos = blob;
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
