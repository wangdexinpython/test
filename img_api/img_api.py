



import re
def img_qiniu(url):
    qiniuurl = 'http://py.yuedusikao.com:8081/?url={}'.format(url)
    return qiniuurl

def local_content_img(content):
    imgs = re.findall('<img.*?src="(.*?)"', content)
    for img in imgs:
        local_img = img_qiniu(img)
        if local_img != "error":
            content = content.replace(img, local_img)
        else:
            pass
    return content