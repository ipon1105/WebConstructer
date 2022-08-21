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
                id: 0,
                title: 'Задний Фон',
                name: 'Background',
                single: true,
            },
            {
                id: 1,
                title: 'Текст',
                name: 'Text',
            },
            {
                id: 2,
                title: 'Картинка',
                name: 'Image',
            },
            {
                id: 3,
                title: 'Фигура',
                name: 'Figure',
            },
            {
                id: 4,
                title: 'Слайдер',
                name: 'Slider',
            },
            {
                id: 5,
                title: 'Форма',
                name: 'Form',
            },
            {
                id: 6,
                title: 'Кнопка',
                name: 'Button',
            },
            {
                id: 7,
                title: 'Поле ввода',
                name: 'Input',
            },
        ],
        blockMenuData: {
            1: [
                {
                    title: 'ширина',
                    field: 'width',
                    type: 'Input',
                    measure: 'px',
                    defaultValue: 100,
                },
                {
                    title: 'высота',
                    field: 'height',
                    type: 'Input',
                    measure: 'px',
                    defaultValue: 100,
                },
                {
                    title: 'X',
                    field: 'left',
                    type: 'Input',
                    measure: 'px',
                    defaultValue: 100,
                },
                {
                    title: 'Y',
                    field: 'top',
                    type: 'Input',
                    measure: 'px',
                    defaultValue: 100,
                },
                {
                    title: 'Слой',
                    field: 'z-index',
                    type: 'Input',
                    measure: 'none',
                    defaultValue: 0,
                },
                {
                    title: 'Рамка',
                    field: 'border',
                    type: 'Checkbox',
                    measure: 'none',
                    defaultValue: true,
                    values: {
                        false: 'none',
                        true: ''
                    },
                },
                {
                    title: 'Размер шрифта: ',
                    field: 'font-size',
                    type: 'Slider',
                    measure: 'px',
                    defaultValue: 12,
                },
                {
                    title: 'Скругление углов: ',
                    field: 'border-radius',
                    type: 'Slider',
                    measure: '%',
                    defaultValue: 0,
                    additionalData: [
                        0,
                        50,
                    ]
                },
                {
                    title: 'Цвет фона: ',
                    field: 'background-color',
                    type: 'Colorpicker',
                    measure: 'none',
                    defaultValue: 'rgba(255, 255, 255, 1)',
                    additionalData: [
                        '#ff4500',
                        '#ff8c00',
                        '#ffd700',
                        '#90ee90',
                        '#00ced1',
                        '#1e90ff',
                        '#c71585',
                        'rgba(255, 69, 0, 0.68)',
                        'rgb(255, 120, 0)',
                        'hsv(51, 100, 98)',
                        'hsva(120, 40, 94, 0.5)',
                        'hsl(181, 100%, 37%)',
                        'hsla(209, 100%, 56%, 0.73)',
                        '#c7158577',
                    ]
                },
                {
                    title: 'Цвет текста: ',
                    field: 'color',
                    type: 'Colorpicker',
                    measure: 'none',
                    defaultValue: 'rgba(0, 0, 0, 1)',
                    additionalData: [
                        '#ff4500',
                        '#ff8c00',
                        '#ffd700',
                        '#90ee90',
                        '#00ced1',
                        '#1e90ff',
                        '#c71585',
                        'rgba(255, 69, 0, 0.68)',
                        'rgb(255, 120, 0)',
                        'hsv(51, 100, 98)',
                        'hsva(120, 40, 94, 0.5)',
                        'hsl(181, 100%, 37%)',
                        'hsla(209, 100%, 56%, 0.73)',
                        '#c7158577',
                    ]
                },
                {
                    title: 'Шрифт',
                    field: 'font-family',
                    type: 'Cascader',
                    measure: 'none',
                    defaultValue: 'Roboto',
                    additionalData: [
                        {
                            value: 'Times New Roman',
                            label: 'Times New Roman'
                        },
                        {
                            value: 'Georgia',
                            label: 'Georgia'
                        },
                        {
                            value: 'Arial',
                            label: 'Arial'
                        },
                        {
                            value: 'Comic Sans MS',
                            label: 'Comic Sans MS'
                        },
                        {
                            value: 'Impact',
                            label: 'Impact'
                        },
                        {
                            value: 'Tahoma',
                            label: 'Tahoma'
                        },
                    ]
                },
                {
                    title: 'Выравнивание текста',
                    field: 'text-align',
                    type: 'Imgset',
                    measure: 'none',
                    defaultValue: 'left',
                    additionalData: [
                        {
                            src: 'iconAlignLeft.png',
                            val: 'left',
                        },
                        {
                            src: 'iconAlignCenter.png',
                            val: 'center',
                        },
                        {
                            src: 'iconAlignRight.png',
                            val: 'right',
                        },
                    ]
                }


            ]
        },
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
        getBlockMenuDataById (state) {
            return state.blockMenuData
        }
    }
}