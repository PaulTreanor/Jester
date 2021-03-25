<template>
    <div>
        <!--Standard Camera.Vue preview -->
        <video id="preview" playsinline autoplay muted></video>
        <!----end-------->
        <!-------POTENTIALLY HIDE CANVAS USING BOOTSTRAP------->
        <canvas id="canvas" width="640" height="480" style="border: 1px solid black;"> </canvas>
        <div>
            <button id="record" disabled>Start Recording</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "Camera",
    mounted() {
        let mediaRecorder;
        let recordedBlobs;

        let vidLength = 3000;
        var canvas = document.getElementById('canvas');
        //Don't display the canvas
        canvas.style.display="none";
        var context = canvas.getContext('2d');
        var vm = this;
        const recordButton = document.querySelector('button#record');
        const preview = document.querySelector('video#preview');

        var post_url = "http://192.168.43.105:5000/image";
        // -------------------- UI FUNCTIONS -------------------//

        // Start/stop video
        recordButton.addEventListener('click', () => {
        if (recordButton.textContent === 'Start Recording') {
            startRecording(vidLength);
        } else {
            stopRecording();
        }
        });

        function takePhoto(){
        context.drawImage(preview, 0, 0, 640, 480);
        }

    
        // ------------- DATA FUNCTIONS ---------------//

        function handleDataAvailable(event) {
        if (event.data && event.data.size > 0) {
            recordedBlobs.push(event.data);
        }
        }

        function startRecording(vidLength) {
        recordedBlobs = [];
        mediaRecorder = new MediaRecorder(window.stream, {mimeType: 'video/webm'});
        recordButton.textContent = 'Stop Recording';
        mediaRecorder.ondataavailable = handleDataAvailable;
        mediaRecorder.start();
        setTimeout(function(){
            checkVideoStop();
            }, vidLength); 
        
        }

        function stopRecording() {
        mediaRecorder.stop();
        recordButton.textContent = 'Start Recording';
        // emit recorded video blob 
        vm.$emit('recorded-video', recordedBlobs);  
        }

        function pauseMedia() {
  mediaRecorder.requestData();
  mediaRecorder.pause();
  //play();
}

function resumeMedia() {
  mediaRecorder.resume();
  setTimeout(function(){
      checkVideoStop();


  }, vidLength); 
}


function checkVideoStop() {
  pauseMedia();
  //check handgesture 
  updateServer();
    // palm =
}

        // Access camera and display preview at id='preview'
        if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // {audo: true} to get audio
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            recordButton.disabled = false;
            window.stream = stream;
            // Play video stream in preview box
            preview.srcObject = stream;
        });
        }

        // Send screenshots to server
        async function postData(post_url, image) {
            let formData = new FormData();
            formData.append('file', image);
            console.log(image);

            const response = await fetch(post_url, {
            method: 'POST',
            body: formData
            });

            response.text().then(function (text) {
                console.log(text)
                alert(text);
                if (text =="palm"){
                stopRecording();
                }
                if (text == "peace"){
                takePhoto();
                }
                if (text == "thumbs_up"){
                startRecording(vidLength);
                }
                
                resumeMedia();
                
            });
        }
        
        function updateServer(){
            takePhoto();
            canvas.toBlob(function(blob){
                    //I can porbably remove this variable right?
                    var image = blob;

                    // emit blob for storage in gallery
                    vm.$emit('caputure-image', blob);
                    postData(post_url, image)
                }, 'image/jpeg', 0.95)
        }
        // Take and send photo every x seconds
        window.setInterval(updateServer, 20000);
    }
}
</script>

<style scoped>

</style>