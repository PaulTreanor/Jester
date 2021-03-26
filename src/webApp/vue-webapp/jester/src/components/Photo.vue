<template>
    <div>
        <p>This is a photo component</p>
        <b-img v-bind:src='image_src' id="image" fluid ></b-img>
    </div>
</template>

<script>
export default {
    name: "Photo", 
    props: ['photo'],
    data () {
		return {
			image_src : URL.createObjectURL(this.photo)
		}
	}
}
</script>