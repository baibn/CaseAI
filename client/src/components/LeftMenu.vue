<script>
import aios from "axios"
export default {
  name: 'LeftMenu',
  data(){
    return {
      projects: [],
      dialogVisible: false,
      new_project: {
        name: '',
      }
    }
  },
  methods:{
    getProjects(){
      aios.get('http://127.0.0.1:8989/get_projects/')
          .then(response => {
            this.projects = response.data
          })
    },
    addProject(){
      aios.get('http://127.0.0.1:8989/add_project/', {
        params: {
          name: this.new_project.name
        }
      }).then(response => {
        // 实时更新子菜单（project是数组）
        if (response.data){
          this.projects.push(response.data)
        }
        this.new_project = {name: ''}
        this.dialogVisible = false
      })
    }
  },
  mounted() {
    this.getProjects()
  }
}

</script>

<template>
  <div class="layout">
  <el-menu
      :default-active="$route.path"
      class="cool-menu"
      background-color="#1e1e2e"
      text-color="#bfcbd9"
      active-text-color="#fff"
      :collapse="isCollapse"
      :collapse-transition="false"
      router
  >
    <el-menu-item index="/homenew">【回到首页】</el-menu-item>
    <el-sub-menu index="1">
      <template #title>项目列表</template>
      <el-button @click="dialogVisible = true">增加项目</el-button>
      <el-menu-item v-for="i in projects" :key="i" :index="'/detail/?id=' + i.id">进入项目：{{i.name}}</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="2">
      <template #title>系统维护</template>
      <el-menu-item>训练管理</el-menu-item>
      <el-menu-item>AI管理</el-menu-item>
      <el-menu-item>平台配置</el-menu-item>
      <el-menu-item>公告信息</el-menu-item>
      <a href="http://127.0.0.1:8000/admin/" style="text-decoration: none" target="_blank">
        <el-menu-item>后台管理</el-menu-item>
      </a>
    </el-sub-menu>
    <el-menu-item index="/">获取帮助</el-menu-item>
    <el-menu-item index="/">反馈建议</el-menu-item>
  </el-menu>
</div>
  <el-dialog v-model="dialogVisible" title="增加项目" style="width: 40%">
    <el-form v-model = "new_project">
      <el-form-item label="项目名称">
        <el-input v-model="new_project.name" placeholder="请输入项目名称"></el-input>
      </el-form-item>
    </el-form>
      <template #footer>
        <div class="dialog-footer">
        <el-button  @click="addProject">创建</el-button>
        </div>
      </template>
  </el-dialog>
</template>

<style scoped>

/* 2. 布局容器 */
.layout {
  display: flex;
  flex-direction: column;
  height: 100%;
}

/* 让 el-menu 自动撑满剩余高度 */
.cool-menu {
  flex: 1;
  overflow-y: auto;
  border: none;
  padding: 0 8px;
}

/* 顶部 logo 块 */
.cool-menu logo {
  height: 60px;
  line-height: 60px;
  color: #fff;
  font-size: 20px;
  text-align: center;
  background: rgba(0,0,0,.25);
  backdrop-filter: blur(10px);
  margin-bottom: 10px;
  border-radius: 6px;
}

/* 菜单项圆角 + 悬停动效 */
.cool-menu el-menu-item,
.cool-menu el-submenu__title {
  border-radius: 6px;
  margin: 4px 0;
  height: 46px;
  line-height: 46px;
  transition: all .3s;
}
.cool-menu el-menu-item:hover,
.cool-menu el-submenu__title:hover {
  background: rgba(255,255,255,.1) !important;
  transform: translateX(4px);
}

/* 激活项 */
.cool-menu el-menu-item is-active {
  background: linear-gradient(90deg, #6a5af9, #d66efd) !important;
  box-shadow: 0 2px 8px rgba(102,95,249,.6);
  color: #fff !important;
}
</style>