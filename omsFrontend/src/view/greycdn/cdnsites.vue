<template>
  <div class="components-container">
    <div class="head-lavel">
      <div class="table-button">
        <Button v-if="username==='admin'" type="primary" icon="md-add" @click="addForm=true">新建</Button>
      </div>
      <div class="table-search">
      </div>
    </div>
    <Table border stripe :data="tableData" :columns="tablecolumns"></Table>
    <div style="margin: 10px;overflow: hidden">
      <div style="float: right;">
        <Page :total="tableCount" :current="1" show-total show-sizer
              @on-change="changePage" @on-page-size-change="changePagesize"></Page>
      </div>
    </div>
    
    <Modal v-model="addForm" title="新建" footer-hide>
      <add-group @DialogStatus="getDialogStatus"></add-group>
    </Modal>
    
    <Modal v-model="editForm" title="修改" footer-hide>
      <edit-group :ruleForm="ruleForm" @DialogStatus="getDialogStatus"></edit-group>
    </Modal>
    
    <Modal v-model="addWriteForm" title="白名单设置" footer-hide width="800">
      <Form ref="ruleForm" :model="ruleForm" :label-width="80">
        <FormItem label="值" prop="value">
          <Input type="textarea" :autosize="{minRows: 10,maxRows:20}" v-model="ruleForm.value"
                 placeholder="多个ip用着`,`分割，如 `127.0.0.1,128.0.0.1`">
          </Input>
          <a class="tips">Tip：多个ip用着`,`分割，如 `127.0.0.1,128.0.0.1`</a>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="submitForm('ruleForm')">提交</Button>
        </FormItem>
      </Form>
    </Modal>
  </div>
</template>
<script>
  import {getCdnsite, deleteCdnsite, getActionWhiteip, postActionWhiteip} from '@/api/greycdn'
  import addGroup from './components/addsite.vue'
  import editGroup from './components/editsite.vue'
  import {mapGetters} from 'vuex'
  
  export default {
    components: {
      addGroup, editGroup
    },
    data() {
      return {
        tableData: [],
        tableCount: 10,
        listQuery: {
          limit: 10,
          offset: 0,
          search: ''
        },
        addForm: false,
        editForm: false,
        addWriteForm: false,
        ruleForm: {}
      }
    },
    computed: {
      ...mapGetters([
        'role',
        'username'
      ]),
      tablecolumns() {
        let columns = [];
        columns.push({
          title: '名称',
          key: 'name'
        });
        columns.push({
          title: '备注',
          key: 'desc'
        });
        columns.push({
          title: '操作',
          key: 'action',
          align: 'center',
          render: (h, params) => {
            return h('div', [
              h('Button', {
                props: {
                  type: 'warning',
                  size: 'small',
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    const data = {
                      name: params.row.name
                    }
                    getActionWhiteip(data).then(res => {
                      this.addWriteForm = true
                      this.ruleForm.name = data.name
                      this.ruleForm.value = res.data
                    }).catch(error => {
                      console.log(error)
                      const errordata = JSON.stringify(error.response.data)
                      this.$Message.error(errordata);
                    })
                  }
                }
              }, '白名单'),
              h('Button', {
                props: {
                  type: 'success',
                  size: 'small',
                  disabled: this.username === 'admin' ? false : true
                },
                style: {
                  marginRight: '5px'
                },
                on: {
                  click: () => {
                    this.editForm = true
                    this.ruleForm = params.row
                  }
                }
              }, '修改'),
              h('Poptip', {
                props: {
                  title: '确定要删除吗！',
                  confirm: true,
                  transfer: true,
                  placement: 'top-end'
                },
                on: {
                  'on-ok': () => {
                    deleteCdnsite(params.row.id).then(res => {
                      this.fetchData()
                    })
                  },
                  'on-cancel': () => {
                    this.$Message.info('取消删除')
                  }
                }
              }, [
                h('Button', {
                  props: {
                    type: 'error',
                    size: 'small',
                    disabled: this.username === 'admin' ? false : true
                  }
                }, '删除')
              ]),
            ]);
          }
        });
        return columns;
      }
    },
    created() {
      this.fetchData()
    },
    methods: {
      fetchData() {
        getCdnsite(this.listQuery).then(res => {
          this.tableData = res.data.results
          this.tableCount = res.data.count
        })
      },
      fetchWhiteipData() {
      
      },
      getDialogStatus(data) {
        this.addForm = data
        this.editForm = data
        this.addWriteForm = data
        this.fetchData()
      },
      changePage(page) {
        this.listQuery.offset = (page - 1) * this.listQuery.limit
        this.fetchData()
      },
      changePagesize(size) {
        this.listQuery.limit = size
        this.fetchData()
      },
      submitForm(name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            postActionWhiteip(this.ruleForm).then(res => {
              this.$Message.success(res.data.response);
              this.addWriteForm = false
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

<style lang="less">

</style>
