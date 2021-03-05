let mediaRecorder;
let recordedBlobs;
let vidLength = 5000;

var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

const errorMsgElement = document.querySelector('span#errorMsg');
const recordedVideo = document.querySelector('video#recorded');
const recordButton = document.querySelector('button#record');
const snapButton = document.querySelector('button#snap');
const preview = document.querySelector('video#preview');
const playButton = document.querySelector('button#play');
const downloadButton = document.querySelector('button#download');

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
  a.download = 'video.webm';
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  }, 100);
});


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

// Access camera 
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  // {audo: true} to get audio
  navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
    recordButton.disabled = false;
    window.stream = stream;
    // Play video stream in preview box
    preview.srcObject = stream;
  });
}

var intervalID = window.setInterval(takePhoto, 5000);



