<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">Jester</b-navbar-brand>

        
            <!---nav items could be disabled when you're in that specific section --->
            <!--- text is just placeholder for icons _---->
            <b-navbar-nav class="ml-auto">
                <b-nav-item v-on:click="$emit('active-view', 1)">Camera</b-nav-item>
                <b-nav-item v-on:click="$emit('active-view', 2)">Gallery</b-nav-item>
                <b-nav-item v-on:click="$emit('active-view', 3)">Info</b-nav-item>
            </b-navbar-nav>

        </b-navbar>
    </div>
</template>

<script>
export default {
    name: "Nav",

   
}
</script>

<style scoped>

</style>