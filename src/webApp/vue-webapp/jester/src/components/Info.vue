
<template>
    <main>
        <b-container class="info-col">
            <h3 class="pt-2">Info</h3>
            <p>Jester allows users to take photos and record videos without needing to touch their device.</p>
            <p>It works on any device that has a camera and uses Firefox, Chrome, and Edge. </p>
            <hr>
            <h4>Taking Photos</h4>
            <img src="../assets/logo.png">
            <p>Jester takes photos when it recognises the peace sign hand gesture. This snapshot is stored in the gallery which can hold up to 5 photos. </p>
            <hr>
            <h4>Recording Videos</h4>
            <img src="../assets/logo.png">
            <img src="../assets/logo.png">
            
            <p>Jester begins video recording when it detects that the user is making a thumbs up gesture. Video recording continues until the user makes a gesture with their flattened palm facing the devices camera (imagine the hand gesture a police officer would use to stop traffice).</p>
            <p>The video is stored in the gallery, which can hold 1 video at a time. </p>
            <hr>
            <h4>Making the most of Jester</h4>
            <ol class="pl-3">
                <li>Keep elbows in frame.</li>
                <li>Have good lighting.</li>
                <li>Use a modern internet browser.</li>
                <li>Gestures must be made with the users right hand.</li>
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
