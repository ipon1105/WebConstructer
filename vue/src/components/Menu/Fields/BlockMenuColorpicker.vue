<template>
    <div class="menu-block-color-picker-wrapper">
        <p class="menu-block-color-picker-el">
            {{ title }}
        </p>
        <span
            class="menu-block-color-picker-el menu-block-color-picker"
        >
        <el-color-picker
            :predifine="additionalData"
            show-alpha
            v-model="value"
            @active-change="onChange"
        />
        </span>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            default: ''
        },
        additionalData: {
            default: () => ({})
        },
        val: {
            default: ''
        },
    },
    data: () => ({
        value: ''
    }),
    methods: {
        onChange (value) {
            this.value = value
        }
    },
    watch: {
        value (newValue) {
            this.$emit('blockChange', newValue)
        },
        val (newValue) {
            this.value = newValue
        }
    },
}
</script>

<style>
.menu-block-color-picker-el {
    flex: 1;
}
.menu-block-color-picker-wrapper {
    display: flex;
    padding: 1rem 0;
}
</style>