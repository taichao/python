# coding: utf-8
__author__ = 'zhangtaichao'


from qiniu import Auth
from qiniu import put_file
from config import param

import qiniu.config

access_key = param.AccessKey
secret_key = param.SecretKey
bucket_name = param.bucket

print(__file__)


q = Auth(access_key, secret_key)

mime_type = "application/octet-stream"
params = {'x:a': 'a'}
localfile = '/Users/zhangtaichao/Downloads/赤壁赋第一讲赏读.mp4'
localfile = '/Users/zhangtaichao/code/python/qiniu/upload.py'

key = 'upload.py'
token = q.upload_token(bucket_name, key)

progress_handler = lambda progress, total: progress
ret, info = put_file(token, key, localfile, params, mime_type, progress_handler=progress_handler)
print(info)
assert ret['key'] == key
