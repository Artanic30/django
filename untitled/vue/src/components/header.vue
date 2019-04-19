<template>
 <div class="header">
   <el-row type="flex" class="row-chicken" justify="space-between" align="middle" :gutter="15">
          <el-col :span="4">
            <el-row type="flex" justify="left" align="middle" :gutter="18">
              <el-col type="flex" justify="center" align="middle">
                <img v-bind:src="img" class="img-logo">
              </el-col>
            </el-row>
          </el-col>
         <el-col :span="5" v-if="checklogin">
           <el-button class="button-login" @click="login">
                 <span class="title-small">login</span>
           </el-button>
         </el-col>
         <el-col :span="7" v-else>
           <el-button class="button-login" @click="logout" type="flex" align="middle" justify="center">
             <el-row>
               <el-col>
                 <span class="title-small">logout</span>
               </el-col>
             </el-row>
           </el-button>
         </el-col>
   </el-row>
 </div>
</template>
<script>
export default {
  data () {
    return {
      img: require('../assets/logo.png')
    }
  },
  methods: {
    login () {
      /* this.axios({
        method: 'get',
        url: `user/login/oauth/param`
      }).then((response) => {
        // window.location.href = response.data.login_url // todo: warning
        window.location.reload()
      }).catch((error) => {
        this.$message({
          type: 'error',
          message: error,
          showClose: true
        })
      }) */
      this.$store.commit('login')
      window.location.reload()
    },
    logout () {
      this.$store.commit('logout')
      window.location.reload()
    }
  },
  computed: {
    checklogin () {
      return this.$route.name === 'login'
    },
    checkState () {
      return this.$store.state.isAuthorized
    }
  },
  created () {
    if (this.checklogin && this.checkState) {
      this.$router.push('/register')
    } else if (!this.checkState && this.$route.name === 'register') {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
  .row-chicken {
    background-color: #A40006;
  }
  .img-logo {
    margin-top: 10px !important;
    margin-bottom: 10px !important;
    height: 50px ! important;
  }
  .header {
    background-color: #A40006;
    width: 100% ! important;
  }
  .button-login {
    float: right;
    background-color: white;
    margin-top: 2px;
    margin-right: 10px;
    font-size: 15px;
    width: 80px;
  }
  .title-small{
    font-size: 15px;
  }
</style>
