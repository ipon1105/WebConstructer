<template>
<BlockMovable>
	<div class="obj-fit">
    <el-carousel :heigth="height">
      <el-carousel-item v-for="item in 5" :key="item">
        <h3>{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>
  </div>
</BlockMovable>
</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default {
	components: { BlockMovable },
	methods:
	{
		
	}
}
</script>

<style scoped>

.obj-fit { object-fit: fill; }

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.95;
  line-height: 150px;
  margin: 0;
  text-align: center;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}
.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

</style>