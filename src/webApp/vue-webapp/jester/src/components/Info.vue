
<template>
    <main>
        <b-container class="info-col">

            <h4>What is Jester?</h4>
            <p >Use hand gestures to take photos and videos with ease!</p>
            
            <h4>Taking Photos</h4>
            <div class="alert d-inline-flex">
                <b-icon class="h3" icon="hand-thumbs-up"></b-icon>
                <p>A peace sign gesture takes a photo.</p>
            </div>
            
            <h4>Recording Videos</h4>
            <div class="alert d-inline-flex">
                <b-icon class="h3" icon="hand-thumbs-up"></b-icon>
                <p>A thumbs up gestures starts video recording.</p>
            </div>
            
            <div class="alert d-inline-flex">
                <b-icon class="h3" icon="hand-thumbs-up"></b-icon>
                <p>A flat palm facing the camera stops the recording</p>
            </div>
            

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

    p {
        padding:0px;
        margin: 0px;
        padding-top: 5px;
    }

    h4 {
        padding-top: 25px;
        padding-bottom: 5px;
        color: purple;
    }

    .alert {
        background: #FFFFFF;
        border: 1px solid rgba(214, 214, 214, 0.15);
        box-sizing: border-box;
        box-shadow: 0px 4px 8px rgba(56, 56, 56, 0.15);
        border-radius: 16px;
        color: #2c3e50;
        max-width: 500px;
    }

    .b-icon {
        margin-right: 20px;
    }
</style>
