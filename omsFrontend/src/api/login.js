import axios from '@/libs/api.request'
import apiURL from '@/config'

export const login = (data) => {
  console.log(apiURL.login)
  return axios.request({
    url: apiURL.login,
    method: 'post',
    data
  })
}

export const logout = () => {
  return axios.request({
    url: apiURL.logout,
    method: 'get'
  })
}

export const changePassword = (data) => {
  console.log(data)
  return axios.request({
    url: apiURL.changePassword,
    method: 'post',
    data
  })
}
