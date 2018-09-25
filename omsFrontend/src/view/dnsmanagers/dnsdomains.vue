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
  import {getDnsDomain} from '@/api/dnsmanager'

  export default {
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
            title: '状态',
            key: 'status'
          },
          {
            title: '域名服务商',
            key: 'type'
          }
        ],
        listQuery: {
          limit: 10,
          offset: 0,
          search: ''
        }
      }
    },
    created() {
      this.fetchData()
    },
    methods: {
      fetchData() {
        getDnsDomain(this.listQuery).then(res => {
          this.tableData = res.data.results
          this.tableCount = res.data.count
        })
      },
      changePage(page) {
        this.listQuery.offset = page - 1
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
