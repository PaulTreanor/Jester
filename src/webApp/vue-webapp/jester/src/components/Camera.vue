<template>
    <div>
        <video id="preview" playsinline autoplay muted></video>
    </div>
</template>

<script>
export default {
    name: "Camera",
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

<style scoped>

</style>