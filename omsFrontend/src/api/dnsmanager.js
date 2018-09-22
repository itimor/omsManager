import axios from '@/libs/api.request'
import apiUrl from '@/config'

// dnsdomains
export function postDnsDomain(data) {
  return axios.request({
    url: apiUrl.dnsdomains,
    method: 'post',
    data
  })
}

export function getDnsDomain(query) {
  return axios.request({
    url: apiUrl.dnsdomains,
    method: 'get',
    params: query
  })
}

export function putDnsDomain(id, data) {
  return axios.request({
    url: apiUrl.dnsdomains + id + '/',
    method: 'patch',
    data
  })
}

export function deleteDnsDomain(id) {
  return axios.request({
    url: apiUrl.dnsdomains + id + '/',
    method: 'delete'
  })
}
