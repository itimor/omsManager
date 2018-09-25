<template>
  <Form ref="ruleForm" :model="ruleForm" :rules="rules" :label-width="80">
    <FormItem label="名称" prop="name">
      <Input type="text" v-model="ruleForm.name" placeholder="名称">
      </Input>
    </FormItem>
    <FormItem label="key" prop="key">
      <Input type="text" v-model="ruleForm.key" placeholder="key">
      </Input>
    </FormItem>
    <FormItem label="secret" prop="secret">
      <Input type="text" v-model="ruleForm.secret" placeholder="secret">
      </Input>
    </FormItem>
    <FormItem label="类型" prop="type">
      <Select v-model="ruleForm.type">
        <Option v-for="item in Dns_Types" :value="item" :key="item">{{ item }}</Option>
      </Select>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="submitForm('ruleForm')">提交</Button>
    </FormItem>
  </Form>
</template>
<script>
  import {putDnsApi} from '@/api/dnsmanager'

  export default {
    props: {
      ruleForm: {
        type: Object,
      }
    },
    data() {
      return {
        rules: {
          name: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
          key: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
          secret: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ],
          type: [
            {required: true, message: 'The select cannot be empty', trigger: 'change'},
          ]
        },
        Dns_Types: ['dnspod', 'godaddy', 'bind']
      }
    },
    methods: {
      submitForm(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            putDnsApi(this.ruleForm.id, this.ruleForm).then(() => {
              this.$emit('DialogStatus', false)
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
