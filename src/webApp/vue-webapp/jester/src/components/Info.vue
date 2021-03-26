
<template>
    <main>
        <b-container>
            <h1>Info</h1>
            <p>Jester allows users to take photos and record videos without needing to touch their device.</p>
            <p>It works on any device that has a camera and uses a modern web browser (*****Firefox, Chrome, and Edge****). </p>
            <h3>Taking Photos</h3>
            <img src="../assets/logo.png">
            <p>Jester takes photos when it recognises the peace sign hand gesture. This snapshot is stored in the gallery which can hold up to 5 photos. </p>
            <h3>Recording Videos</h3>
            <img src="../assets/logo.png">
            <img src="../assets/logo.png">
            <p>Jester begins video recording when it detects that the user is making a thumbs up gesture. Video recording continues until the user makes a gesture with their flattened palm facing the devices camera (imagine the hand gesture a police officer would use to stop traffice).</p>
            <p>The video is stored in the gallery, which can hold 1 video at a time. </p>
            <h3>Making the most of Jester</h3>
            <ol>
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

</style>
