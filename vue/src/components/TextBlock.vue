<template>
    <MovableBlock>
        <input type="input" v-model="value"/>
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

</style>