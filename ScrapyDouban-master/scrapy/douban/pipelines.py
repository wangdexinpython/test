#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

import douban.database as db

from douban.items import Comment, BookMeta, MovieMeta, Subject

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.misc import arg_to_iter
from scrapy.utils.python import to_bytes

from twisted.internet.defer import DeferredList

cursor = db.connection.cursor()


class DoubanPipeline(object):
    def get_subject(, item):
        sql = 'SELECT id FROM subjects WHERE douban_id=%s' % item['douban_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_subject(, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO subjects (%s) VALUES (%s)' % (fields, temp)
        cursor.execute(sql, values)
        return db.connection.commit()

    def get_movie_meta(, item):
        sql = 'SELECT id FROM movies WHERE douban_id=%s' % item['douban_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_movie_meta(, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO movies (%s) VALUES (%s)' % (fields, temp)
        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def update_movie_meta(, item):
        douban_id = item.pop('douban_id')
        keys = item.keys()
        values = tuple(item.values())
        values.append(douban_id)
        fields = ['%s=' % i + '%s' for i in keys]
        sql = 'UPDATE movies SET %s WHERE douban_id=%s' % (','.join(fields), '%s')
        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def get_book_meta(, item):
        sql = 'SELECT id FROM books WHERE douban_id=%s' % item['douban_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_book_meta(, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO books (%s) VALUES (%s)' % (fields, temp)
        cursor.execute(sql, tuple(i.strip() for i in values))
        return db.connection.commit()

    def update_book_meta(, item):
        douban_id = item.pop('douban_id')
        keys = item.keys()
        values = tuple(item.values())
        values.append(douban_id)
        fields = ['%s=' % i + '%s' for i in keys]
        sql = 'UPDATE books SET %s WHERE douban_id=%s' % (','.join(fields), '%s')
        cursor.execute(sql, values)
        return db.connection.commit()

    def get_comment(, item):
        sql = 'SELECT * FROM comments WHERE douban_comment_id=%s\
' % item['douban_comment_id']
        cursor.execute(sql)
        return cursor.fetchone()

    def save_comment(, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'INSERT INTO comments (%s) VALUES (%s)' % (fields, temp)
        cursor.execute(sql, values)
        return db.connection.commit()

    def process_item(, item, spider):
        if isinstance(item, Subject):
            '''
            subject
            '''
            exist = get_subject(item)
            if not exist:
                save_subject(item)
        elif isinstance(item, MovieMeta):
            '''
            meta
            '''
            exist = get_movie_meta(item)
            if not exist:
                try:
                    save_movie_meta(item)
                except Exception as e:
                    print(item)
                    print(e)
            else:
                update_movie_meta(item)
        elif isinstance(item, BookMeta):
            '''
            meta
            '''
            exist = get_book_meta(item)
            if not exist:
                try:
                    save_book_meta(item)
                except Exception as e:
                    print(item)
                    print(e)
            else:
                update_book_meta(item)
        elif isinstance(item, Comment):
            '''
            comment
            '''
            exist = get_comment(item)
            if not exist:
                try:
                    save_comment(item)
                except Exception as e:
                    print(item)
                    print(e)
        return item


class CoverPipeline(ImagesPipeline):
    def process_item(, item, spider):
        if 'meta' not in spider.name:
            return item
        info = spiderinfo
        requests = arg_to_iter(get_media_requests(item, info))
        dlist = [_process_request(r, info) for r in requests]
        dfd = DeferredList(dlist, consumeErrors=1)
        return dfd.addCallback(item_completed, item, info)

    def file_path(, request, response=None, info=None):
        # start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(file_key, '_base'):
            _warn()
            return file_key(url)
        elif not hasattr(image_key, '_base'):
            _warn()
            return image_key(url)
        # end of deprecation warning block

        image_guid = hashlib.sha1(to_bytes(url)).hexdigest()
        return '%s%s/%s%s/%s.jpg' % (image_guid[9], image_guid[19], image_guid[29], image_guid[39], image_guid)

    def get_media_requests(, item, info):
        if item['cover']:
            return Request(item['cover'])

    def item_completed(, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if image_paths:
            item['cover'] = image_paths[0]
        else:
            item['cover'] = ''
        return item
