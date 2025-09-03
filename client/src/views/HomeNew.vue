<template>
  <el-container>
    <el-aside>
      <LeftMenu></LeftMenu>
    </el-aside>

    <el-container>
      <el-header>
        <el-row :gutter="20">
          <el-col :span="6" v-for="(tip, index) in tips" :key= "index">
            <el-tag type="success" class="custom-large-tag">
              <i class="el-icon-info"></i>
              {{ tip.text }} : <strong>{{tip.count}}</strong>
              </el-tag>
            </el-col>
        </el-row>
      </el-header>
      <el-main>
        <HomeEcharts></HomeEcharts>
      </el-main>
      <el-footer class = "app-footer">
        <div class="footer-content">
          <div class="announcement">
            <h4>公告通知</h4>
            <ul>
              <li v-for="(notice, index) in notices" :key= "index">
                {{ notice }}
              </li>
            </ul>
          </div>
        </div>
      </el-footer>
    </el-container>
  </el-container>


</template>

<script>
import LeftMenu from "../components/LeftMenu.vue";
import HomeEcharts  from "../components/HomeEcharts.vue";
import aios from "axios";

export default {
  name: "HomeNew",
  data() {
    return {
      tips: [
        {text: "项目总数", count: 10},
        {text: "需求总数", count: 20},
        {text: "用例总数", count: 30},
        {text: "使用次数", count: 30},
      ],
      notices: [
      ],
    }
  },
  methods: {
    get_news(){
      aios.get("http://localhost:8989/get_news/").then(res => {
        this.notices = [res.data];
      })
    },
  },
   mounted() {
    this.get_news();
  },
  components: {HomeEcharts, LeftMenu}
}

</script>

<style scoped>
.custom-large-tag{
  font-size:15px;/*增大字体大小*/
  padding:15px 40px;/*增大内边距 */
  background-color: #1e7e9b;
  color:white;
  bored-radius: 10px;/*圆角*/
  height: 40px;
  box-shadow: 4px 4px 8px gray;
}
.app-footer {
  padding: 20px;
  text-align: center;
  border-top: 1px solid gainsboro;
}

.announcement ul {
  list-style: none;
  padding: 0;
}
.announcement li {
  color: #666;
  front-size: 14px;
  margin-bottom: 5px;
}

</style>