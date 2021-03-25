<template>
	<div>
		<p>This is gallery tab</p>
		<img v-bind:src='image_src' id="image"/>
		<video id="recorded" playsinline loop></video>
		<button id="play" >Play</button>
		<button id="download">Download</button>
	</div>
</template>

<script>
export default {
	name: "Gallery",
	props: ['photo', 'video'],
	data () {
		return {
			image_src : URL.createObjectURL(this.photo)
		}
	},
	mounted() {
		const downloadButton = document.querySelector('button#download');
		let recordedBlobs = this.video;
		const recordedVideo = document.querySelector('video#recorded');
		const playButton = document.querySelector('button#play');

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
	}
	
}
</script>

<style scoped>

</style>
