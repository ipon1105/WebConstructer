import axios from 'axios'

export default {
    actions: {
        fetchMenuData (ctx) {
            return axios.get('http://26.243.23.165:8000/api/widgets/')
                .then(response => ctx.commit('updateMenuData', response.data))
        },
        fetchBlockMenuData (ctx) {
            ctx
            return axios.get('http://26.243.23.165:8000/api/widgets_property/')
                .then(response => ctx.commit('updateBlockMenuData', response.data))
        },
        changeGridSize (ctx, gridSize) {
            ctx.commit('updateGridSize', gridSize)
        },
    },
    mutations: {
        updateGridSize (state, gridSize) {
            state.gridSize = gridSize
        },
        updateMenuData (state, gridSize) {
            state.menuData = gridSize
        },
        updateBlockMenuData (state, blockMenuData) {
            for (let block of blockMenuData) {
                if (!state.blockMenuData[block.parentId]) {
                    state.blockMenuData[block.parentId] = []
                }
                state.blockMenuData[block.parentId].push(block)
            }
            console.log(state.blockMenuData)
        },
    },
    state: {
        menuData: [],
        blockMenuData: {},
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