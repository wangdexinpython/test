# -*- coding: utf-8 -*-
#redis
def dmpRedisConfig(environment):
    config = {}
    if environment == 'windows':
        config['host'] = '127.0.0.1'
        config['port'] = 6379
        config['passwd'] = ''
        config['url'] = ""
    elif environment == 'linux':
        config['host'] = ''
        config['port'] = 6379
        config['passwd'] = ''
    return config