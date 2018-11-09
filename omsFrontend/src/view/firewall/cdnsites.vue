<template>
  <div class="components-container">
    <div class="head-lavel">
      <div class="table-button">
        <Button type="primary" icon="md-add" @click="addForm=true">新建</Button>
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

    <Modal v-model="addWriteForm" :title="`${vhost}-白名单设置`" footer-hide>
      <add-whiteip :ruleForm="ruleForm" @DialogStatus="getDialogStatus"></add-whiteip>
    </Modal>
  </div>
</template>
<script>
  import {getCdnsite, deleteCdnsite, getActionWhiteip} from '@/api/firewall'
  import addGroup from './components/addsite.vue'
  import editGroup from './components/editsite.vue'
  import addWhiteip from './components/addwhiteip.vue'

  export default {
    components: {
      addGroup, editGroup, addWhiteip
    },
    data() {
      return {
        tableData: [],
        tableCount: 10,
        tablecolumns: [
          {
            title: '名称',
            key: 'name'
          },
          {
            title: '备注',
            key: 'desc'
          },
          {
            title: '操作',
            key: 'action',
            align: 'center',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'warning',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.addWriteForm = true
                      this.vhost = params.row.name
                      this.fetchWhiteipData()
                    }
                  }
                }, '白名单'),
                h('Button', {
                  props: {
                    type: 'success',
                    size: 'small'
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
                    }
                  }, '删除')
                ]),
              ]);
            }
          }
        ],
        listQuery: {
          limit: 10,
          offset: 0,
          search: ''
        },
        addForm: false,
        editForm: false,
        addWriteForm: false,
        ruleForm: {},
        vhost: ''
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
        const params = {
          vhost: this.vhost
        }
        getActionWhiteip(params).then(res => {
          this.ruleForm = res.data[0]
          this.ruleForm['vhost'] = this.vhost
          this.ruleForm['action'] = res.data.length
        }).catch(error => {
          console.log(error)
          const errordata = JSON.stringify(error.response.data)
          this.$Message.error(errordata);
        })
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
      searchClick() {
        this.fetchData()
      }
    }
  }
</script>

<style lang="less">

</style>
