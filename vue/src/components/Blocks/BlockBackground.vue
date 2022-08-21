<template>
<div 
    class="bg"
    :style="style"
>
</div>   
</template>

<script>

export default {
    computed: {
        style () {
            return {
                backgroundSize: this.$store.getters.getGridSize + 'px ' +  this.$store.getters.getGridSize + 'px',
                // backgroundImage: 'repeating-linear-gradient(0deg, #000, #000 1px, transparent 1px, transparent ' + this.$store.getters.getGridSize + 'px),repeating-linear-gradient(-90deg, #000, #000 1px, transparent 1px, transparent ' + this.$store.getters.getGridSize + 'px)'
            }
        },

    },
}
</script>

<style>
.bg {
    height: 100%;
    width: 100%;
    opacity: 0.15;
    z-index: 0;
}
</style>