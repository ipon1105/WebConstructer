<template>
<div class="buttonWrapper">
    <div 
        class="buttonContainer"
        @click="addEll(widget)"
        v-for="widget in getMenuData"
        :key="widget"
    >
        <img :src="require('@/assets/image/icon' + widget.name + (widget.ext ?? '.png'))">
        <p>{{ widget.title }}</p>
    </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default{
    name: 'WidjetsMenu',

    methods: {
        addEll(widget){
            this.$emit('addBlock', widget)
        }
    },
    computed: mapGetters(['getMenuData']),
}
</script>

<style scoped>

.buttonContainer{
    width: 100%;
    background-color: #263845;
    text-align: center;
    flex: 1 1;
}

.buttonContainer:hover{
    background-color: #49677C;
}

.buttonWrapper {
    display: flex;
    flex-direction: column;
    min-height: 100%;
}

p{
    color: #D4E6ED;
    font-family: Arial, Helvetica, sans-serif;
    src: local('Extra light italic'),
    url(@/assets/Exo_2_Extra_Light.ttf); 
    font-size: 0.8em;
    margin-top: 8%;
    margin-bottom: 0; 
}

img{
    margin-top: 10%;
}

</style>