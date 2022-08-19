<template>
    <div class="widjetsMenu">
        <p>Размер шрифта: {{fontSize}}</p>

        <input type="range" min="1" max="100"
                v-model="fontSize"
                @change="changeFontSize($event)"/>

        <div class="palitra">
            <div 
                v-for="color in colorBase"
                @click="changeColorText(color)" 
                :key="color"
                class="palitraElement"
                :id="color"
                :style="{ 'background-color': color}">
            </div>
        </div>

        <div>
            <div>
                <div>
                    <p>Ширина : </p>
                    <input type="input" v-model="width"/>
                </div>
                <div>
                    <p>Высота : </p>
                    <input type="input" v-model="height"/>
                </div>
                <div>
                    <p>X : </p>
                    <input type="input" v-model="x"/>
                </div>
                <div>
                    <p>Y : </p>
                    <input type="input" v-model="y"/>
                </div>
            </div>
        </div>
        
        <button @click="deleteElement">Удалить</button>

        
    </div>
</template>

<script>
    export default {
        props: {
            size: {
                default: () => ({})
            },
            pos: {
                default: () => ({})
            },
            styles: {
                default: () => ({})
            },
        },
        data: () => ({
            width: 0,
            height: 0,
            fontSize: 12,
            x: 0,
            y: 0,
            colorBase: ['#FFFFFF', '#000000', '#808080', '#C0C0C0', '#FF00FF', 
                            '#800080', '#000080', '#FF0000', '#FFFF00', '#808000',
                            '#00FF00', '#008000', '#0000FF', '#FF4500', '#8B0000'],
        }),
        mounted () {
        },
        methods: {
            changeSize (data) {
                this.$emit('changeSize', data)
            },
            deleteElement () {
                this.$emit('deleteElement', this.id)
            },
            changeStyle (data) {
                this.$emit('changeStyle', data)
            },
            changeColorText (newValue) {
                this.changeStyle ({
                    color: newValue
                })
            },
            changeFontSize(event) {
                this.changeStyle({
                    fontSize: event.target.value + 'px'
                })
            },
            processWidth () {
                
            }
        },
        watch: {
            width (newValue) {
                this.changeSize({
                    width: newValue
                })
            },
            height (newValue) {
                this.changeSize({
                    height: newValue
                })
            },
            fontSize (newValue) {
                this.changeStyle({
                    fontSize: newValue
                })
            },
            pos: {
                handler (newValue) {
                    this.x = newValue.x
                    this.y = newValue.y
                }, 
                deep: true
            },
            styles: {
                handler (newValue) {
                    this.fontSize = newValue.fontSize
                }, 
                deep: true
            },
            size: {
                handler (newValue) {
                    this.width = newValue.width
                    this.height = newValue.height
                }, 
                deep: true
            },
        },
    }
</script>

<style scoped>
    .widjetsMenu{
        width:95%;
        padding-left: 5%;
    }

    p{
        font-size: 0.9em;
        font-family:Verdana, Geneva, Tahoma, sans-serif;
        color: #D4E6ED;
        margin-top: 10%;
        display: inline-block;
    }

    .palitra{
        margin-top: 10%;
        width: 90%;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }

    .palitraElement{
        padding: 6%;
        margin: 3%;
        border-radius: 50%;
    }

    input[type=input]{
        width: 20%;
        border: 1px solid #2A4164; 
        background-color: #2d4554;
        color: #FFFFFF;
        border-radius: 5%;
        display: inline-block;
    }

    button{
        margin-top: 10%;
        background-color: #177ab3;
        border: 2px solid #FFFFFF ;
        color: #FFFFFF;
        border-radius: 4%;
        padding: 3%;
        font-family:Verdana, Geneva, Tahoma, sans-serif;
    }

    button:hover{
        background-color: #2e80b0;
        color: #185578;
    }

    input[type=range] {
    -webkit-appearance: none; /* Скрывает слайдер, чтобы можно было создать свой */
    width: 50%; /* Указание параметра ширины требуется для Firefox. */
    }
    
    input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    }
    
    input[type=range]:focus {
    outline: none; /* Убирает голубую границу у элемента. Хотя, возможно, и стоит создавать некоторое оформления для состояния фокуса в целях обеспечения доступности. */
    }
    
    input[type=range]::-ms-track {
    width: 100%;
    cursor: pointer;
    background: transparent; /* Скрывает слайдер, чтобы можно было добавить собственные стили. */
    border-color: transparent;
    color: transparent;
    }

    input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    border: 1px solid #134969;
    height: 15px;
    width: 16px;
    border-radius: 50%;
    background: #2796d6;
    cursor: pointer;
    margin-top: -5px; 
    margin-bottom: -5px;

    }
</style>