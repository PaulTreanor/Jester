<template>

    <div>
        <b-navbar toggleable="lg" type="dark" variant="success">
            <b-navbar-brand href="#" v-on:click="$emit('active-view', 1)">
                <h2 class="brand">Jester</h2>
            </b-navbar-brand>
            <!----nav collapse btn --->
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            

            <!---nav items could be disabled when you're in that specific section --->
            <!--- text is just placeholder for icons _---->
            
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item v-on:click="$emit('active-view', 1)">
                        <p class="h2 mb-1" v-bind:class="{'is-active':activeView ===1}" v-b-tooltip.hover title="Camera" > <b-icon icon="camera"></b-icon></p>
                    </b-nav-item>
                    <b-nav-item v-on:click="$emit('active-view', 3)">
                        <p class="h2 mb-1" v-bind:class="{'is-active':activeView ===3}" v-b-tooltip.hover title="Gallery"> <b-icon icon="card-image"></b-icon></p>
                    </b-nav-item>
                    <b-nav-item v-on:click="$emit('active-view', 2)">
                        <p class="h4 mb-1" v-bind:class="{'is-active':activeView ===2}" v-b-tooltip.hover title="Information"> <b-icon icon="info-square" shift-v="-3"></b-icon></p>
                    </b-nav-item>
                </b-navbar-nav>
            </b-collapse>
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
    
    .brand {
        color:white;
    }

    

    .bg-success {
    background-color: purple !important;
    }

   
</style>