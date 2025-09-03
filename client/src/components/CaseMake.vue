<template>
  <div style="text-align: left">
    <span style="font-size: small"
      >（生成结果较慢，请耐心等待，不要刷新或关闭页面）</span
    >
    <div>
      <br />
      <el-card class="custom-card">
        <template #header>
          <div class="card-header">
            <el-button
              type="success"
              @click="srs_fj"
              style="position: absolute; right: 10px"
              >开始生成</el-button
            >
            <span>基本生成信息</span
            ><span style="font-size: xx-small; color: gray"
              >（请确保无误后点击右侧'开始生成按钮'）</span
            >
          </div>
        </template>
        <div class="card-content">
          <div style="display: flex;align-items: center;gap: 10px">
            <span style="flex-shrink: 0">原始需求</span>
            <el-input
            :value="old_srs"
            readonly
            style="flex: 1"
            disabled
            placeholder="此处展示原始需求"></el-input>
          </div>
          <span>生成任务数量：{{new_srs.length}}</span>
        </div>
      </el-card>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'CaseMake',
  data() {
    return {
      old_srs: '',
      new_srs: '',
    }
  },
  methods: {},
  watch: {
    'project.id': {
      immediate: true, // 立即执行一次
      handler(newId) {
        if (newId) {
          axios.get('http://localhost:8989/get_old_srs/?project_id=' + this.project.id).then(res => {
            this.old_srs = res.data
            })
          axios.get('http://localhost:8989/get_new_srs/?project_id=' + this.project.id).then(res=> {
              this.new_srs = res.data
            })
        }
      },

    },
  },
  props: ['project'],
  computed: {
    name: {
      get() {
        return this.project.id // 从prop获取初始值
      },
    },
  },
}
</script>
<style scoped>
.card-content {
  margin-bottom: 5px;
}
.input-group {
  display: flex; /* 启用 Flex 布局 */
  align-items: center; /* 垂直居中 */
  gap: 5px; /* 元素间距 */
  /* 如果不需要响应式可以固定高度 */
  height: 40px;
}
</style>
