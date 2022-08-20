<template>
<<<<<<< HEAD
    <BlockMovable @change-styles="changeStyles">
        <textarea :style="styles" v-model="value">
=======
    <BlockMovable
        @change-styles="changeStyles"
        :innerSelection="isSelected"
    >
        <textarea
            :style="styles"
            v-model="value"
            @focus="onFocus"
            @blur="onBlur"
        >

>>>>>>> 816ac6bfc1de4c860a17633d6e92ba167bda4632
        </textarea>
    </BlockMovable>
</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default {
    components: {
        BlockMovable
    },
    data: () => ({
        value: 'Sample',
        styles: {
            default: () => ({})
        },
        isSelected: false,
    }),
    methods :{
        changeStyles(data){
            console.log('blockText: ', data)
            this.styles.color = data.color
            this.styles.backgroundColor = data.backgroundColor
            this.styles.fontSize = data.fontSize
            this.styles.fontFamily = data.fontFamily
            this.styles.borderRadius = data.borderRadius
            this.styles.zIndex = data.zIndex
            this.styles.textAlign = data.textAlign
        },
        onFocus () {
            this.isSelected = true
        },
        onBlur () {
            this.isSelected = false
        },
    }
}
</script>

<style>

    textarea{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
        outline: none;
        resize: none;
        z-index: 2;
        padding: 0;
        overflow: hidden;
        /* border: 1px solid rgba(255, 255, 255, 0); */
    }
</style>