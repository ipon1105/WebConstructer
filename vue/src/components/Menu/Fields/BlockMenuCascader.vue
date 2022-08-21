<template>
    <div>
        <p class="menu-block-cascader-el">
            {{ title }}
        </p>
        <span class="menu-block-cascader-el">
        <el-cascader
            class="menu-block-cascader"
            v-model="value"
            :options="additionalData"
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

<style scoped>

.menu-block-cascader-el {
    padding: 1rem 0;
}
</style>