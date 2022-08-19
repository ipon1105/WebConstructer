<template>
  <div class="all"> 
    <!-- Меню с кнопками -->
    <WidjetsMenu @addText="addText"></WidjetsMenu>
    <!-- Общее поле, где можно перемещать элементы -->
    <div
      class="container"
    >
    <!-- Блок с текстом -->
    <!-- id, xCoord, yCoord это пропсы из TextBlock.vue -->
      <div v-if="items.length > 0">
        <TextBlock
          v-for="item in items"
          :key="item.id"
          :id="item.id"
          :selected-object-id="selectedObjectId"
          @object-selection="objectSelection"
          @delete-element="deleteElement"
        ></TextBlock>
      </div>
    </div>
    <div class="objectMenu" id="optionsMenu">
      
    </div>
  </div>
</template>

<script>

import TextBlock from '@/components/TextBlock.vue'
import WidjetsMenu from '@/components/WidjetsMenu.vue'


export default {
  name: 'App',
  components: {
    TextBlock,
    WidjetsMenu,
  },
  data (){
    return{
      // Массив объектов, где хранятся данные об элементе
      items: [],
      selectedObjectId : 0,
    }
  },
  methods: {
    addText () { // Добавление текстового блока
      this.items.push({ // Запись нового элемента в массив объектов
        id: this.items.length,
        name: null
      })
    },
    objectSelection (id) {
      this.selectedObjectId = id
    },
    deleteElement (id) {
      this.items.splice(id, 1)
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin: 0;
}

.container{
  background-color: #FFFFFF;
  height:800px;
  width: 72%;
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
  background-color: blueviolet;
  width: 20%;
  border: 2px solid black;
}
</style>
