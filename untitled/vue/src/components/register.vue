<template>
  <div>
    <el-row>
      <el-col>
        <g-header></g-header>
      </el-col>
    </el-row>
    <el-row class="rows-one">
      <el-col class="left_side">
        <span class="title">{{ userInfo.name }}</span>
      </el-col>
    </el-row>
    <el-row class="rows-one">
      <el-col type="flex" align="middle">
        <el-card class="card-only">
            <el-collapse v-model="activeNames">
              <el-collapse-item title="我的志愿" name="1">
                <el-card>
                  <span class="title">{{ userInfo.will}}</span>
                </el-card>
              </el-collapse-item>
            </el-collapse>
          </el-card>
      </el-col>
    </el-row>
    <el-row class="rows-one">
      <el-col class="left_side">
        <span class="sub-title">Tips: 每次选择地点会覆盖之前数据</span>
      </el-col>
    </el-row>
    <el-row class="rows-one">
      <el-col type="flex" align="middle">
        <el-card class="card-only">
          <el-table
          :data="sites"
          style="width: 100%">
          <el-table-column
            label="地点"
            prop="location">
          </el-table-column>
          <el-table-column
            label="日期"
            prop="time">
          </el-table-column>
          <el-table-column
            label="可选人数"
            prop="capacity">
          </el-table-column>
          <el-table-column
            label="以选人数"
            prop="student">
          </el-table-column>
            <el-table-column
              fixed="right"
              label="操作">
              <template slot-scope="scope">
                <el-button type="text" size="small" class="button-self" @click="register(scope.row)">选择</el-button>
              </template>
            </el-table-column>
        </el-table>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import header from './header'
export default {
  data () {
    return {
      activeNames: '1',
      userInfo: {
        name: 'Hammer WAng',
        will: 'Beijing'
      },
      sites: [{
        location: 'test1',
        capacity: 20,
        time: '6.7',
        student: 23
      }
      ]
    }
  },
  components: {
    'g-header': header
  },
  methods: {
    register (row) {
      this.axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/site`,
        data: JSON.stringify(row.location),
        headers: {'X-CSRFToken': this.$cookie.get('csrftoken')}
      }).then((response) => {
        alert('报名成功!')
        window.location.reload()
      })
        .catch((err) => {
          this.$message({
            type: 'error',
            message: err.response.data,
            showClose: true
          })
        })
    }
  },
  created () {
    this.axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/api/user`
    }).then((response) => {
      this.userInfo = response.data
    }).catch((err) => {
      this.$message({
        type: 'error',
        message: err.response.data,
        showClose: true
      })
    })
    this.axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/api/site`
    }).then((response) => {
      this.sites = response.data
    }).catch((err) => {
      this.$message({
        type: 'error',
        message: err,
        showClose: true
      })
    })
  }
}
</script>
<style>
  .card-only {
    width: 80%;
  }
  .el-collapse-item__content {
    padding-bottom: 0 !important;
  }
  .el-collapse-item__header {
    padding-left: 10px !important;
  }
  .rows-one {
    margin-top: 3%;
  }
  .title {
    font-size: 30px;
  }
  .left_side {
    padding-left: 10%;
  }
  .sub-title {
    font-size: 20px;
  }
  .el-table {
    font-size: 20px! important;
  }
  .button-self {
    font-size: 20px;
  }
  .el-table .cell {
    line-height: 70px !important;
  }
</style>
