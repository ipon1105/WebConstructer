<template>
    <div class="widjetsMenu">
        <p class="widgetsMenuHeader">
            Настройка виджета
        </p>
        <div v-for="field in getBlockMenuDataById[parentId]" :key="field">
            <component
                :is="'BlockMenu' + field.type"
                :title="field.title"
                :additional-data="field.additionalData"
                :val="menuBlockData[field.field]"
                @blockChange="handleBlockChange($event, field.field)"
            >
            </component>
        </div>

        <button class="buttonDelete" @click="deleteElement">Удалить</button>

        
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import BlockMenuInput from '@/components/Menu/Fields/BlockMenuInput.vue';
import BlockMenuCascader from '@/components/Menu/Fields/BlockMenuCascader.vue';
import BlockMenuColorpicker from '@/components/Menu/Fields/BlockMenuColorpicker.vue';
import BlockMenuImgset from '@/components/Menu/Fields/BlockMenuImgset.vue';
import BlockMenuSlider from '@/components/Menu/Fields/BlockMenuSlider.vue';
import BlockMenuCheckbox from '@/components/Menu/Fields/BlockMenuCheckbox.vue';

    export default {
        components: {
            BlockMenuInput,
            BlockMenuCascader,
            BlockMenuColorpicker,
            BlockMenuImgset,
            BlockMenuSlider,
            BlockMenuCheckbox,
        },
        props: {
            stylesValues: {
                default: () => ({})
            },
            parentId: {
                type: Number
            },
            styleData: {
                default: null
            }
        },
        data: () => ({
            menuBlockData: {}
        }),
        mounted () {
            if (this.styleData) {
                this.menuBlockData = this.styleData
                return
            }
            for (let field of this.getBlockMenuDataById[this.parentId]) {
                this.menuBlockData[field.field] = field.defaultValue
            }
        },
        computed: mapGetters (['getBlockMenuDataById']),
        methods: {
            handleBlockChange (value, field) {
                this.menuBlockData[field] = value
                this.$emit('changeObject', value, field)
            }
        },
        watch: {
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
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    color: #DDD;
}

.buttonDelete{
    margin-top: 10%;
    background-color: #177ab3;
    border: 2px solid #FFFFFF ;
    color: #FFFFFF;
    border-radius: 4%;
    padding: 3%;
}

.buttonDelete:hover{
    background-color: #2e80b0;
    color: #185578;
}

.widgetsMenuHeader {
    text-align: center;
    font-size: 20px;
    padding: 0 1rem 1rem 1rem;
}
</style>