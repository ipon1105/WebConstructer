<template>
<div
    :class="{
        'block': true,
        'block-selected': isElSelected || isDrag,
    }" 
    :style="styleDataFormatted"
    tabindex="0"
    @mousedown="dragMouseDown"
    @mousemove="dragMouseMove"
    @mouseup="dragMouseUp"
    @focus="objectSelection"
    @blur="objectUnselect"
>
    <div v-if="(isElSelected && !isDrag) || isSizeChange">
        <div
            v-for="pointer in sizeChangePointers"
            :key="pointer.direction"
            :class="['pointer', pointer.direction]"
            :style="pointer.style"
            @mousedown="sizeChangeMouseDown($event, pointer.direction)"
            @mouseup="sizeChangeMouseUp"
            @mousemove="sizeChangeMouseMove"
        >
        </div>

        <!-- <div
            class="pointer rotate-pointer"
            :style="rotatePointerStyle"
            @mousedown="rotateMouseDown"
            @mouseup="rotateMouseUp"
            @mousemove="rotateMouseMove"
        >
        </div> -->
    </div>
    <slot></slot>
</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default{
    name: 'MovableBlock',
    props: {
        id: {
            type: Number,
        },
        styleData: {
            default: () => ({})
        },
        selected: {
            type: Boolean
        },
        parentId: {
            type: Number
        }
    },
    data: () => ({
        sizeChangePointers: [],
        // rotatePointerStyle: {},
        pointerSize: 12,
        borderSize: 2,
        directionMap: [
            'nw',
            'n',
            'ne',
            'e',
            'se',
            's',
            'sw',
            'w'
        ],
        styles: {},
        isElSelected: false,
        innerPos: {},
        innerSize: {},
        mouseStartPos: {
            x: 0,
            y: 0
        },
        startSize: {},
        isDrag: false,
        isSizeChange: false,
        isRotate: false,
        prevValue: {
            x: 0,
            y: 0
        },
        curDir: '',
    }),
    mounted () {
        this.styles = this.styleData
        document.documentElement.addEventListener('mouseup', this.dragMouseUp, true)
        document.documentElement.addEventListener('mouseup', this.sizeChangeMouseUp, true)
        document.documentElement.addEventListener('mouseup', this.rotateMouseUp, true)
        document.documentElement.addEventListener('mousemove', this.dragMouseMove, true)
        document.documentElement.addEventListener('mousemove', this.sizeChangeMouseMove, true)
        document.documentElement.addEventListener('mousemove', this.rotateMouseMove, true)
        for (let direction of this.directionMap) {
            let pointer = {}
            pointer.style = {
                top: 'calc(' + (direction.includes('n') ? '0%' : (direction.includes('s') ? '100%' : '50%')) + ' - ' + Math.floor(this.pointerSize / 2 + 1) + 'px)',
                left: 'calc(' + (direction.includes('w') ? '0%' : (direction.includes('e') ? '100%' : '50%')) + ' - ' + Math.floor(this.pointerSize / 2 + 1) + 'px)',
                cursor: direction + '-resize',
                width: this.pointerSize + 'px',
                height: this.pointerSize + 'px',
            }
            pointer.direction = direction
            this.sizeChangePointers.push(pointer)
        }
        this.rotatePointerStyle = {
            width: this.pointerSize + 'px',
            height: this.pointerSize + 'px',
            top: '-2rem',
            left: 'calc(50% - ' + Math.round(this.pointerSize / 2 + 1) + 'px)',
        }
    },
    computed: {
        styleDataFormatted () {
            const formattedStyleData = {
                position: 'absolute'
            }
            if (!this.getBlockMenuDataById[this.parentId]) {
                return
            }
            for (let field of this.getBlockMenuDataById[this.parentId]) {
                formattedStyleData[field.field] = (field.values ? field.values[this.styles[field.field]] : ('' + this.styles[field.field] + (field.measure && field.measure != 'none' ? field.measure : '')))
                if (field.field == 'left') {
                    formattedStyleData[field.field] = 'calc(' + this.getMenuWidth + '% + ' + (field.values ? field.values[this.styles[field.field]] : ('' + this.styles[field.field] + (field.measure && field.measure != 'none' ? field.measure : ''))) + ')'
                }
                if (field.field == 'height') {
                    formattedStyleData[field.field] = (field.values ? field.values[this.styles[field.field]] : (this.styles[field.field] + (field.measure && field.measure != 'none' ? field.measure : '')))
                }
            }
            return formattedStyleData
        },
        gridSize () {
            return this.$store.getters.getGridSize
        },
        ...mapGetters(['getMenuWidth', 'getBlockMenuDataById']),

    },
    methods: {
        dragMouseDown (event) {
            this.mouseStartPos.x = this.innerPos.x - event.clientX
            this.mouseStartPos.y = this.innerPos.y - event.clientY
            this.$emit('stateChange');
            this.isDrag = true
        },
        dragMouseMove (event) {
            if (this.isDrag) {
                this.innerPos.x = (event.clientX + this.mouseStartPos.x) - (event.clientX + this.mouseStartPos.x) % this.gridSize
                this.innerPos.y = (event.clientY + this.mouseStartPos.y) - (event.clientY + this.mouseStartPos.y) % this.gridSize
                const rightBorder = (window.innerWidth - window.innerWidth * this.getMenuWidth * 2 / 100) - this.innerSize.width
                this.innerPos.x = this.innerPos.x < 0 ? 0 : (this.innerPos.x < rightBorder ? this.innerPos.x : rightBorder)
                this.innerPos.y = this.innerPos.y < 0 ? 0 : this.innerPos.y
            }
        },
        dragMouseUp () {
            this.$emit('stateChange')
            this.isDrag = false
        },
        objectSelection () {
            this.isElSelected = true
            this.$emit('objectSelected')
        },
        objectUnselect () {
            this.isElSelected = false
            this.$emit('objectUnselected')
        },
        sizeChangeMouseDown (event, direction) {
            this.isSizeChange = true
            this.curDir = direction
            setTimeout(() => {
                this.isDrag = false
                this.mouseStartPos.x = event.clientX
                this.mouseStartPos.y = event.clientY
                this.startSize.width = this.prevValue.x = this.innerSize.width
                this.startSize.height = this.prevValue.y = this.innerSize.height
            }, 20)
        },
        sizeChangeMouseMove (event) {
            if (this.isSizeChange) {
                if (this.curDir.includes('w') || this.curDir.includes('e')) {
                    let diffX = 0
                    if (this.curDir.includes('w')) {
                        diffX = (this.startSize.width + (event.clientX - this.mouseStartPos.x) * -1) - (this.startSize.width + (event.clientX - this.mouseStartPos.x) * -1) % this.gridSize
                        if (this.innerPos.x > 0) {
                            this.innerPos.x += this.prevValue.x - diffX
                        } else {
                            if (diffX >= this.innerSize.width) {
                                diffX = this.innerSize.width
                            } else {
                                this.innerPos.x += this.prevValue.x - diffX
                            }
                        }
                    } else {
                        diffX = (this.startSize.width + (event.clientX - this.mouseStartPos.x)) - (this.startSize.width + (event.clientX - this.mouseStartPos.x)) % this.gridSize
                        if (diffX > ((window.innerWidth - window.innerWidth * this.getMenuWidth * 2 / 100) - this.innerPos.x)) {
                            diffX = (window.innerWidth - window.innerWidth * this.getMenuWidth * 2 / 100) - this.innerPos.x
                        }
                    }
                    if (diffX >= this.gridSize) {
                        this.innerSize.width = diffX
                    }
                    this.prevValue.x = diffX
                }
                if (this.curDir.includes('n') || this.curDir.includes('s')) {
                    let diffY = 0
                    if (this.curDir.includes('n')) {
                        diffY = (this.startSize.height + (event.clientY - this.mouseStartPos.y) * -1) - (this.startSize.height + (event.clientY - this.mouseStartPos.y) * -1) % this.gridSize
                        if (this.innerPos.y > 0) {
                            this.innerPos.y -= (this.prevValue.y - diffY) * -1
                        } else {
                            if (diffY >= this.innerSize.height) {
                                diffY = this.innerSize.height
                            } else {
                                this.innerPos.y -= (this.prevValue.y - diffY) * -1
                            }
                        }
                    } else {
                        diffY = (this.startSize.height + (event.clientY - this.mouseStartPos.y)) - (this.startSize.height + (event.clientY - this.mouseStartPos.y)) % this.gridSize
                    }
                    if (diffY >= this.gridSize) {
                        this.innerSize.height = diffY
                    }
                    this.prevValue.y = Number(diffY)
                }
            }
        },
        sizeChangeMouseUp () {
            this.isSizeChange = false
        },
        rotateMouseDown (event) {
            setTimeout(() => {
                this.isDrag = false
                this.isRotate = true
                this.isElSelected = true
                this.mouseStartPos.x = event.clientX
                this.mouseStartPos.y = event.clientY
            }, 40)
            this.$emit('stateChange');
        },
        rotateMouseMove (event) {
            if (this.isRotate) {
                this.innerPos.rotation = Math.atan((event.clientX - this.mouseStartPos.x) / (event.clientY - this.mouseStartPos.y)) * 180 / Math.PI
            }
        },
        rotateMouseUp () {
            this.$emit('stateChange')
            this.isRotate = false
        },
        deleteBlock () {
            this.$emit('deleteElement')
        }
    },

    watch: {
        styleData: {
            handler (newValue) {
                this.styles = newValue
            },
            deep: true
        },
        styles: {
            handler (newValue) {
                this.innerSize.width = newValue.width
                this.innerSize.height = newValue.height
                this.innerPos.y = newValue.top
                this.innerPos.x = newValue.left
            },
            deep: true
        },
        innerSize: {
            handler (newValue) {
                this.$emit('changeObject', newValue.width, 'width')
                this.$emit('changeObject', newValue.height, 'height')
                this.styles.width = newValue.width
                this.styles.height = newValue.height
            },
            deep: true
        },
        innerPos: {
            handler (newValue) {
                this.$emit('changeObject', newValue.y, 'top')
                this.$emit('changeObject', newValue.x, 'left')
                this.styles.top = newValue.y
                this.styles.left = newValue.x
            },
            deep: true
        },
        selected (newValue) {
            this.isElSelected = newValue
        },
    },
}

</script>

<style scoped>
.block{
    text-align: left;
    display: inline-block;
    background: none;
    width: 200px;
    height: 100px;
    font-size: 10px;
    z-index: 1;
    margin: 0;
    padding: 0;
    cursor: move;
    border: 2px solid #888;
    margin: -2px;
}

.block-selected {
    border: 2px dotted #333 !important;
}

.pointer {
    background: #CCC;
    position: absolute;
    border-radius: 50%;
    border: 1px solid #444;
    z-index: 4;
    margin: 0;
    padding: 0;
}

.rotate-pointer {
    cursor: crosshair;
}
</style>
