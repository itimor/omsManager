<template>
  <Form ref="ruleForm" :model="ruleForm" :rules="rules" :label-width="80">
    <FormItem label="名称" prop="name">
      <Input type="text" v-model="ruleForm.name" placeholder="input">
      </Input>
    </FormItem>
    <FormItem label="备注" prop="desc">
      <Input type="textarea" :rows="4" v-model="ruleForm.desc" placeholder="input">
      </Input>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="submitForm('ruleForm')">提交</Button>
    </FormItem>
  </Form>
</template>
<script>
  import { postCdnsite } from '@/api/cdnbest'

  export default {
    data() {
      return {
        ruleForm: {
          name: '',
          desc: ''
        },
        rules: {
          name: [
            {required: true, message: 'The input cannot be empty', trigger: 'blur'},
          ]
        }
      }
    },
    methods: {
      submitForm(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            postCdnsite(this.ruleForm).then(() => {
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
