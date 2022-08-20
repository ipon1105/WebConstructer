export default {
    actions: {
        fetchMenuData () {
            return null
        },
        changeGridSize (ctx, gridSize) {
            ctx.commit('updateGridSize', gridSize)
        },
    },
    mutations: {
        updateGridSize (state, gridSize) {
            state.gridSize = gridSize
        },
    },
    state: {
        menuData: [
            {
                title: 'Задний Фон',
                name: 'Background',
                single: true,
            },
            {
                title: 'Текст',
                name: 'Text',
            },
            {
                title: 'Картинка',
                name: 'Image',
            },
            {
                title: 'Фигура',
                name: 'Figure',
            },
            {
                title: 'Слайдер',
                name: 'Slider',
            },
            {
                title: 'Форма',
                name: 'Form',
            },
            {
                title: 'Кнопка',
                name: 'Button',
            },
            {
                title: 'Поле ввода',
                name: 'Input',
            },
        ],
        gridSize: 20,
        menuWidth: 20
    },
    getters: {
        getMenuData (state) {
            return state.menuData
        },
        getGridSize (state) {
            return state.gridSize
        },
        getMenuWidth (state) {
            return state.menuWidth
        },
    }
}