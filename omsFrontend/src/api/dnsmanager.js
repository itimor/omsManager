import axios from '@/libs/api.request'
import apiUrl from '@/config'

// dnsapis
export function postDnsApi(data) {
  return axios.request({
    url: apiUrl.dnsapis,
    method: 'post',
    data
  })
}

export function getDnsApi(query) {
  return axios.request({
    url: apiUrl.dnsapis,
    method: 'get',
    params: query
  })
}

export function putDnsApi(id, data) {
  return axios.request({
    url: apiUrl.dnsapis + id + '/',
    method: 'put',
    data
  })
}

export function deleteDnsApi(id) {
  return axios.request({
    url: apiUrl.dnsapis + id + '/',
    method: 'delete'
  })
}

// dnsdomains
export function getDnsDomain(query) {
  return axios.request({
    url: apiUrl.dnsdomains,
    method: 'get',
    params: query
  })
}

// dnstypes
export function postDnsType(data) {
  return axios.request({
    url: apiUrl.dnstypes,
    method: 'post',
    data
  })
}

export function getDnsType(query) {
  return axios.request({
    url: apiUrl.dnstypes,
    method: 'get',
    params: query
  })
}

export function putDnsType(id, data) {
  return axios.request({
    url: apiUrl.dnstypes + id + '/',
    method: 'put',
    data
  })
}

export function deleteDnsType(id) {
  return axios.request({
    url: apiUrl.dnstypes + id + '/',
    method: 'delete'
  })
}

// dnsrecords
export function postDnsRecord(data) {
  return axios.request({
    url: apiUrl.dnsrecords,
    method: 'post',
    data
  })
}

export function getDnsRecord(query) {
  return axios.request({
    url: apiUrl.dnsrecords,
    method: 'get',
    params: query
  })
}

export function putDnsRecord(id, data) {
  return axios.request({
    url: apiUrl.dnsrecords + id + '/',
    method: 'put',
    data
  })
}

export function deleteDnsRecord(id) {
  return axios.request({
    url: apiUrl.dnsrecords + id + '/',
    method: 'delete'
  })
}
