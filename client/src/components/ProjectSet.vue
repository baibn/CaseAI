<script>
export default {
  name: "ProjectSet",
  props: ["project"],
  computed: {
    name: {
      get() {
        return this.project.name
      },
      set(val) {
        this.$emit('update-name', val)
      }
    }
  }
}

</script>

<template>
  <div class="input-wrap">
    <span class="label">项目名称：</span>
    <el-input type="text" v-model="name" class="short-input" placeholder="请输入项目名称"></el-input>
  </div>

</template>

<style scoped>
.input-wrap {
  display: flex;
  align-items: center;
}
.label {
  margin-right: 12px;
  min-width: 80px;
}
.short-input {
  width: 300px;
}
</style>