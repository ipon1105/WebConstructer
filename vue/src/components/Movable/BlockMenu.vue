<template>
    <div class="widjetsMenu">
        <div>
            <p>Размер шрифта: {{fontSize}}</p>

            <el-slider class="slider" v-model="fontSize"
                        @change="changeFontSize"/>
        </div>
        <div>
            <p>Стиль шрифта</p>
            <el-cascader v-model="valueCascader" 
                        :options="optionsCascader" 
                        @change="changeFontFamily" 
                        style="width: 70%; margin-bottom: 10%;" />
        </div>

        <div>
            <p style="margin-right: 5%;">Цвет текста :</p>
            <el-color-picker v-model="colorPic" show-alpha :predefine="predefineColors" 
                                @active-change="(changeColorText)"/>
        </div>

        <div>
        <p style="margin-right: 5%;">Цвет фона :</p>
            <el-color-picker v-model="backgroudColorPic" show-alpha :predefine="predefineColors" 
                                @active-change="(changeColorBackground)"/>
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
            fontFamily: 'Impact',
            x: 0,
            y: 0,
            colorPic: 'rgba(0, 0, 0, 1)',
            backgroudColorPic: 'rgba(255, 255, 255, 1)',
            predefineColors: [
            '#ff4500',
            '#ff8c00',
            '#ffd700',
            '#90ee90',
            '#00ced1',
            '#1e90ff',
            '#c71585',
            'rgba(255, 69, 0, 0.68)',
            'rgb(255, 120, 0)',
            'hsv(51, 100, 98)',
            'hsva(120, 40, 94, 0.5)',
            'hsl(181, 100%, 37%)',
            'hsla(209, 100%, 56%, 0.73)',
            '#c7158577',
            ],
            valueCascader: [],
            optionsCascader: [{
                    value: 'Times New Roman',
                    label: 'Times New Roman'
                },
                {
                    value: 'Georgia',
                    label: 'Georgia'
                },
                {
                    value: 'Arial',
                    label: 'Arial'
                },
                {
                    value: 'Comic Sans MS',
                    label: 'Comic Sans MS'
                },
                {
                    value: 'Impact',
                    label: 'Impact'
                },
                {
                    value: 'Tahoma',
                    label: 'Tahoma'
                },
            ]
        }),
        mounted () {
        },
        methods: {
            changeSize (data) {
                this.$emit('changeSize', data)
            },
            changePos (data) {
                this.$emit('changePos', data)
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
            changeColorBackground(newValue){
                this.changeStyle ({
                    backgroundColor: newValue
                })
            },
            changeFontSize(newValue) {
                this.changeStyle({
                    fontSize: newValue + 'px'
                })
            },
            changeFontFamily(newValue){
                this.changeStyle({
                    fontFamily: newValue
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
            x(newValue){
                this.changePos({
                    x: newValue
                })
            },
            y(newValue){
                this.changePos({
                    y: newValue
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

   .slider{
        width: 70%;
        
   }

</style>