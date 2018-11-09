<template>
  <Form ref="ruleForm" :model="ruleForm" :label-width="80">
    <FormItem label="值" prop="value">
      <Input type="textarea" :rows="4" v-model="ruleForm.value" placeholder="多个ip用着`|`分割，如 `127.0.0.1|128.0.0.1`">
      </Input>
      <a class="tips">Tip：多个ip用着`|`分割，如 `127.0.0.1|128.0.0.1`</a>
    </FormItem>
    <FormItem>
      <Button type="primary" @click="submitForm('ruleForm')">提交</Button>
    </FormItem>
  </Form>
</template>
<script>
  import {postActionWhiteip} from '@/api/firewall'

  export default {
    props: {
      ruleForm: {
        type: Object
      }
    },
    data() {
      return {}
    },
    methods: {
      submitForm(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            postActionWhiteip(this.ruleForm).then(res => {
              if (res.data.status.code == 1) {
                this.$Message.success(res.data.status.message);
                this.$emit('DialogStatus', false)
              } else {
                this.$Message.error(res.data);
              }
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
