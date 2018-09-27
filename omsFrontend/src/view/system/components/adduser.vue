<template>
  <Form ref="ruleForm" :model="ruleForm" :rules="rules" :label-width="80">
    <FormItem label="名称" prop="username">
      <Input type="text" v-model="ruleForm.username" placeholder="input">
      </Input>
    </FormItem>
    <FormItem label="邮箱" prop="email">
      <Input type="text" v-model="ruleForm.email" placeholder="input">
      </Input>
    </FormItem>
    <FormItem label="头像" prop="avator">
      <Input type="text" v-model="ruleForm.avator" placeholder="input">
      </Input>
    </FormItem>
    <FormItem label="skype" prop="skype">
      <Input type="text" v-model="ruleForm.skype" placeholder="input">
      </Input>
    </FormItem>
    <FormItem label="角色" prop="roles">
      <Select v-model="ruleForm.roles" multiple>
        <Option v-for="item in roles" :key="item.id" :value="item.name">{{ item.name }}</Option>
      </Select>
    </FormItem>
    <FormItem label="密码" prop="password">
      <Input type="text" v-model="ruleForm.password" placeholder="input">
      </Input>
    </FormItem>
    <FormItem label="激活" prop="is_active">
      <Checkbox v-model="ruleForm.is_active">账号激活</Checkbox>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="submitForm('ruleForm')">提交</Button>
    </FormItem>
  </Form>
</template>
<script>
  import {postUser, getRole} from '@/api/user'

  export default {
    data() {
      return {
        ruleForm: {
          username: '',
          email: '',
          avator: 'https://avatars0.githubusercontent.com/u/20942571?s=460&v=4',
          skype: null,
          password: '',
          roles: [],
          is_active: true
        },
        rules: {
          username: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
          email: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
          password: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
          roles: [
            {required: true, type: 'array', message: 'The input cannot be empty', trigger: 'change'},
          ],
        },
        roles: []
      }
    },
    created() {
      this.fetchRoleData()
    },
    methods: {
      submitForm(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            postUser(this.ruleForm).then(() => {
              this.$emit('DialogStatus', false)
            }).catch(error => {
              const errordata = JSON.stringify(error.response.data)
              this.$Message.error(errordata);
            })
          } else {
            this.$Message.error('请认真填写!');
          }
        })
      },
      fetchRoleData() {
        getRole(this.listQuery).then(res => {
          this.roles = res.data
        })
      }
    }
  }
</script>
