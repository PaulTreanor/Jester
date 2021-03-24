<template>
	<div>
		<p>This is gallery tab</p>
		<img v-bind:src='image_src' id="image"/>
		
	</div>
</template>

<script>
export default {
	name: "Gallery",
	props: ['photo'],
	data () {
		return {
			image_src : URL.createObjectURL(this.photo)
		}
	},
	
	mounted() {

		//blob will be props 

		//DISPLAY IMAGE TAKEN 
		//var myImage = document.querySelector('img#image');
		//myImage.src = URL.createObjectURL(this.photo);
		//console.log(this.photo);

		// look at App.vue data for photo blobs (will reload each time gallery is opened, so it's fine)
		// display them 
	}
	
   
}
</script>

<style scoped>

</style>
