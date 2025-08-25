<script>

import LeftMenu from "../components/LeftMenu.vue";
import ProjectSet from "../components/ProjectSet.vue";
import SrsSet from "../components/SrsSet.vue";
import axios from "axios";


export default {
  name: "ProjectDetail",
  data() {
    return {
      id: this.$route.query.id,
      project: {}
    }
  },
  methods: {
    init() {
      axios.get("http://localhost:8989/get_project_detail/", {params: {id: this.id}}).then(response => {
        this.project = response.data
      })
    },
    handlenameUpdate(newVal) {
      this.project.name = newVal
      axios.post("http://localhost:8989/update_project_detail/", this.project)
    }
  },
  mounted() {
    this.init()
  },
  watch: {
    '$route'(to, from) {
      if (to.query.id !== from.query.id) {
        this.id = to.query.id
        this.init()
      }
    }
  },
  components: {
    SrsSet,
    LeftMenu,
    ProjectSet
  },
}
</script>

<template>
  <el-container>
    <el-aside>
      <LeftMenu></LeftMenu>
    </el-aside>
    <el-container style="padding-left: 10px">
      <el-header>
        <h1>项目名称：{{ project.name }}</h1>
      </el-header>
      <el-main>
        <div>
          <el-tabs tab-position="top" style="" class="demo-tab">
            <el-tab-pane label="项目设置">
              <ProjectSet :project="project" @update-name="handlenameUpdate"></ProjectSet>
            </el-tab-pane>
            <el-tab-pane label="需求配置">
              <SrsSet :project="project"></SrsSet>
            </el-tab-pane>
            <el-tab-pane label="用例生成"></el-tab-pane>
            <el-tab-pane label="其他"></el-tab-pane>
          </el-tabs>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped>

</style>