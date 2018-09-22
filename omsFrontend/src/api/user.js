import axios from '@/libs/api.request'
import apiUrl from '@/config'

// users
export function postUser(data) {
  return axios.request({
    url: apiUrl.users,
    method: 'post',
    data
  })
}

export function getUser(query) {
  return axios.request({
    url: apiUrl.users,
    method: 'get',
    params: query
  })
}

export function patchUser(id, data) {
  return axios.request({
    url: apiUrl.users + id + '/',
    method: 'patch',
    data
  })
}

export function deleteUser(id) {
  return axios.request({
    url: apiUrl.users + id + '/',
    method: 'delete'
  })
}

// roles
export function postRole(data) {
  return axios.request({
    url: apiUrl.roles,
    method: 'post',
    data
  })
}

export function getRole(query) {
  return axios.request({
    url: apiUrl.roles,
    method: 'get',
    params: query
  })
}

export function putRole(id, data) {
  return axios.request({
    url: apiUrl.roles + id + '/',
    method: 'put',
    data
  })
}

export function deleteRole(id) {
  return axios.request({
    url: apiUrl.roles + id + '/',
    method: 'delete'
  })
}
