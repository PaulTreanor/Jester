let mediaRecorder;
let recordedBlobs;
let vidLength = 20000;

const recordedVideo = document.querySelector('video#recorded');
const recordButton = document.querySelector('button#record');
const preview = document.querySelector('video#preview');
const playButton = document.querySelector('button#play');
const downloadButton = document.querySelector('button#download');

var controls = document.getElementById('controls');
const pauseButton = document.querySelector('button#pause');
const resumeButton = document.querySelector('button#resume');

var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
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

// Pause/Result Video 
pauseButton.addEventListener('click', () => {
  pauseMedia();
});

// Pause/Result Video 
resumeButton.addEventListener('click', () => {
  resumeMedia();
});


playButton.addEventListener('click', () => {
  playVideo();
});

function playVideo() {
  const superBuffer = new Blob(recordedBlobs, {type: 'video/webm'});
  recordedVideo.src = window.URL.createObjectURL(superBuffer);
  recordedVideo.controls = true;
  recordedVideo.play();
}

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

function startRecording() {
  recordedBlobs = [];
  mediaRecorder = new MediaRecorder(window.stream, {mimeType: 'video/webm'});
  recordButton.textContent = 'Stop Recording';
  playButton.disabled = true;
  downloadButton.disabled = true;
  mediaRecorder.ondataavailable = handleDataAvailable;
  mediaRecorder.start();
  setTimeout(function(){
      checkVideoStop();


  }, vidLength);  
}

function stopRecording() {
  mediaRecorder.stop();
  recordButton.textContent = 'Start Recording';
  playButton.disabled = false;
  downloadButton.disabled = false;
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




// -------------- API STUFF --------------//


function takePhoto(){
     context.drawImage(preview, 0, 0, 640, 480);
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
            postData(post_url, image)
        }, 'image/jpeg', 0.95)
}
// Take and send photo every x seconds
window.setInterval(updateServer, 20000);






// --------------- MAIN ---------------------//

// Access camera and display preview at id='preview'
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  // {audo: true} to get audio
  navigator.mediaDevices.getUserMedia({ video: true, audio: true }).then(function(stream) {
    recordButton.disabled = false;
    window.stream = stream;
    // Play video stream in preview box
    preview.srcObject = stream;
  });
}




