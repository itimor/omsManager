# -*- coding: utf-8 -*-
# author: timor
# desc:

import qiniu
from qiniu import Auth
from qiniu import BucketManager
import requests
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

qiniu_key = {
    "ACCESS_KEY": "Bd1KeZHbjcpdhQxVF9OPpQukrvcoZ1w9QYbTbKKb",
    "SECRET_KEY": "fadmf-jv6Z4gGguvjpWo9VwAj3xET4eE_OTBhwt-"
}

bucket_name = "game"
bucket_domain = 'www.staticsources.com'

q = Auth(qiniu_key["ACCESS_KEY"], qiniu_key["SECRET_KEY"])
bucket = BucketManager(q)
basedir = os.path.realpath(os.path.dirname(__file__))
charset = "utf8"
mime_type = "text/plain"


# 解析结果
def parseRet(retData, respInfo):
    if retData != None:
        print(retData["key"] + " Upload file success!")
        print("Hash: " + retData["hash"])

        # 检查扩展参数
        for k, v in retData.items():
            if k[:2] == "x:":
                print(k + ":" + v)

        # 检查其他参数
        for k, v in retData.items():
            if k[:2] == "x:" or k == "hash" or k == "key":
                continue
            else:
                print(k + ":" + str(v))
    else:
        print(retData)
        print("Error: " + respInfo.text_body)


def list_all(bucket_name, bucket=None, prefix=None, limit=10000):
    rlist=[]
    if bucket is None:
        bucket = BucketManager(q)
    marker = None
    eof = False
    while eof is False:
        ret, eof, info = bucket.list(bucket_name, prefix=prefix, marker=marker, limit=limit)
        marker = ret.get('marker', None)
        for item in ret['items']:
            rlist.append(item["key"])
    if eof is not True:
        # 错误处理
        pass
    return rlist


def upload_file(key, localfile):
    print("upload_file:")
    print(key)
    token = q.upload_token(bucket_name, key)
    params = {'x:a': 'a'}
    progress_handler = lambda progress, total: progress
    ret, info = qiniu.put_file(token, key, localfile, params, mime_type, progress_handler=progress_handler)
    parseRet(ret, info)


def down_file(key, basedir="", is_private=1, expires=3600):
    url = 'http://{}/{}'.format(bucket_domain, key)
    print(url)
    if is_private:
        url = q.private_download_url(url, expires=expires)

    c = requests.get(url, verify=False)
    fpath=key.replace("/", os.sep)
    savepath = os.path.join(basedir, fpath)
    dir_ = os.path.dirname(savepath)
    if not os.path.isdir(dir_):
        os.makedirs(dir_)
    elif os.path.isfile(savepath):
        pass

    with open(savepath, "wb") as code:
        code.write(c.content)


def down_all(prefix=""):
    n = 0
    for key in list_all(bucket_name, bucket, prefix=prefix):
        try:
            down_file(key, basedir=basedir)
            print("{} down: {}".format(n, key))
        except:
            pass
        n = n + 1


def main():
    # list_all(bucket_name)
    down_all()


if __name__ == "__main__":
    print(main())
