<template>
  <div
    class="all"
    :style="windowStyle"
  > 
    <!-- Меню с кнопками -->
    <el-container>
      <el-aside :width="menuWidth">
        <div class="menu">
          <WidgetsMenu @add-block="addBlock"></WidgetsMenu>
        </div>
      </el-aside>
    <!-- Общее поле, где можно перемещать элементы -->
      <el-main>
        <div
          class="container"
        >
        <!-- Блок с текстом -->
          <component
            v-for="item in items"
            :key="item.id"
            :is="item.name"
            :id="item.id"
            :parent-id="item.parentBlockId"
            :selected-object-id="selectedObjectId"
            @object-selection="objectSelection"
            @delete-element="deleteBlock"
          ></component>
        </div>
      </el-main>
      <el-aside :width="menuWidth">
        <div class="objectMenu" id="optionsMenu">
        </div>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import BlockText from '@/components/Blocks/BlockText.vue'
import BlockFigure from '@/components/Blocks/BlockFigure.vue'
import BlockBackground from '@/components/Blocks/BlockBackground.vue'
import BlockImage from '@/components/Blocks/BlockImage.vue'
import BlockSlider from '@/components/Blocks/BlockSlider.vue'
import BlockForm from '@/components/Blocks/BlockForm.vue'
import BlockButton from '@/components/Blocks/BlockButton.vue'
import WidgetsMenu from '@/components/Menu/WidgetsMenu.vue'

export default {
  name: 'App',
  components: {
    BlockText,
    WidgetsMenu,
    BlockFigure,
    BlockBackground,
    BlockImage,
    BlockSlider,
    BlockForm,
    BlockButton,
  },
  data (){
    return{
      items: [],
      selectedObjectId: 0,
      backgroundId: 0,
    }
  },
  computed: {
    ...mapGetters(['getMenuData', 'getMenuWidth']),
    windowStyle () {
      return {
        minHeight: window.innerHeight + 'px'
      }
    },
    menuWidth () {
      return this.getMenuWidth + '%'
    }
  },

  mounted () {
    for (let widget of this.getMenuData) {
      if (widget.single) {
        this.addBlock(widget)
      }
    }
  },

  methods: {
    addBlock (block) {
      if (block.single && this.items.find((el) => 'Block' + block.name == el.name)) {
        this.selectedObjectId = this.items.find((el) => block.name == el.name).id
        return
      }
      this.items.push({
        id: this.items.length,
        name: 'Block' + block.name,
        parentBlockId: block.id,
      })
      if (block.name == 'Background') {
        this.backgroundId = this.items.length - 1
      }
    },
    objectSelection (id) {
      this.selectedObjectId = id
    },
    deleteBlock (id) {
      this.items.splice(id, 1)
      this.selectedObjectId = this.backgroundId
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
}

* {
  margin: 0;
  padding: 0;
}

.container {
  background-color: #FFFFFF;
  width: 100%;
  height: 100%;
  padding: 0;
}

.el-main {
  padding: 0 !important;
}

.all{
  display: flex;
  justify-content: space-between;
}

body{
  margin: 0;
  padding: 0;
}

.objectMenu{
  background-color: #1C2A33;
  width: 100%;
  height: 100%;
}

.menu{
  background-color: #1C2A33;
  margin: 0;
  width: 100%;
  height: 100%;
}
</style>
