import axios from '@/libs/api.request'

export function getTableData(params) {
  return axios.request({
    url: 'get_table_data',
    method: 'get',
    params: params
  })
}

export function getDragList(params) {
  return axios.request({
    url: 'get_drag_list',
    method: 'get',
    params: params
  })
}
