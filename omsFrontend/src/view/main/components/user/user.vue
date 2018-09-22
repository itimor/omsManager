<template>
  <div class="user-avator-dropdown">
    <Dropdown @on-click="handleClick">
      <Avatar :src="userAvator"/>
      <Icon :size="18" type="md-arrow-dropdown"></Icon>
      <DropdownMenu slot="list">
        <DropdownItem name="userinfo" disabled>{{username}}</DropdownItem>
        <DropdownItem name="changepasswd">修改密码</DropdownItem>
        <DropdownItem name="logout">退出登录</DropdownItem>
      </DropdownMenu>
    </Dropdown>

    <Modal v-model="changeForm"
           @on-ok="changePass('ruleForm')"
           title="修改密码">
      <Form ref="ruleForm" :model="passwdForm" :rules="passwdrules">
        <FormItem prop="new_password1">
          <Input type="text" v-model="passwdForm.new_password1" placeholder="密码">
            <Icon type="ios-lock-outline" slot="prepend"></Icon>
          </Input>
        </FormItem>
        <FormItem prop="new_password2">
          <Input type="text" v-model="passwdForm.new_password2" placeholder="确认密码">
            <Icon type="ios-lock-outline" slot="prepend"></Icon>
          </Input>
        </FormItem>
      </Form>
    </Modal>
  </div>
</template>

<script>
  import './user.less'
  import {mapGetters, mapActions} from 'vuex'
  import {changePassword} from '@/api/login'

  export default {
    name: 'User',
    props: {
      userAvator: {
        type: String,
        default: ''
      }
    },
    data() {
      const validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入新密码'));
        } else if (!/(?=.*\d)(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9])/.test(value)) {
          callback(new Error('密码中必须包含字母、数字、特称字符'));
        } else {
          if (this.passwdForm.new_password2 !== '') {
            // 对第二个密码框单独验证
            this.$refs.ruleForm.validateField('new_password2');
          }
          callback();
        }
      };
      const validatePassCheck = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.passwdForm.new_password1) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        changeForm: false,
        passwdForm: {
          new_password1: '',
          new_password2: ''
        },
        passwdrules: {
          new_password1: [
            {required: true, message: 'The new_password1 cannot be empty', trigger: 'blur'},
            {validator: validatePass, trigger: 'blur'}
          ],
          new_password2: [
            {required: true, message: 'The new_password2 cannot be empty', trigger: 'blur'},
            {validator: validatePassCheck, trigger: 'blur'}
          ]
        }
      }
    },
    computed: {
      ...mapGetters([
        'username'
      ]),
    },
    methods: {
      ...mapActions([
        'handleLogOut'
      ]),
      handleClick(name) {
        switch (name) {
          case 'changepasswd':
            this.changeForm = true
            break
          case 'logout':
            this.handleLogOut().then(() => {
              this.$router.push({
                name: 'login'
              })
            }).catch(error => {
              const errordata = JSON.stringify(error.response.data)
              this.$Message.error(errordata);
            })
            break
        }
      },
      changePass(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            changePassword(this.passwdForm).then(() => {
              this.handleLogOut().then(() => {
                this.$router.push({
                  name: 'login'
                })
              })
            }).catch(error => {
              const errordata = JSON.stringify(error.response.data)
              this.$Message.error(errordata);
            })
          } else {
            this.$Message.error('请认真填写!');
          }
        })
      }
    }
  }
</script>
