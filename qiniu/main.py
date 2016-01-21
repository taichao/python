# coding: utf-8
# zhangtaichao
import config.param as param
from qiniu import Auth, PersistentFop, build_op, op_save

key_src= '赤壁赋第一讲赏读.mp4'

q = Auth(param.AccessKey,param.SecretKey)

pfop = PersistentFop(q,param.bucket,param.pipeline)
#op = op_save('avthumb/m3u8/segtime/10/vcodec/libx264/s/320x240', saved_bucket, saved_key)
#op = op_save('avthumb/m3u8/segtime/10/vcodec/libx264/s/320x240')

ops = {
    'r':24,
    'vb':'56k'
}
op = build_op('avthumb','flv',**ops)
ops = []
ops.append(op)
ret, info = pfop.execute(key_src, ops, 1)
print(info)
assert ret['persistentId'] is not None
