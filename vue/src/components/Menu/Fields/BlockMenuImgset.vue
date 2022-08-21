<template>
    <div>
        <p class="menu-block-imgset-el">
            {{ title }}
        </p>
        <div class="menu-block-imgset-el menu-block-imgset-img-wrapper">
            <img
                v-for="img in additionalData"
                :key="img.src"
                :src="require('@/assets/image/' + img.src)"
                class="menu-block-imgset-img"
                @click="setValue(img.val)"
            />
        </div>
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
        setValue (newValue) {
            this.value = newValue
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

<style scoped>
.menu-block-imgset-el {
    padding-top: 1rem;
}

.menu-block-imgset-img-wrapper {
    display: flex;
    width: 40%;
}

.menu-block-imgset-img {
    flex: 1;
}

.menu-block-imgset-img:hover {
    background: rgba(0.4, 0.4, 0.4, 0.4);
}
</style>