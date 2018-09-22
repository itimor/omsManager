const getters = {
  token: state => state.user.token,
  username: state => state.user.username,
  roles: state => state.user.roles,
  avatar: state => state.user.avatar,
}
export default getters
