<template>
  
<BlockMovable
  @change-size="changeSize"
>
  <input type="file" @change="onFileChange($event)" class="imgFill" />
  <button style="margin-top:10%" class="buttonDelete" @click="imageDelete">Удалить</button>
	<div class="obj-fit">
    <el-carousel :height="formattedHeight">
      <el-carousel-item v-for="item in images" :key="item">
        <img :src="item" class="image">   
      </el-carousel-item>
    </el-carousel>
  </div>
</BlockMovable>
</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default {
	components: { BlockMovable },
  data: () => ({
    height: 150,
    defaultHeight: 150,
    images: [],
  }),
	methods:
	{
		changeSize(data) {
      this.height = data.height ?? this.defaultHeight
    },
    onFileChange(event) {
      this.images.push(URL.createObjectURL(event.target.files[0]))
      // this.isInput = false
    },
    imageDelete(){
      this.images.pop()
    }
	},
  computed: {
    formattedHeight () {
      return this.height + 'px'
    }
  }
}
</script>

<style scoped>

.obj-fit { object-fit: fill; height: 80%; margin-top: 20%;}

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

.imgFill
{
    position: absolute;
    width: 50%;
    height: 10%;
    object-fit: fill;
}
.image
{
    width: 100%;
    height: 100%;
    object-fit: fill;
}

</style>