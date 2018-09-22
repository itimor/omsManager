<template>
  <div>
    <Table :data="tableData" :columns="tablecolumns" stripe></Table>
    <div style="margin: 10px;overflow: hidden">
      <div style="float: right;">
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
        tableCount: 1,
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
      }
    },
    created() {
      this.fetchData()
    },
    methods: {
      fetchData() {
        getDnsDomain().then(res => {
          this.tableData = res.data
        }).catch(error => {
          const errordata = JSON.stringify(error.response.data)
          this.$Message.error(errordata);
        })
      }
    }
  }
</script>
