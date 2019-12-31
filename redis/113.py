import redis,pyssdb

class Par(object):
    def __init__():
        c = pyssdb.Client('127.0.0.1', 8992)
        pool = redis.ConnectionPool(host='127.0.0.1', port=8990, db=2,
                                    password='28JCi*289V92ofj2owoBkv8282928SKVISmv8920565LjhMcs')
        r = redis.Redis(connection_pool=pool)
    def parse():
        url = r.lpop('query_seeds')
        c.qpush_front('query_seeds',url)
    def run():
        while True:
            parse()
if __name__ == '__main__':
    pa = Par()
    pa.run()