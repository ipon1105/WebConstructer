<template>
    <div>
        <Movable 
            :id="id"
            :parent-id="parentId"
            :selected="isSelected"
            :style-data="styleData"
            @changeObject="handleBlockChange"
            @object-selected="objectSelection"
            @deleteElement="deleteElement"
        >
            <slot></slot>
        </Movable>
        <div v-if="id == selectedObjectId">
            <Teleport to="#optionsMenu">
                {{ selectedObjectId }}
                <BlockMenu
                    :parent-id="parentId"
                    :style-data="styleData"
                    @deleteElement="deleteElement"
                    @changeObject="handleBlockChange"
                ></BlockMenu>
            </Teleport>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Movable from '@/components/Movable/Movable.vue'
import BlockMenu from '@/components/Movable/BlockMenu.vue'

export default {
    components: {
        Movable,
        BlockMenu,
    },
    props: {
        id: {
            type: Number
        },
        selectedObjectId: {
            type: Number
        },
        innerSelection: {
            type: Boolean
        },
        parentId: {
            type: Number
        },
    },
    computed: mapGetters (['getBlockMenuDataById']),

    data: () => ({
        styleData: {},
        isSelected: false,
    }),

    created () {
        if (!this.getBlockMenuDataById[this.parentId]) {
            return
        }
        for (let field of this.getBlockMenuDataById[this.parentId]) {
            this.styleData[field.field] = field.defaultValue
        }
    },

    methods: {
        objectSelection () {
            this.$emit('objectSelection', this.id);
        },
        handleBlockChange (value, field) {
            this.styleData[field] = value
            this.$emit('changeStyles', value, field, this.getBlockMenuDataById[this.parentId].find((el) => el.field == field).measure)
        },
        deleteElement () {
            this.$emit('deleteElement', this.id)
        },
    },

    watch: {
        innerSelection (newValue) {
            this.isSelected = newValue
        },
        isSelected (newValue) {
            if (newValue) {
                this.objectSelection()
            }
        }
    },
}
</script>

<style>
</style>