<template>
    <div>
        <b-img class="pb-3" v-bind:src='image_src' id="image" fluid ></b-img>
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