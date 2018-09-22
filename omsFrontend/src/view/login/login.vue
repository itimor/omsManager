<style lang="less">
  @import './login.less';
</style>

<template>
  <div class="login">
    <div class="login-con">
      <Card icon="log-in" title="欢迎登录" :bordered="false">
        <div class="form-con">
          <login-form @on-success-valid="handleSubmit"></login-form>
        </div>
      </Card>
    </div>
  </div>
</template>

<script>
  import LoginForm from '_c/login-form'
  import {mapActions} from 'vuex'

  export default {
    components: {
      LoginForm
    },
    methods: {
      ...mapActions([
        'handleLogin',
        'getUserInfo'
      ]),
      handleSubmit({username, password}) {
        this.handleLogin({username, password}).then(res => {
          this.getUserInfo({"username":username}).then(res => {
            this.$router.push(this.$route.query.redirect ||
              {
                name: 'home'
              })
          })
        }).catch(error => {
          const errordata = JSON.stringify(error.response.data)
          this.$Message.error(errordata);
        })
      }
    }
  }
</script>

<style>

</style>
