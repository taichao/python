# coding: utf-8
# zhangtaichao
import config.param as param
from qiniu import Auth, PersistentFop, build_op, op_save

key_src= 'o_1a4v9o1qpk9l19766sp1nor13cvb.mp4'

q = Auth(param.AccessKey,param.SecretKey)

pfop = PersistentFop(q,param.bucket,param.pipeline)
#op = op_save('avthumb/m3u8/segtime/10/vcodec/libx264/s/320x240', saved_bucket, saved_key)
#op = op_save('avthumb/m3u8/segtime/10/vcodec/libx264/s/320x240')

ops = {
    'segtime':10,
}
op = build_op('avthumb','m3u8',**ops)
ops = []
ops.append(op)
ret, info = pfop.execute(key_src, ops, 1)
print(info)
assert ret['persistentId'] is not None
