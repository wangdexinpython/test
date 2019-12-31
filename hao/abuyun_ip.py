#! -*- encoding:utf-8 -*-
import requests
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"
proxyUser = "HK7PDG1295J2407D"
proxyPass = "A0D7F8443FA69296"
targetUrl = "http://test.abuyun.com"
proxyMeta = "https://%(user)s:%(pass)s@%(host)s:%(port)s" % {
  "host" : proxyHost,
  "port" : proxyPort,
  "user" : proxyUser,
  "pass" : proxyPass,
}
proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}
resp = requests.get(targetUrl, proxies=proxies)
print (resp.status_code)
print (resp.text)