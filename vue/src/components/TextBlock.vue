<template>
    <MovableBlock contenteditable>
        <!-- <p contenteditable>{{value}}</p> -->
        {{value}}
    </MovableBlock>
</template>

<script>
import MovableBlock from '@/components/MovableBlock.vue'

export default {
    components: {
        MovableBlock
    },
    data: () => ({
        value: 'bebra'
    }),
}
</script>

<style>
    /* p{
        margin: 0;
    } */
    MovableBlock{
        overflow:hidden;
    }
</style>