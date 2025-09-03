import { createRouter, createWebHashHistory } from 'vue-router'
import HomeNew from '../views/HomeNew.vue'
import ProjectDetail  from "../views/ProjectDetail.vue";

const routes = [
  {
    path: '/',
    name: 'homenew',
    redirect: '/homenew'
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/homenew',
    component: HomeNew,
  },
  {
    path: '/detail/',
    component: ProjectDetail,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
