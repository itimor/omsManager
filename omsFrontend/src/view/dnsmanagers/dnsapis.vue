<template>
  <div class="components-container">
    <div class="head-lavel">
      <div class="table-button">
        <Button type="primary" icon="md-add" @click="addForm=true">新建</Button>
        <Button type="success" v-show="sync" :loading="sync" style="margin-left: 10px">同步中</Button>
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
  </div>
</template>
<script>
  import {getDnsApi, deleteDnsApi, PostGodaddyDomain, PostNamesiloDomain} from '@/api/dnsmanager'
  import addGroup from './components/adddnstapi.vue'
  import editGroup from './components/editdnsapi.vue'
  import {mapGetters} from 'vuex'

  export default {
    components: {
      addGroup, editGroup
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
            title: 'key',
            key: 'key'
          },
          {
            title: '类型',
            key: 'type'
          },
          {
            title: '操作',
            key: 'action',
            align: 'center',
            render: (h, params) => {
              return h('div', [
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
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small',
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.dnsQuery.dnsname = params.row.name
                      this.dnsQuery.type = params.row.type
                      this.syncDomwin()
                    }
                  }
                }, '同步'),
                h('Poptip', {
                  props: {
                    title: '确定要删除吗！',
                    confirm: true,
                    transfer: true,
                    placement: 'top-end'
                  },
                  on: {
                    'on-ok': () => {
                      deleteDnsApi(params.row.id).then(res => {
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
                      disabled: this.roles.indexOf('admin') > -1 ? false : true
                    }
                  }, '删除')
                ]),
              ]);
            }
          }
        ],
        sync: false,
        listQuery: {
          limit: 10,
          offset: 0,
          search: ''
        },
        addForm: false,
        editForm: false,
        ruleForm: {},
        dnsQuery: {
          dnsname: '',
          type: ''
        }
      }
    },
    created() {
      this.fetchData()
    },
    computed: {
      ...mapGetters([
        'roles'
      ]),
    },
    methods: {
      fetchData() {
        getDnsApi(this.listQuery).then(res => {
          this.tableData = res.data.results
          this.tableCount = res.data.count
        })
      },
      getDialogStatus(data) {
        this.addForm = data
        this.editForm = data
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
      },
      syncDomwin() {
        this.$Message.info('正在同步中，请稍后')
        this.sync = true
        if (this.dnsQuery.type === 'godaddy') {
          PostGodaddyDomain(this.dnsQuery).then(() => {
            this.sync = false
          }).catch(error => {
            const errordata = JSON.stringify(error.response.data)
            this.$Message.error(errordata);
          })
        } else if (this.dnsQuery.type === 'namesilo') {
          PostNamesiloDomain(this.dnsQuery).then(() => {
            this.sync = false
          }).catch(error => {
            const errordata = JSON.stringify(error.response.data)
            this.$Message.error(errordata);
          })
        }

      }
    }
  }
</script>

<style lang="less">

</style>
