<template>
  <div id="app">
    <Nav/>
    <!---video tag is a placeholder for the camera/gallery/info components ---->
    <video id="preview" playsinline autoplay muted></video>
  </div>
</template>

<script>
import Nav from './components/Nav';
export default {
  name: 'App',
  components: {
    Nav
  },
  data() {
    return {
      msg: ""
    };
  },
  mounted() {
    const preview = document.querySelector('video#preview');

    // Access camera 
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // {audo: true} to get audio
      navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        window.stream = stream;
        // Play video stream in preview box
        preview.srcObject = stream;
      });
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
