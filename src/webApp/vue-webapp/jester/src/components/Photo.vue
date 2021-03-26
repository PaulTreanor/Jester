<template>
    <div>
        <p>This is a photo component</p>
        <img v-bind:src='image_src' id="image"/>
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