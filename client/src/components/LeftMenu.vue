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
        this.getProjects = response.data
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
  <el-menu
      style="height: 750px"
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
/* 外层容器样式 */
.menu-container {
  height: 100vh; /* 容器高度占满整个视口 */
  display: flex; /* 启用 flex 布局 */
}

/* 菜单样式 */
.full-height-menu {
  flex: 1; /* 宽度自适应，占满父容器 */
  min-width: 200px; /* 最小宽度防止内容挤压 */
  max-width: 300px; /* 最大宽度限制（可选） */
  height: 100%; /* 高度继承父容器 */
  background-color: #f5f7fa; /* 浅灰色背景 */
  border-right: none; /* 去掉右侧边框 */
  padding-top: 20px; /* 顶部内边距 */
}

/* 菜单项样式 */
.el-menu-item {
  font-size: 14px; /* 字体大小 */
  color: #333; /* 文字颜色 */
  margin: 8px 0; /* 上下外边距 */
  border-radius: 4px; /* 圆角 */
  transition: background-color 0.3s ease, color 0.3s ease; /* 过渡效果 */
}

/* 菜单项悬停效果 */
.el-menu-item:hover {
  background-color: #409eff; /* 悬停背景色 */
  color: #fff; /* 悬停文字颜色 */
}

/* 激活菜单项样式 */
.el-menu-item.is-active {
  background-color: #409eff; /* 激活背景色 */
  color: #fff; /* 激活文字颜色 */
  font-weight: bold; /* 加粗 */
}

/* 子菜单标题样式 */
.el-sub-menu__title {
  font-size: 14px; /* 字体大小 */
  color: #333; /* 文字颜色 */
  margin: 8px 0; /* 上下外边距 */
  border-radius: 4px; /* 圆角 */
  transition: background-color 0.3s ease, color 0.3s ease; /* 过渡效果 */
}

/* 子菜单标题悬停效果 */
.el-sub-menu__title:hover {
  background-color: #409eff; /* 悬停背景色 */
  color: #fff; /* 悬停文字颜色 */
}

/* 子菜单项样式 */
.el-sub-menu .el-menu-item {
  padding-left: 50px !important; /* 子菜单项缩进 */
  font-size: 13px; /* 字体大小 */
  color: #666; /* 文字颜色 */
}

/* 子菜单项悬停效果 */
.el-sub-menu .el-menu-item:hover {
  background-color: #e6f7ff; /* 悬停背景色 */
  color: #409eff; /* 悬停文字颜色 */
}

/* 链接样式 */
a {
  text-decoration: none; /* 去掉下划线 */
  color: inherit; /* 继承父元素颜色 */
}
</style>