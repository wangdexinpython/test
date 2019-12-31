# -*- coding: utf-8 -*-
import re
from lxml import etree
import html
ss = '''&lt;p&gt;来源：央视财经&lt;/p&gt;&lt;p&gt;在美国对中国加征关税之后，目前第一艘被征收新关税的中国货船已经正式到达美国港口。&lt;/p&gt;&lt;p&gt;对于更加高昂的关税，到底是谁在买单呢？分析师认为，从货船上的橡胶轮胎到牙线棒，都会给美国家庭带来额外的支出。&lt;/p&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/RS35kr4Iup5zB7&quot; img_width&#x3D;&quot;734&quot; img_height&#x3D;&quot;400&quot; alt&#x3D;&quot;美加征关税后，中国第一艘货轮抵港！关税高昂，商品涨价，到底谁在买单？&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p&gt;上图这艘船，是美国最近对中国加征关税之后，第一艘抵达美国的货运船只，上面运载着轮胎、电视机和家具等货物。&lt;/p&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/RS37ESrHI9Hlel&quot; img_width&#x3D;&quot;731&quot; img_height&#x3D;&quot;399&quot; alt&#x3D;&quot;美加征关税后，中国第一艘货轮抵港！关税高昂，商品涨价，到底谁在买单？&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p&gt;货物被转移到卡车上，之后卖给美国消费者。对于更加高昂的关税，到底是谁在买单呢？&lt;/p&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/RS37ET512K3P3l&quot; img_width&#x3D;&quot;489&quot; img_height&#x3D;&quot;270&quot; alt&#x3D;&quot;美加征关税后，中国第一艘货轮抵港！关税高昂，商品涨价，到底谁在买单？&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p&gt;CNBC记者简·威尔逊：这里是一个例子。在那艘船上，装载着7.2万包在中国制造的牙线棒。在关税加征之前，每包售价42美分，而现在每包超过48美分。这艘船上仅牙线棒比之前就高了4000美元（约2.7万人民币）。&lt;/p&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/RS37Ebj7Y2aINn&quot; img_width&#x3D;&quot;731&quot; img_height&#x3D;&quot;397&quot; alt&#x3D;&quot;美加征关税后，中国第一艘货轮抵港！关税高昂，商品涨价，到底谁在买单？&quot; inline&#x3D;&quot;0&quot;&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/RS37Ec0IlAiDsb&quot; img_width&#x3D;&quot;475&quot; img_height&#x3D;&quot;267&quot; alt&#x3D;&quot;美加征关税后，中国第一艘货轮抵港！关税高昂，商品涨价，到底谁在买单？&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p&gt;美国加利福尼亚长滩港口执行董事 马里奥·科德罗：举个例子，美国的鞋类服装产业将每天面临近400亿美元的损失。&lt;/p&gt;&lt;p&gt;美国经济分析师史蒂文·费雷尔表示，关税的提高，会增加美国和中国企业的压力，而美国公司需要支付的成本并不少。&lt;/p&gt;&lt;img src&#x3D;&quot;http://p1.pstatp.com/large/pgc-image/RS37EcDAm41zo5&quot; img_width&#x3D;&quot;727&quot; img_height&#x3D;&quot;401&quot; alt&#x3D;&quot;美加征关税后，中国第一艘货轮抵港！关税高昂，商品涨价，到底谁在买单？&quot; inline&#x3D;&quot;0&quot;&gt;&lt;p&gt;美国经济分析师 史蒂文·费雷尔：特朗普总统说美国的进口商们只用承担新增关税中的4个百分点，而中国方面要承担21个百分点。根据我的判断，事实恰好相反。&lt;/p&gt;&lt;p&gt;纽约联储的经济学家预测，今年之内，关税的变化会让每户美国家庭平均多花800美元（约5520元人民币）。&lt;/p&gt;&lt;p&gt;但大部分的成本不是因为关税本身，而是美国企业用于调整供应链的新花销。&lt;/p&gt;'''
print('s1',ss)
select = etree.HTML(ss)
conss = select.xpath("//text()")[0]
pattern = re.compile(r'<[^>]+>', re.S).sub('', conss)

# re.compile()

# result = pattern.sub('', conss)
print('len',len(conss))
print(conss)
# print(result)
s=html.unescape(ss)
print('ss2222',s)

www = '</p><p>'
w = html.unescape(www)
print('w',w)

print('0000000000002')
ff='</p>jsf<p>'
rs = re.sub(r'<.*?>','',ff)
print('rs',rs)


