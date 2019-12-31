# ##
# # You should look at the following URL's in order to grasp a solid understanding
# # of Nginx configuration files in order to fully unleash the power of Nginx.
# # http://wiki.nginx.org/Pitfalls
# # http://wiki.nginx.org/QuickStart
# # http://wiki.nginx.org/Configuration
# #
# # Generally, you will want to move this file somewhere, and start with a clean
# # file but keep this around for reference. Or just disable in sites-enabled.
# #
# # Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
# ##
#
# # Default server configuration
# #
#
# server
# {
#     listen
# 80;
# server_name
# popdailys.com
# www.popdailys.com;
# # 这一步是http重定向到https，也可以不写
# rewrite ^ (.*)$ https: // ${server_name}$1
# permanent;
# location / {
#     root / home / daily_pops / templates / article;
# index
# index.html
# index.htm;
# }
#
# location / static / {
#     alias / home / daily_pops / templates / static /;
# }
#
#
# location / xml / {
#     alias / home / daily_pops / templates / xml /;
# index
# popdaliys.xml;
# }
# error_page
# 500
# 502
# 503
# 504 / 50
# x.html;
# location = / 50
# x.html
# {
#     root / usr / share / nginx / html;
# }
#
# }
#
#
#
# server
# {
#     listen
# 443;
# server_name
# popdailys.com
# www.popdailys.com;
#
# ssl
# on;
# ssl_certificate
# full_chain.pem;
# ssl_certificate_key
# private.key;
# ssl_session_timeout
# 5
# m;
# ssl_ciphers
# ECDHE - RSA - AES128 - GCM - SHA256: ECDHE:ECDH: AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
# ssl_protocols
# TLSv1
# TLSv1
# .1
# TLSv1
# .2;
# ssl_prefer_server_ciphers
# on;
# gzip
# on;
# gzip_min_length
# 1
# k;
# gzip_buffers
# 4
# 16
# k;
# gzip_comp_level
# 3;
# gzip_types
# text / plain
# text / css
# application / xml
# application / javascript
# application / x - javascript
# text / javascript;
# types
# {
#     text / html
# html
# htm
# shtml;
# text / css
# css;
# text / xml
# xml;
# image / gif
# gif;
# image / jpeg
# jpeg
# jpg;
# application / javascript
# js;
# application / atom + xml
# atom;
# application / rss + xml
# rss;
# }
# location / {
#     root / home / daily_pops / templates / article;
# index
# index.html
# index.htm;
# }
#
# location / static / {
#     alias / home / daily_pops / templates / static /;
# }
#
#
# location / xml / {
#     alias / home / daily_pops / templates / xml /;
# index
# popdaliys.xml;
# }
# error_page
# 500
# 502
# 503
# 504 / 50
# x.html;
# location = / 50
# x.html
# {
#     root / usr / share / nginx / html;
# }
#
# }
