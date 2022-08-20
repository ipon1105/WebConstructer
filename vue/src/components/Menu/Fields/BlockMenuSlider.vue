<template>
    <div>
        <p>
            {{ title }} {{ value }}
        </p>
        <el-slider
            size="large"
            v-model="value"
            class="slider"
            :min="additionalData[0]"
            :max="additionalData[1]"
        />
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