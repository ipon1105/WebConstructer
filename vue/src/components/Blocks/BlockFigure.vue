<template>
<BlockMovable>
  <div class="square"
  @click="addSquare">      
  </div>
</BlockMovable>
</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default
{
  components: { BlockMovable }
}

</script>

<style scoped> 
.square{
  object-fit: fill;
  height:100px;
  width:100px;
  text-align: center;
  vertical-align: center;
  margin-right:10px;
  }
</style>