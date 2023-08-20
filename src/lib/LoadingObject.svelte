<script lang="ts">

</script>


<div id="loader" class="p-base-item" >
</div>


<style lang="css">
#loader {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    border: 12px solid #f3f3f3de;
    border-radius: 50%;
    border-top: 12px solid #004c23;
    width: 70px;
    height: 70px;
    animation: spin 1s linear infinite;
}

@keyframes spin{
    100%{
        transform: rotate(360deg);
    }
}
</style>