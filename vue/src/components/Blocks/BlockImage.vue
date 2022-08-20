<template>
<BlockMovable>
    <input v-if="isInput" type="file" @change="onFileChange($event)" class="imgFill" /> 
    <img :src="imageSrc" class="image">
</BlockMovable>

</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default
{
    components: { BlockMovable },
        data: () => ({
            imageSrc: '',
            isInput: true,
        }),
    
    methods: {
        onFileChange(event){
            this.imageSrc = URL.createObjectURL(event.target.files[0])
            this.isInput = false
        }
    }

}

</script>

<style scoped>
.imgFill
{
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: fill;
}

.image
{
    width: 100%;
    height: 100%;
    object-fit: fill;
}
</style>