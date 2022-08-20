<template>
    <div class="menu-block-checbox-wrapper">
        <p
            class="menu-block-checbox-el menu-block-checbox-title"
        >
            {{ title }}
        </p>
        <el-checkbox
            size="large"
            v-model="value"
            class="menu-block-checbox-el menu-block-checbox"
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

<style scoped>
.menu-block-checbox-el {
    flex: 1
}
.menu-block-checbox-title {
    padding: .5rem 0;
}
.menu-block-checbox-wrapper {
    padding-bottom: 1rem;
    display: flex;
}
</style>