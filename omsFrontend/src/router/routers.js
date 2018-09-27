import Main from '@/view/main'

/**
 * iview-admin中meta除了原生参数外可配置的参数:
 * meta: {
 *  hideInMenu: (false) 设为true后在左侧菜单不会显示该页面选项
 *  notCache: (false) 设为true后页面不会缓存
 *  access: (null) 可访问该页面的权限数组，当前路由设置的权限会影响子路由
 *  icon: (-) 该页面在左侧菜单、面包屑和标签导航处显示的图标，如果是自定义图标，需要在图标名称前加下划线'_'
 * }
 */

export default [
  {
    path: '/login',
    name: 'login',
    meta: {title: 'Login - 登录', hideInMenu: true},
    component: () => import('@/view/login/login.vue')
  },
  {
    path: '/', name: '_home', redirect: '/home', component: Main, meta: {hideInMenu: true, notCache: true},
    children: [
      {
        path: '/home',
        name: 'home',
        meta: {hideInMenu: true, title: '首页', notCache: true},
        component: () => import('@/view/home')
      }
    ]
  },
  {
    path: '/system', name: 'system', meta: {icon: 'logo-buffer', title: '系统管理'}, component: Main,
    children: [
      {
        path: 'users',
        name: 'users',
        meta: {icon: 'md-bonfire', title: '用户管理'},
        component: () => import('@/view/system/users.vue')
      },
      {
        path: 'roles',
        name: 'roles',
        meta: {icon: 'md-bonfire', title: '角色管理'},
        component: () => import('@/view/system/roles.vue')
      }
    ]
  },
  {
    path: '/dnsmanagers', name: 'dnsmanagers', meta: {icon: 'logo-buffer', title: '域名管理'}, component: Main,
    children: [
      {
        path: 'dnsapis',
        name: 'dnsapis',
        meta: {icon: 'md-bonfire', title: '域名api'},
        component: () => import('@/view/dnsmanagers/dnsapis.vue')
      },
      {
        path: 'dnsdomains',
        name: 'dnsdomains',
        meta: {icon: 'md-bonfire', title: '域名列表'},
        component: () => import('@/view/dnsmanagers/dnsdomains.vue')
      },
    ]
  },
  {path: '/401', name: 'error_401', meta: {hideInMenu: true}, component: () => import('@/view/error-page/401.vue')},
  {path: '/500', name: 'error_500', meta: {hideInMenu: true}, component: () => import('@/view/error-page/500.vue')},
  {path: '*', name: 'error_404', meta: {hideInMenu: true}, component: () => import('@/view/error-page/404.vue')}
]
