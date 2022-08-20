<template>
	<BlockMovable>
        <img :src="require('@/assets/image/iconSlider.png')" alt="" draggable="false" >
    </BlockMovable>
</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default
{
    components: { BlockMovable },
}

</script>

<style scoped>
img
{
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: fill;
}
</style>