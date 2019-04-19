<template>
  <div>
    <el-row>
      <el-col>
        <g-header></g-header>
      </el-col>
    </el-row>
    <el-row class="rows-one">
      <el-col type="flex" justify="center" align="middle">
        <span class="title-main">社会实践</span>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <el-carousel :interval="4000" type="card" height="400px">
          <el-carousel-item v-for="item in pictures" :key="item.id">
            <el-row>
                <el-col :span="24" type="flex" align="middle" justify="center">
                    <img :src="item.img" class="img">
                </el-col>
              </el-row>
          </el-carousel-item>
        </el-carousel>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import header from './header'
export default {
  data () {
    return {
      pictures: [
        {
          id: 0,
          img: 'https://static.ericdiao.xyz/osa/one.jpg'
        },
        {
          id: 1,
          img: 'https://static.ericdiao.xyz/osa/two.jpg'
        },
        {
          id: 2,
          img: 'https://static.ericdiao.xyz/osa/three.jpg'
        },
        {
          id: 3,
          img: 'https://static.ericdiao.xyz/osa/four.jpg'
        },
        {
          id: 4,
          img: 'https://static.ericdiao.xyz/osa/five.jpg'
        },
        {
          id: 5,
          img: 'https://static.ericdiao.xyz/osa/six.jpg'
        },
        {
          id: 6,
          img: 'https://static.ericdiao.xyz/osa/seven.jpg'
        }
      ]
    }
  },
  components: {
    'g-header': header
  }
}
</script>
<style>
  .title-main {
    font-size: 80px;
    font-family: Arial !important;
  }
  .rows-one {
    margin-top: 20px;
  }
  .img {
    height: 400px !important;
    padding: 1px;
  }
</style>
