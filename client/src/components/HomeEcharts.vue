<template>
  <br><br>
  <el-card class="chart-container">
    <div ref="chart" style="width: 100%;height: 400px"></div>
    <span style="font-size: xx-small">
      使用次数每月1日统计
    </span>
  </el-card>
</template>
<script>
import * as echarts from 'echarts';
import {ref, onMounted} from 'vue';

export default {
  name: 'HomeEcharts',
  setup() {
    const chart = ref(null);
    onMounted(() => {
      const myChart = echarts.init(chart.value);
      const option = {
        title: {
          text: '平台测试用例使用次数统计折线图',
          left: 'center'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['次数']
        },
        xAxis: {
          type: 'category',
          data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          name: '使用次数',
          type: 'line',
          data: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
          itemStyle: {
            color: '#409eff'
          },
          lineStyle: {
            width: 3,
          },
          symbol: 'circle',
          symbolSize: 10,
        }]
      }
      myChart.setOption(option);
    })
    return {
      chart
    }
  }
};
</script>

<style scoped>
.chart-container {
  margin: 20px;
}
</style>