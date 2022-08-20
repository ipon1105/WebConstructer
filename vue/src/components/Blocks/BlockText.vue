<template>
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
            this.styles.color = data.color
            this.styles.backgroundColor = data.backgroundColor
            this.styles.fontSize = data.fontSize
            this.styles.fontFamily = data.fontFamily
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
    }
</style>