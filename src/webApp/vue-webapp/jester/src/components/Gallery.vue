<template>
	<div>
		<h1>Gallery</h1>
		<div v-bind:key="photo" v-for="photo in photo">
            <Photo v-bind:photo="photo"/>
        </div>
		<div v-bind:key="video" v-for="video in video">
            <Video v-bind:video="video"/>
        </div>
	</div>
</template>

<script>

import Photo from './Photo';
import Video from './Video';

export default {
	name: "Gallery",
	components: {
		Photo,
		Video
	},
	props: ['photo', 'video'],	
}
</script>

<style scoped>

</style>
