<template>
    <div>
        <video id="recorded" playsinline loop></video>
        <b-button class="mb-2" id="download" block variant="primary">Download</b-button>
    </div>
</template>

<script>
export default {
    name: "Video", 
    props: ['video'],
    mounted() {
		const downloadButton = document.querySelector('button#download');
		let recordedBlobs = this.video;
		const recordedVideo = document.querySelector('video#recorded');
		
        // Play video
        const superBuffer = new Blob(recordedBlobs, {type: 'video/webm'});
        recordedVideo.src = window.URL.createObjectURL(superBuffer);
        recordedVideo.controls = true;        

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
    #recorded {
        width: 100%;
        height: auto;
        max-width: 640px;
    }

    #download {
        max-width: 640px;
    }
</style>