<template>
    <main >
        <div class="d-flex justify-content-center">
            <video id="preview" playsinline autoplay muted></video>
        </div>     
        <canvas id="canvas"> </canvas>        
        <b-container class="pointers text-center">
            <p>Use gestures to control the camera!</p>
            <b-row class="justify-content-md-center">
                <a id="photo"  class="gesture">
                    <i class="icon far fa-hand-peace fa-2x"></i>
                    <p>Photo</p>
                </a>
                <a id="record"  class="gesture">
                    <i class="icon far fa-thumbs-up fa-2x"></i>
                    <p>Start</p>
                </a>
                <a id="stop"  class="gesture">
                    <i class="icon far fa-hand-paper fa-2x"></i>
                    <p>Stop</p>
                </a>
            </b-row>
        </b-container>
    </main>
</template>

<script>
export default {
    name: "Camera",
    mounted() {
        let mediaRecorder;
        let recordedBlobs;
        let vidLength = 10000;
        var canvas = document.getElementById('canvas');
        //Don't display the canvas
        canvas.style.display="none";
        var context = canvas.getContext('2d');
        context.canvas.width = 640;
        context.canvas.height = 480;
        var vm = this;
        const photoButton = document.querySelector('#photo');
        const recordButton = document.querySelector('#record');
        const stopButton = document.querySelector('#stop');
        const preview = document.querySelector('video#preview');
        var post_url = "http://192.168.43.105:5000/image";
        var recording = false;


        // Start video
        photoButton.addEventListener('click', () => {        
            if (!recording) {       // Can't take photo and video at same time
                takePhoto();
            } 
        });

        // Start video
        recordButton.addEventListener('click', () => {          
            if (!recording) {
                startRecording(vidLength);
            } 
        });

        // Stop video
        stopButton.addEventListener('click', () => {     
            if (recording) {
                stopRecording();
            }
        });

        function snapCanvas(){
            context.drawImage(preview, 0, 0, 640,  480);
        }

    
        // ------------- MEDIA STREAM FUNCTIONS ---------------//

        function handleDataAvailable(event) {
            if (event.data && event.data.size > 0) {
                recordedBlobs.push(event.data);
            }
        }

        function startRecording(vidLength) {
            flashGesture(recordButton); 
            tempAlert("Starting to record",2000);  
            recordedBlobs = [];
            mediaRecorder = new MediaRecorder(window.stream, {mimeType: 'video/webm'});
            recording = true;
            mediaRecorder.ondataavailable = handleDataAvailable;
            mediaRecorder.start();
            setTimeout(function(){
                checkVideoStop();
            }, vidLength); 
        }

        function stopRecording() { 
            mediaRecorder.stop();
            flashGesture(stopButton); 
            tempAlert("Stopping recording",2000); 
            recording = false;
            // emit recorded video blob 
            vm.$emit('recorded-video', recordedBlobs);  
        }

        function pauseMedia() {
            mediaRecorder.requestData();
            mediaRecorder.pause();
        }

        function resumeMedia() {
            mediaRecorder.resume();
            setTimeout(function(){
                checkVideoStop();
            }, vidLength); 
        }


        function checkVideoStop() {
            pauseMedia();   // Pausing allows chance for server to update
            updateServer();
        }

        // Access camera and display preview at id='preview'
        if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true, audio: true }).then(function(stream) {
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
                tempAlert(text,3000);
                if (text =="palm"){
                    stopRecording();
                }
                if (text == "peace"){
                    takePhoto();
                }
                if (text == "thumbs_up"){
                    startRecording(vidLength);
                }
                // resumemedia() will do nothing unless video on and paused 
                resumeMedia();               
            });
        }

        function tempAlert(msg,duration){
            var popup = document.createElement("popup");
            popup.setAttribute("style","position:absolute;top:20%;left:45%;border-style: solid;background-color:white;padding:10px");
            popup.innerHTML = msg;
            setTimeout(function(){
                popup.parentNode.removeChild(popup);
                },duration);
            document.body.appendChild(popup);
        }

        function flashGesture(element){
            element.className += ' feedback';
            setTimeout(function(){
                element.className = element.className.replace(/\bfeedback\b/, '');
            }, 900);
        }

        function takePhoto(){
            tempAlert("Taking photo!",2000);  
            flashGesture(photoButton);  
            snapCanvas()
            canvas.toBlob(function(blob){
                // emit blob for storage in gallery
                vm.$emit('caputure-image', blob);
            }, 'image/jpeg', 0.95)
        }
        
        function updateServer(){            
            snapCanvas();
            canvas.toBlob(function(blob){
                // post regular snapshots to server for gesture analysis
                postData(post_url, blob)
            }, 'image/jpeg', 0.95)
        }
        // Take and send photo every x seconds
        window.setInterval(updateServer, 15000);
    }
}
</script>

<style scoped>
    #preview {
        width: 100%;
        max-width: 900px;
        height: auto;
    }

    .pointers {
        width: auto;
        
    }

    .gesture {
        margin: 10px;
        opacity: 0.4;
        color: black;
    }

    @keyframes spin {
        from {
            transform:rotate(0deg);
        }
        to {
            transform:rotate(360deg);
        }
    }
  
    @media only screen and (min-width: 600px) {
        .pointers {
            border-style: solid;
            color: white;
            left: 50%;
            bottom: 0px;
            position: absolute;
            background: linear-gradient(180deg, rgba(16, 16, 16, 0.1) 0%, rgba(0, 0, 0, .5) 50%);            
        }
        
        .gesture {
            color: white;
        }
    }

    .feedback {
        opacity: 1;
        color: purple;    
        transition-property: opacity, color;
        transition-duration: 1s;
        transition-delay: 0s;
        animation-name: spin;
        animation-duration: 800ms;
        animation-iteration-count: infinite;
        animation-timing-function: linear; 
    } 
</style>