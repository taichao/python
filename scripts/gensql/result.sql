CREATE TABLE IF NOT EXISTS sh_shop (
    shop_id int(11) NOT NULL  AUTO_INCREMENT  COMMENT  '商户主键',
    phone varchar(11) NOT NULL COMMENT  '商户手机号，主号，登陆，唯一',
    other_phone varchar(16) NULL COMMENT  '其他联系方式，',
    shop_name varchar(32) NOT NULL COMMENT  '商户名称',
    shop_linkman varchar(32) NOT NULL COMMENT  '商户联系人',
    shop_linkman_head varchar(128) NULL COMMENT  '联系人头像',
    passwd varchar(32) NOT NULL COMMENT  '商户密码MD5加密',
    status int(11) NOT NULL COMMENT  '商户状态，0：正常，1：禁用',
    create_time datetime NOT NULL COMMENT  '创建时间',
    update_time datetime NOT NULL COMMENT  '修改时间',
    primary key(shop_id)
)
ENGINE = InnoDB
COMMENT '商户表';

CREATE TABLE IF NOT EXISTS sh_shop_card (
    shop_id int(11) NOT NULL COMMENT  '商户主键',
    shop_card_num varchar(20) NOT NULL COMMENT  '商户借记卡账号',
    shop_card_bank varchar(30) NOT NULL COMMENT  '借记卡开户行',
    shop_card_user varchar(20) NOT NULL COMMENT  '商户借记卡开户行',
    status int(11) NOT NULL COMMENT  '当前状态，0：提交，1：审核中，2：信息不符或者其他原因审核不通过，3：通过，4：已更换，此卡是商户之前使用过的银行卡',
    create_time datetime NOT NULL COMMENT  '创建时间',
    update_time datetime NOT NULL COMMENT  '最后状态更新时间',
    create_ip varchar(20) NOT NULL COMMENT  '操作人当前IP地址',
    spam_time datetime NULL COMMENT  '审核通过时间',
    spam_admin int(11) NULL COMMENT  '审核管理员',
    spam_idea varchar(64) NULL COMMENT  '审核不通过时，添加审核提示语言，告知商户如何修改'
    ,primary key(shop_id)
)
ENGINE = InnoDB
COMMENT '商户当前绑定银行卡';

CREATE TABLE IF NOT EXISTS sh_shop_channel (
    shop_channel_id int(11) NOT NULL  AUTO_INCREMENT COMMENT  '商户渠道ID,自增',
    shop_id int(11) NOT NULL COMMENT  '商户ID',
    shop_qrcode_url varchar(128) NOT NULL COMMENT  '商户二维码图片地址',
    shop_channel_name varchar(64) NOT NULL COMMENT  '商户渠道名称',
    shop_channel_desc text NOT NULL COMMENT  '商户渠道描述',
    create_time datetime NOT NULL COMMENT  '渠道创建时间',
    update_time datetime NOT NULL COMMENT  '渠道修改时间',
    status int(11) NOT NULL COMMENT  '当前状态，0：正常，1：已经删除'
    ,primary key(shop_channel_id)
)
ENGINE = InnoDB
COMMENT '商户渠道';

CREATE TABLE IF NOT EXISTS sh_shop_collect (
    shop_id int(11) NOT NULL COMMENT  '商户ID',
    scan_qr int(11) NOT NULL COMMENT  '累计扫码数',
    download int(11) NOT NULL COMMENT  '累计下载量',
    reg int(11) NOT NULL COMMENT  '累计注册量',
    buy int(11) NOT NULL COMMENT  '累计消费金额',
    pay int(11) NOT NULL COMMENT  '累计充值金额',
    collect double NOT NULL COMMENT  '总收益',
    withdraw double NOT NULL COMMENT  '可提现金额',
    collect_yestoday double NOT NULL COMMENT  '昨日收益',
    create_time datetime NOT NULL COMMENT  '数据最后更新时间'
    ,primary key(shop_id)
)
ENGINE = InnoDB
COMMENT '商户累计总表';

CREATE TABLE IF NOT EXISTS sh_shop_income (
    shop_id int(11) NOT NULL COMMENT  '商户ID',
    scan_qr int(11) NOT NULL COMMENT  '扫码数',
    download int(11) NOT NULL COMMENT  '下载数',
    reg int(11) NOT NULL COMMENT  '注册数',
    buy int(11) NOT NULL COMMENT  '购买金额',
    pay int(11) NOT NULL COMMENT  '充值金额',
    income double NOT NULL COMMENT  '当日总收益',
    income_desc text NOT NULL COMMENT  '收入计算公式',
    create_time datetime NOT NULL COMMENT  '数据生成时间'
    ,primary key(shop_id)
)
ENGINE = InnoDB
COMMENT '商户收益';


CREATE TABLE IF NOT EXISTS sh_shop_withdraw (
    shop_id int(11) NOT NULL COMMENT  '商户ID',
    shop_card_num varchar(20) NOT NULL COMMENT  '商户借记卡账号',
    money double NOT NULL COMMENT  '提现金额',
    status int(11) NOT NULL COMMENT  '提现状态，0:提交，1:已接受，2:已打款，2：问题提现',
    `show` int(11) NOT NULL COMMENT  '客户端是否删除，0：不删除，1：删除，',
    create_time datetime NOT NULL COMMENT  '提现记录提交时间',
    admin_id int(11) NULL COMMENT  '打款人ID',
    problem text NULL COMMENT  '打款中，出现不能打款的问题描述',
    update_time datetime NULL COMMENT  '提现成功时的记录'
    ,primary key(shop_id)
)
ENGINE = InnoDB
COMMENT '商户提现';



