<template>
<BlockMovable>
    <div class="text-content">{{value}}</div>
</BlockMovable>
</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default {
    components: {
        BlockMovable
    },
    data: () => ({
        value: 'bebra'
    }),
}
</script>

<style>
.text-content{
    overflow: hidden;
}
</style>