<template>
  <div class="components-container">
    <div class="head-lavel">
      <div class="table-button">
      </div>
      <div class="table-search">
        <Input
          placeholder="搜索 ..."
          v-model="listQuery.search"
          @keyup.enter.native="searchClick">
          <Icon type="ios-search" slot="suffix" @click="searchClick"/>
        </Input>
      </div>
    </div>
    <Table border stripe :data="tableData" :columns="tablecolumns"></Table>
    <div style="margin: 10px;overflow: hidden">
      <div style="float: right;">
        <Page :total="tableCount" :current="1" show-total show-sizer
              @on-change="changePage" @on-page-size-change="changePagesize"></Page>
      </div>
    </div>
  </div>
</template>
<script>
  import {getWhiteip} from '@/api/firewall'

  export default {
    data() {
      return {
        tableData: [],
        tableCount: 10,
        tablecolumns: [
          {
            title: '站点',
            key: 'vhost'
          },
          {
            title: '修改值',
            key: 'value'
          },
          {
            title: '操作',
            key: 'action'
          },
          {
            title: '操作时间',
            key: 'create_time'
          }
        ],
        listQuery: {
          limit: 10,
          offset: 0,
          search: ''
        },
        addForm: false,
        editForm: false,
        ruleForm: {}
      }
    },
    created() {
      this.fetchData()
    },
    methods: {
      fetchData() {
        getWhiteip(this.listQuery).then(res => {
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
      }
    }
  }
</script>

<style lang="less">

</style>
