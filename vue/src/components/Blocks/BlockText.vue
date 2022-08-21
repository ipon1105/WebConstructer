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
import { mapGetters } from 'vuex'
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default {
    components: {
        BlockMovable
    },
    data: () => ({
        value: 'Sample',
        styles: {
            'color': '',
            'background-color': '',
            'font-size': '',
            'font-family': '',
            'border-radius': '',
            'z-index': '',
            'text-align': ''
        },
        isSelected: false,
    }),
    computed: mapGetters(['getBlockMenuDataById']),
    methods :{
        changeStyles(value, field, measure){
            if (typeof this.styles[field] !== 'undefined') {
                this.styles[field] = value + (measure && measure != 'none' ? measure : '')
            }
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

<style scoped>

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