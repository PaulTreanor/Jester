<template>
    <div>
        <!--Standard Camera.Vue preview -->
        <video id="preview" playsinline autoplay muted></video>
        <!----end-------->
    
        <video id="recorded" playsinline loop></video>
        <canvas id="canvas" width="640" height="480" style="border: 1px solid black;"> </canvas>
        <div>
            <button id="record" disabled>Start Recording</button>
            <button id="play" disabled>Play</button>
            <button id="download" disabled>Download</button>
            <button id="snap">Snap Photo</button>
        </div>
        <img id="image"/>

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
        var context = canvas.getContext('2d');

        var vm = this;

        const recordedVideo = document.querySelector('video#recorded');
        const recordButton = document.querySelector('button#record');
        const snapButton = document.querySelector('button#snap');
        const preview = document.querySelector('video#preview');
        const playButton = document.querySelector('button#play');
        const downloadButton = document.querySelector('button#download');

        //DISPLAY IMAGE TAKEN 
        var myImage = document.querySelector('img#image');

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

        // Take screenshot/photo
        snapButton.addEventListener("click", function() {
        takePhoto();
        });

        function takePhoto(){
        context.drawImage(preview, 0, 0, 640, 480);
        }

        playButton.addEventListener('click', () => {
        const superBuffer = new Blob(recordedBlobs, {type: 'video/webm'});
        recordedVideo.src = window.URL.createObjectURL(superBuffer);
        recordedVideo.controls = true;
        recordedVideo.play();
        });

        downloadButton.addEventListener('click', () => {
        const blob = new Blob(recordedBlobs, {type: 'video/webm'});
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'test.webm';
        document.body.appendChild(a);
        a.click();
        setTimeout(() => {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 100);
        });

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
        playButton.disabled = true;
        downloadButton.disabled = true;
        mediaRecorder.ondataavailable = handleDataAvailable;
        mediaRecorder.start();
        setTimeout(function(){
            stopRecording()
            }, vidLength); 
        }

        function stopRecording() {
        mediaRecorder.stop();
        recordButton.textContent = 'Start Recording';
        playButton.disabled = false;
        downloadButton.disabled = false;
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
                setTimeout(
                    takePhoto()
                    , 5000);
                }
                if (text == "peace"){
                takePhoto();
                }
                if (text == "thumbs_up"){
                startRecording(vidLength);
                }
                //else do nothing
            });
        }

        
        function updateServer(){
            takePhoto();
            canvas.toBlob(function(blob){
                    var image = blob;
                    // ************ DISPLAY BLOB
                    
                    myImage.src = URL.createObjectURL(blob);
                    
                    // emit blob 
                    vm.$emit('caputure-image', blob);

                    postData(post_url, image)
                }, 'image/jpeg', 0.95)
        }


        // Take and send photo every x seconds
        window.setInterval(updateServer, 5000);

    }
}
</script>

<style scoped>

</style>