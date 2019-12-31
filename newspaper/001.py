from newspaper import Article
url = 'https://baike.baidu.com/item/%E6%AC%A7%E6%B4%B2%E7%90%86%E4%BA%8B%E4%BC%9A%E4%B8%BB%E5%B8%AD/3898141?fromtitle=%E6%AC%A7%E7%9B%9F%E6%80%BB%E7%BB%9F&fromid=3400995'
# url = 'https://news.google.com/articles/CBMiP2h0dHBzOi8vd3d3LnNub3Blcy5jb20vZmFjdC1jaGVjay9pdmFua2EtdHJ1bXAtdm90aW5nLW1hY2hpbmVzL9IBAA?hl=en-US&gl=US&ceid=US%3Aen'
news = Article(url, language='cn')
news.download()  #先下载h
news.parse()    #再解析
print('++++++++++++++++++++',news.text) #新闻正文
print(news.text) #新闻正文
print(news.text.replace('\n','<br>')) #新闻正文

# print(news.title) #新闻标题
# print(news.html)   #未修改的原始HTML
# print(news.authors)  #新闻作者
# print(news.top_image) #本文的“最佳图像”的URLf
# print(news.movies)  #本文电影url
# print(news.keywords) #新闻关键词
# print(news.summary)   #从文章主体txt中生成的摘要
# print(news.images) #本文中的所有图像url