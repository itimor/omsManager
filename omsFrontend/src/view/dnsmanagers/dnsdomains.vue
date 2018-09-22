<template>
  <div>
    <Table :data="tableData" :columns="tablecolumns" stripe></Table>
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
        },
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
        }).catch(error => {
          const errordata = JSON.stringify(error.response.data)
          this.$Message.error(errordata);
        })
      },
      changePage(page) {
        this.listQuery.offset = page - 1
        this.fetchData()
      },
      changePagesize(size) {
        this.listQuery.limit = size
        this.fetchData()
      }
    }
  }
</script>
