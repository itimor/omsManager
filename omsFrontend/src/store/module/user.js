import {login, logout} from '@/api/login'
import {getUser} from '@/api/user'
import {setUsername, getUsername, setToken, getToken} from '@/libs/util'

export default {
  state: {
    username: getUsername(),
    avatorImgPath: '',
    token: getToken(),
    roles: '',
    access: ''
  },
  mutations: {
    setAvator(state, avatorPath) {
      state.avatorImgPath = avatorPath
    },
    setUsername(state, username) {
      state.username = username
      setUsername(username)
    },
    setAccess(state, access) {
      state.access = access
    },
    setToken(state, token) {
      state.token = token
      setToken(token)
    }
  },
  actions: {
    // 登录
    handleLogin({commit}, {username, password}) {
      username = username.trim()
      return new Promise((resolve, reject) => {
        login({
          username,
          password
        }).then(res => {
          const data = res.data
          commit('setUsername', username)
          commit('setToken', data.token)
          resolve()
        }).catch(err => {
          reject(err)
        })
      })
    },
    // 退出登录
    handleLogOut({state, commit}) {
      return new Promise((resolve, reject) => {
        // logout().then(() => {
        //   commit('setToken', '')
        //   commit('setAccess', [])
        //   resolve()
        // }).catch(err => {
        //   reject(err)
        // })
        // 如果你的退出登录无需请求接口，则可以直接使用下面三行代码而无需使用logout调用接口
        commit('setToken', '')
        commit('setAccess', [])
        resolve()
      })
    },
    // 获取用户相关信息
    getUserInfo({state, commit}) {
      return new Promise((resolve, reject) => {
        const userinfo = {
          username: state.username
        }
        getUser(userinfo).then(res => {
          const data = res.data[0]
          commit('setAvator', data.avator)
          commit('setUsername', data.username)
          commit('setAccess', data.access)
          resolve(data)
        }).catch(err => {
          reject(err)
        })
      })
    }
  }
}
