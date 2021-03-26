
<template>
    <main>
        <b-container class="info-col">
            <h3 class="pt-2">Info</h3>
            <p>Jester allows users to take photos and record videos without needing to touch their device.</p>
            <p>Jester works on all devices with a camera and a modern internet browser.</p>
            <hr>
            <h4>Taking Photos</h4>
            <img src="../assets/logo.png">
            <p>Making a peace sign gesture triggers a photo to be taken. The gallery can hold up to 5 photos.</p>
            <hr>
            <h4>Recording Videos</h4>
            <img src="../assets/logo.png">
            <img src="../assets/logo.png">
            
            <p>A thumbs up gestures triggers video recording.</p>
            <p>Recording continues until the user makes a stop gesture with their flattened palm facing the devices camera (imagine the hand gesture a police officer would use to stop traffice).</p>
            <p>The gallery can store 1 video at a time. </p>
            <hr>
            <h4>Making the most of Jester</h4>
            <ol class="pl-3">
                <li>Keep elbows in frame.</li>
                <li>Use app in good lighting.</li>
                <li>Use a modern internet browser.</li>
                <li>Use right hand to make gestures.</li>
            </ol>
        </b-container>
    </main>
</template>

<script>
export default {
    name: "Info",
    props: ["active_view"]
}
</script>

<style scoped>
    .info-col {
        max-width: 600px;
    }
</style>
