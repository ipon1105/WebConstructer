<template>
    <div>
        <el-input
            class="block-menu-input"
            v-model="value"
            :clearable="true"
        >
            <template #prepend>
                <span class="block-menu-input-content">
                    {{ title }}
                </span>
            </template>
        </el-input>
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

<style scoped>
.block-menu-input{
    margin-bottom: 1.2rem;
    margin-left: -0.5rem;
}
</style>