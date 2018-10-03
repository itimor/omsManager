# domainManager

# 开发环境
## 后端

```bash
cd omsBackend
python manage.py runserver
```

## 前端
```bash
cd omsFrontend
npm run dev
```

# 打包上线
```bash
cd omsFrontend
npm run build

systemctl restart oms
```
