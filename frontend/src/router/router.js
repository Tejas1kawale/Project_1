import { createWebHistory,createRouter } from 'vue-router'
import main from '../components/Dashboard/main.vue' 
import login from '../components/AuthComponents/login.vue'

const router = createRouter({
    history: createWebHistory(),
    routes:[
        {
            path : '/',
            component: main
        },
        {
            path: '/login',
            component: login
        }
    ]
})

export {router}