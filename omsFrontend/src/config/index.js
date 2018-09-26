export default {
  /**
   * @description token在Cookie中存储的天数，默认1天
   */
  cookieExpires: 1,
  /**
   * @description 是否使用国际化，默认为false
   *              如果不使用，则需要在路由中给需要在菜单中展示的路由设置meta: {title: 'xxx'}
   *              用来在菜单中显示文字
   */
  useI18n: true,
  /**
   * @description api请求基础路径
   */
  baseUrl: {
    dev: 'http://127.0.0.1:8000',
    pro: 'https://produce.com'
  },

  // 表格数据
  LIMIT: 10,
  pagesize: [10, 20, 50, 100],
  pageformat: 'total, prev, pager, next, sizes',

  // 本地上传到服务器
  uploadurl: '/api/fileupload/',

  // 登录
  login: '/api/api-token-auth/',
  // logout: '/api/logout/',
  changePassword: '/api/changepasswd/',

  // 用户
  users: '/api/users/',
  groups: '/api/groups/',
  roles: '/api/roles/',

  // tools
  uploads: '/api/upload/',
  sendmail: '/api/sendmail/',
  sendmessage: '/api/sendmessage/',

  // dns
  dnsapis: '/api/dnsapikeys/',
  dnstypes: '/api/dnstypes/',
  dnsdomains: '/api/dnsdomains/',
  dnsrecords: '/api/dnsrecords/',
  godaddydomains: `/api/godaddydomains/`
}
