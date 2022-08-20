<template>
    <div>
        <p>
            {{ title }} {{ value }}
        </p>
        <el-slider
            size="large"
            v-model="value"
            class="slider"
        />
    </div>
</template>

<script>
export default {
    props: {
        title: {
            default: ''
        },
        val: {
            default: ''
        },
    },
    data: () => ({
        value: ''
    }),
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
.slider{
    width: 70%;    
}
</style>