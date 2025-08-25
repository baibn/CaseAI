<script>
import axios from "axios";

export default {
  name: "SrsSet",
  data() {
    return {
      ole_srs: '',
      new_srs: [],
      showDialog: false,
      srs_case_set: [],
    }
  },
  methods: {
    save_set() {
      axios.post('http://localhost:8989/save_set/?project_id=' + this.project.id, JSON.stringify(this.srs_case_set)).then(
          this.showDialog = false)
    },
    begin_set() {
      const loadingInstance = this.$loading({
        lock: true,
        text: '正在优化需求，请稍后...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.5)'
      });
      axios.post('http://localhost:8989/begin_set/?project_id=' + this.project.id, {
        old_srs: this.ole_srs,
        new_srs: this.new_srs
      }).then(res => {
        this.new_srs = res.data
        this.showDialog = false
        loadingInstance.close()
      })

    },
    srs_fj() {
      const loadingInstance = this.$loading({
        lock: true,
        text: '需求正在分解中，请稍后...',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.5)'
      });
      axios.post("http://localhost:8989/srs_fj/?project_id=" + this.project.id, JSON.stringify(this.ole_srs)).then(res => {
        this.new_srs = res.data
        console.log(this.new_srs)
        loadingInstance.close()
      })
    },
    optimize_new_srs() {
      axios.get("http://localhost:8989/get_srs_case_set/?project_id=" + this.project.id).then(res => {
        this.srs_case_set = res.data
        this.showDialog = true
      })

    },
    save_new_srs() {
      axios.post("http://localhost:8989/save_new_srs/?project_id=" + this.project.id, JSON.stringify(this.new_srs)).then(
          this.$message.success("保存成功")
      )
    },
    deleteItem(index) {
      this.new_srs.splice(index, 1)
    },
    addItem() {
      this.new_srs.push("")
    }
  },
  watch: {
    'project.id': {
      immediate: true,
      handler(newId) {
        if (newId) {
          axios.get("http://localhost:8989/get_new_srs/?project_id=" + this.project.id).then(res => {
            this.new_srs = res.data
          })
        }
      }
    }
  },
  props: ['project'],
}
</script>

<template>
  <div style="text-align: left">
    <span style="font-size: small">(需求配置步骤：1.需求分解 2.需求优化 3.人工确认 4.保存结果)</span>
    <div>
      <br>
      <el-card class="custom-card">
        <template #header>
          <div class="card-header">
            <el-button type="success" style="position: absolute;right: 10px" @click="srs_fj">开始分解</el-button>
            <span>请粘贴原始需求</span>
          </div>
        </template>
        <div>
          <el-input v-model="ole_srs" type="textarea" :rows="3"
                    placeholder="请输入原始需求后点击右侧开始分解按钮"></el-input>
        </div>
      </el-card>
    </div>
    <div>
      <br>
      <el-card class="custom-card">
        <template #header>
          <div class="card-header">
            <el-button @click="optimize_new_srs" type="primary" style="position: absolute;right: 100px">先优化
            </el-button>
            <el-button @click="save_new_srs" type="primary" style="position: absolute;right: 10px">再保存</el-button>
            <span>分解结果：</span><span
              style="font-size: xx-small;color: gray">(请人工确认，确保分解正常后点击右侧保存按钮)</span>
          </div>
        </template>
        <div v-for="(item,index) in new_srs" :key="index" class="card-content"
             style="display: flex;align-items: center;margin-bottom: 5px;">
          <span style="min-width: 30px">{{ index + 1 }}.</span>
          <el-input v-model="new_srs[index]" style="flex-grow: 1"/>
          &#12288;<el-button type="danger" @click="deleteItem(index)">删除</el-button>
        </div>
        <el-button type="warning" @click="addItem" style="margin-top: 10px">新增</el-button>
      </el-card>
    </div>
    <el-dialog
        v-model="showDialog"
        title="需求优化配置弹层"
        width="80%"
    >
      <!--内容插槽-->
      <div v-for="(item,index) in srs_case_set" :key="index">
        <div class="input-group">
          <el-input v-model="item.Name" style="flex: 0 0 150px;margin-right: 5px"/>
          <el-input v-model="item.AIContent" style="flex: 2"/>
        </div>
      </div>
      <!--简单底部-->
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="showDialog = false">取消</el-button>
          <el-button type="primary" @click="save_set">保存</el-button>
          <el-button type="success" @click="begin_set">开始优化</el-button>
        </span>
      </template>
    </el-dialog>

  </div>
</template>

<style scoped>
.input-group {
  display: flex;
  align-items: center; /*垂直居中*/
  gap: 5px;
  height: 40px;
}
</style>