<template>
    <BlockMovable @change-styles="changeStyles">
        <textarea :style="styles" v-model="value">

        </textarea>
    </BlockMovable>
</template>

<script>
import BlockMovable from '@/components/BlockMovable.vue'

export default {
    components: {
        BlockMovable
    },
    data: () => ({
        value: 'bebra',
        styles: {
            default: () => ({})
        },
    }),
    methods :{
        changeStyles(data){
            this.styles.color = data.color
            this.styles.backgroundColor = data.backgroundColor
            this.styles.fontSize = data.fontSize
            this.styles.fontFamily = data.fontFamily
        },
    }
}
</script>

<style>
    BlockMovable{
        overflow:hidden;
        outline: none;
    }

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
    }
</style>