import axios from '@/libs/api.request'
import apiUrl from '@/config'

// cdnsites
export function postCdnsite(data) {
  return axios.request({
    url: apiUrl.cdnsites,
    method: 'post',
    data
  })
}

export function getCdnsite(query) {
  return axios.request({
    url: apiUrl.cdnsites,
    method: 'get',
    params: query
  })
}

export function putCdnsite(id, data) {
  return axios.request({
    url: apiUrl.cdnsites + id + '/',
    method: 'put',
    data
  })
}

export function deleteCdnsite(id) {
  return axios.request({
    url: apiUrl.cdnsites + id + '/',
    method: 'delete'
  })
}

// whiteips
export function getWhiteip(query) {
  return axios.request({
    url: apiUrl.whiteips,
    method: 'get',
    params: query
  })
}

// actionwhiteip
export function postActionWhiteip(data) {
  return axios.request({
    url: apiUrl.actionwhiteip,
    method: 'post',
    data
  })
}

export function getActionWhiteip(query) {
  return axios.request({
    url: apiUrl.actionwhiteip,
    method: 'get',
    params: query
  })
}

