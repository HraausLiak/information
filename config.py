from redis import StrictRedis
import logging


class Config(object):
    """项目配置信息"""

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information18"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis项目配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 10

    # flask_session配置信息
    SECRET_KEY = "AJDICE2CHDJ3UjfcGhd"
    # 指定session保存到redis中
    SESSION_TPYE = 'redis'
    # 让cookie中的session_id 被加密签名处理
    SESSION_USE_SIGNER = True
    # 使用redis实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_HOST, db=REDIS_DB)
    # session的有效期,单位是秒
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(Config):
    """开发者模式下的配置"""
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


# 定义配置字典
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
