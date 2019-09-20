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

    <Modal v-model="showWriteForm" title="白名单ips" footer-hide width="800">
        <Input type="textarea" :autosize="true" v-model="value" disabled>
      </Input>
    </Modal>
  </div>
</template>
<script>
  import {getWhiteip} from '@/api/greycdn'

  export default {
    data() {
      return {
        tableData: [],
        tableCount: 10,
        tablecolumns: [
          {
            title: '站点',
            key: 'name'
          },
          {
            title: '修改值',
            key: 'value',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'success',
                    size: 'small',
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.showWriteForm = true
                      this.value = params.row.value
                    }
                  }
                }, '查看')
              ])
            }
          },
          {
            title: '操作',
            key: 'action'
          },
          {
            title: '操作用户',
            key: 'create_user'
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
        showWriteForm: false,
        value: ''
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
