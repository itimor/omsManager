<style lang="less">
  @import './login.less';
</style>

<template>
  <div class="login">
    <div class="login-con">
      <Card icon="log-in" title="欢迎登录" :bordered="false">
        <div class="form-con">
          <Form ref="loginForm" :model="form" :rules="rules" @keydown.enter.native="handleSubmit">
            <FormItem prop="userName">
              <Input v-model="form.username" placeholder="请输入用户名">
                <span slot="prepend">
                  <Icon :size="16" type="ios-person"></Icon>
                </span>
              </Input>
            </FormItem>
            <FormItem prop="password">
              <Input :type="pwdType" v-model="form.password" @keyup.enter.native="handleSubmit" placeholder="请输入密码">
                <span slot="prepend">
                  <Icon :size="14" type="md-lock"></Icon>
                </span>
                <Button size="small" slot="append" :icon="eye" @click="showPwd"></Button>
              </Input>
            </FormItem>
            <FormItem>
              <Button @click="handleSubmit" type="primary" long>登录</Button>
            </FormItem>
          </Form>
        </div>
      </Card>
    </div>
  </div>
</template>

<script>
  import {mapActions} from 'vuex'

  export default {
    data() {
      return {
        pwdType: 'password',
        eye: 'md-eye',
        form: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
          password: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
        }
      }
    },
    methods: {
      ...mapActions([
        'handleLogin',
        'getUserInfo'
      ]),
      handleSubmit() {
        this.handleLogin(this.form).then(res => {
          this.getUserInfo({"username": this.form.username}).then(res => {
            this.$router.push(this.$route.query.redirect ||
              {
                name: 'home'
              })
          })
        }).catch(error => {
          const errordata = JSON.stringify(error.response.data)
          this.$Message.error(errordata);
        })
      },
      showPwd() {
        if (this.pwdType === 'password') {
          this.pwdType = 'text'
          this.eye = 'md-eye-off'
        } else {
          this.pwdType = 'password'
          this.eye = 'md-eye'
        }
      },
    }
  }
</script>

<style>

</style>
