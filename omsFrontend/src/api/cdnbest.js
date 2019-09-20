import axios from '@/libs/api.request'
import apiUrl from '@/config'

// cdnsites
export function postCdnsite(data) {
  return axios.request({
    url: apiUrl.cdnbestsites,
    method: 'post',
    data
  })
}

export function getCdnsite(query) {
  return axios.request({
    url: apiUrl.cdnbestsites,
    method: 'get',
    params: query
  })
}

export function putCdnsite(id, data) {
  return axios.request({
    url: apiUrl.cdnbestsites + id + '/',
    method: 'put',
    data
  })
}

export function deleteCdnsite(id) {
  return axios.request({
    url: apiUrl.cdnbestsites + id + '/',
    method: 'delete'
  })
}

// whiteips
export function getWhiteip(query) {
  return axios.request({
    url: apiUrl.cdnbestwhiteips,
    method: 'get',
    params: query
  })
}

// actionwhiteip
export function postActionWhiteip(data) {
  return axios.request({
    url: apiUrl.actioncdnbest,
    method: 'post',
    data
  })
}

export function getActionWhiteip(query) {
  return axios.request({
    url: apiUrl.actioncdnbest,
    method: 'get',
    params: query
  })
}

