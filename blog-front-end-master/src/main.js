import { createApp } from 'vue'
import App from './App.vue' 
import HomePage from './components/HomePage.vue'
import BlogPage from './components/BlogPage.vue'
import ContactPage from './components/ContactPage.vue'
import LoginPage from './components/admin/LoginPage.vue'
import DashboardPage from './components/admin/DashboardPage.vue'
import NewBlog from './components/admin/NewBlog.vue'
import SearchResult from './components/SearchResult.vue'
import { createMemoryHistory, createRouter } from 'vue-router'


const routes = [
    {path: '/', component: HomePage},
    {path: '/blog/:id', name: 'blog', component: BlogPage, props: true},
    {path: '/searchresult/:categoryId', name: 'searchresult', component: SearchResult, props: true},
    {path: '/admin', component: LoginPage},
    {path: '/manageblog/:id',name: 'manageblog', component: NewBlog, props: true},
    {path: '/dashboard', component: DashboardPage},
    {path: '/contactpage', component: ContactPage}


]
 
//createApp.use(VueQuill)


const router = createRouter({
    history: createMemoryHistory(),
    routes,
  })

createApp(App).use(router).mount('#app')

