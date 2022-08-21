<template>
    <BlockMovable @changeButton="changeButton" @change-styles="changeStyles">
        <el-button class="btn" :style="styles"> Default</el-button>
    </BlockMovable>
</template>

<script>
import BlockMovable from '@/components/Movable/BlockMovable.vue'

export default
{
  components: { BlockMovable },
  data (){
    return {
        styles: {
            default: () => ({})
        },
    }
  },
  methods: {
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
  }
}
</script>

<style>
    .btn{
        width: 100%;
        height: 100%;
    }
</style>