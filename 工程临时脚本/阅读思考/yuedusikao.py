# -*- coding: utf-8 -*-
# @Time : 2019/12/23 16:47
# @Author : EDZ
# @Email : wangdexin@haxitag.com
# @File : yuedusikao.py
# @Project : test
'''

'''
import re,json,time,requests
# data="""<div class="common-width content articleDetailContent kr-rich-text-wrapper"><p><span>文/姜菁玲</span></p><p><span>编辑/地中海蓝</span></p><p><span>36氪获悉，人工智能面试工具提供商<a href="http://www.deeprove.com/" target="_blank">滴孚科技</a>已于2019年11月完成Pre-A轮融资，金额三千万元，投资方为鸿仁资本。此前，滴孚科技曾获千万元天使投资及科大讯飞生态入股。</span><br/></p><p>上海滴孚人工智能科技有限公司（简称滴孚科技）成立于2017年3月，是一家“AI+招聘”领域的人工智能应用公司，旗下有“壹面”及“Hire bot”两款应用。</p><p>在传统的招聘流程里，中大型企业初面环节往往报名人数众多，HR需要进行简历筛选、预沟通并与候选人协商初面时间地点、逐一面试。整体消耗的时间、人力成本较高，且人工能处理的量也不大，效率较低。</p><p>壹面是一款人工智能工具，利用AI面试官替代传统面试官，在初面环节完成对候选人的预沟通信息采集、初面以及结果评估工作。<strong>通过AI面试的形式，候选人可随时随地进入面试，节约面试成本，提高企业初面工作效率及候选人到面率。</strong></p><h3><span>采用AI合成真人面试官，考察专业能力与基础素质</span></h3><p>从操作路径上，HR在ATS系统中调起壹面，向候选人批量发送面试通知。候选人收到面试邀请后，凭邀请码进入壹面APP进行人工智能面试。面试结束后，壹面后台将对候选人面试情况进行分析，输出并传送最终的报告至ATS系统中供HR筛选。</p><p>壹面整体面试环节约为15-20分钟，题型包括视频问答与AI测评两种，主要针对候选人专业能力与基础素质进行考察。</p><p>专业能力方面，围绕知识、技能、经验三个维度，结合简历与视频问答中提及的过往经历信息，进行文本提取、评估、输出分值。基础素质方面，针对候选人的胜任素质以及流体智力（即脑力），以视频问答交互与AI游戏测评的形式进行考察，最终输出分值与CEL特质分析报告。</p><p>视频问答总题量在3-5题，每题限时2分钟。其中，固定的3题为算法根据职位JD及候选人简历中过往经历进行智能推荐，剩余2题支持企业自定义。</p><p><img alt="36氪首发 | 人工智能面试工具「壹面」获三千万元Pre-A轮融资，投资方为鸿仁资本" src="http://img.yuedusikao.com/15760381082516BWbY9IVga.jpg" data-img-size-val="244,444" width="244"/></p><p class="img-desc">壹面视频问答</p><p><span>在面试过程中，为削弱求职者在面试过程中与机器交流的不适感，<strong>壹面利用AI真人合成、情感语音等技术生成真人形象AI面试官，可营造求职者与真人HR面试场景。</strong></span></p><p><span>面试结束后，系统将生成面试评估报告传送至ATS系统中，报告主要包括求职者基本信息、专业能力评分、胜任素质评分、职业风险评估等，各信息模块会生成可筛选的字段，HR可在ATS系统中快速筛选出符合要求的候选人。</span><br/></p><p><img alt="36氪首发 | 人工智能面试工具「壹面」获三千万元Pre-A轮融资，投资方为鸿仁资本" src="http://img.yuedusikao.com/1576038108599Zzskmth8do.jpg" data-img-size-val="545,482" width="545"/></p><p class="img-desc">壹面面试报告</p><p>据壹面产品负责人Irene介绍，在视频分析结果可信度上，壹面综合人机判断重合度为77%，前30%的候选人与后30%的候选人重合度达92%，判断结果较精准。<br/></p><p>在技术层面上，壹面依托股东方科大讯飞的NLP技术及讯飞AIUI平台，构建了基于面试场景的语义理解能力，<span>专注做垂直领域的技术研究</span><span>。</span></p><h3>与北森战略合作，已支持数十万人次面试量</h3><p>壹面创始人及CEO苏睿告诉36氪，壹面与北森已达成深度战略合作，双方在底层技术、产品服务、营销支持等层面上进行了深度对接。</p><p>在产品方面，壹面入驻北森生态版本应用后台，双方接口打通，客户可以在北森ATS中一键进入和使用壹面。营销支持层面，北森与壹面在公众号、CSM、弹窗等渠道进行了宣传合作。接下来，北森或将与壹面协同，共同优化壹面的用户体验和算法模型。</p><p><img alt="36氪首发 | 人工智能面试工具「壹面」获三千万元Pre-A轮融资，投资方为鸿仁资本" src="http://img.yuedusikao.com/1576038108954nUpXOsgGr7.jpg" data-img-size-val="720,386"/></p><p class="img-desc">北森产品应用后台</p><p>据了解，除北森之外，壹面已与科锐国际旗下“睿聘”实现产品对接，与SAP正在进行技术对接。通过北森及其他渠道，<span>壹面已合作中大型公司近百家，涉及金融、地产、汽车、制造业等多个行业，客户有上汽大众、捷信金融等，<strong>共已支持数十万人进行AI面试。</strong></span></p><h3><span><strong>团队和盈利方面</strong></span></h3><p>盈利模式上，壹面以系统订阅年费与个性化增值服务费为盈利点，系统订阅年费在6至8万，增值服务费在30万至100万不等，已初步实现收支平衡。</p><p><span>团队方面，滴孚科技目前团队规模为50人左右，大部分为产品与开发，总部位于上海。创始人及CEO苏睿曾在上汽集团任职十余年，为斑马网络联合创始人。</span><br/></p><p><strong>此轮融资之后，滴孚科技将进行产品升级与团队扩张</strong>，预计在12月份上线壹面3.0版本，在菜单定义、可视化定义、面试题型等方面继续提升。团队方面，半年之内预计增加至100人左右，主要增加研发与营销人员。</p></div>"""
url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1577100626936_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1577100626937%5E00_1903X550&sid=&word=范冰冰"

cons = requests.get(url).text
# print(cons)
img = re.findall(r'''"base64": '(data:image.*?)',''',cons)
print(len(img))
print(img)
# def content_html(html):
#     html=re.sub('div','p',html)
#     img_li = re.findall(r'''<img src="(.*?)".*?>''',html)
#     print("img",img_li)
#     for k in img_li:
#         img = """<img src="{}" width="720px" height="480px">""".format(k)
#         html=re.sub(r'''<img src="{}".*?>'''.format(k),img,html)
#     print(html)
#
# content_html(data)









