<template>

    <div>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">Jester</b-navbar-brand>

            <!---nav items could be disabled when you're in that specific section --->
            <!--- text is just placeholder for icons _---->
            <b-navbar-nav class="ml-auto">
                <b-nav-item v-on:click="$emit('active-view', 1)">
                    <p class="h2 mb-2" v-bind:class="{'is-active':activeView ===1}" > <b-icon icon="camera"></b-icon></p>
                </b-nav-item>
                <b-nav-item v-on:click="$emit('active-view', 3)">
                    <p class="h2 mb-2" v-bind:class="{'is-active':activeView ===3}"> <b-icon icon="card-image"></b-icon></p>
                </b-nav-item>
                <b-nav-item v-on:click="$emit('active-view', 2)">
                    <p class="h4 mb-2" v-bind:class="{'is-active':activeView ===2}"> <b-icon icon="info-square" shift-v="-2"></b-icon></p>
                </b-nav-item>
            </b-navbar-nav>

        </b-navbar>
    </div>
</template>

<script>
export default {
    name: "Nav",
    props: ["active-view"],
    
}
</script>

<style scoped>
    .is-active {
        color: white;
    }
</style>