<template>
<BlockMovable>
    <input type="file" @change="onFileChange" class="imgFill" /> 
</BlockMovable>

</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default
{
    components: { BlockMovable },
    // data: () => ({
    // image: ''
    // }),
    // methods: {
    //     onFileChange(e) {
    //       var files = e.target.files || e.dataTransfer.files;
    //       if (!files.length)
    //         return;
    //       this.createImage(files[0]);
    //     },
    //     createImage(file) {
    //       var image = new Image();
    //       var reader = new FileReader();
    //       var vm = this;

    //       reader.onload = (e) => {
    //         vm.image = e.target.result;
    //       };
    //       reader.readAsDataURL(file);
    //     },
    //     removeImage: function (e) {
    //       this.image = '';
    //     }
    // }

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
</style>