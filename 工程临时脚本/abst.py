# -*- coding: utf-8 -*-
import requests,json
# def nlp_get_abstract_server(data):
#     data1 = {"text": data}
#     url1 = 'http://39.98.194.203:8100/new_abstract_sever'
#     try:
#         cons1 = requests.post(url1, data=data1).text
#         return cons1
#     except:
#         return json.dumps({})


def get_article_nlp_summary_data(content):
    nlp_url = 'http://39.98.194.203:8204'
    data = {
        'content': content
    }
    response = requests.post(url=nlp_url, data=data)
    print(response.text)
    if response.status_code != 200:
        return None
    return response.text[1:-1]


text = '''的是给他们培养数学力量，而不是数学家。数学家太苦了，并不被企业家所需要。中国科学院数学与系统科学研究院研究员李洪波张一甲：真正想做数学家的人对解决企业问题没有什么兴趣。数学有两种，一种是无用之学，一种是有用之学。在象牙塔最核心的，是纯数学家，他们不在乎是不是能被使用，可能他们觉得经世致用是很奇怪的词，这不在咱们今天的讨论范畴，本来跟工业界都没有很大关系。想问一下董老师，今年数学的学生出国的意愿下降，现在大家的就业意愿是什么样子？好像还说这一批临时决定不出国的人纷纷都走向了就业岗位、准备就业。董子静：最近这几年的确出国的比例在下降，今年可能受中美摩擦影响，不过再往前推两年，也的确是一个下降的趋势。现在去工作的这些同学，从前几年大量的涌向金融界，现在我感觉在人工智能、数字科学发展的一个社会时代的背景下，我觉得涌向这些行业的同学还在增多。张一甲：陈亮师兄都没有去数学院招聘过吧？陈亮：还没有招聘过。陈天石：我觉得我去了北大数学院，也没有人来。宣晓华：培养的学生还是不够多，北大有很多大学生都出国了，要是没出国的话，可能他会读研究生。我们本身也需要博士生的。终极使命“在华尔街，对近三十年来对工业产生最大影响的是把数学方法引入了金融。”——广策信息创始人、CEO 陈亮“基础学科人所被培训出来的、被浸泡出来的独特素养，是真正重要的。”——北京大学数学科学学院党委副书记董子静张一甲：我觉得这个论坛的聊法不像科技论坛的聊法，非常发散，非常自由，也非常学院派。上次我遇到陈大岳（北京大学数学科学学院院长）院长，我问了一个问题：作为一个院长，你最大的核心KPI是什么？我以为他会回答科研成果之类的，但他说最终极的使命是维护数院这片土壤的平静，第二使命给享有不同自由选择的人以不同自由选择的权利。我觉得这个说的特别好，如果我们这个议题发生在数院，有一拨人根本不感兴趣，有一拨人可能会跟我们聊的很开心，这就是一个真实的状况。我确实觉得这是一个很好的事情，至少让学院里面最想要跟工业走近的人和对学术抱有一腔热血的人，有一个沟通的桥梁，面对基础科学跟工业的关系，不知道各位有什么心得想法，每个人用2分钟的时间做一个总结。张海霞：其实我最大的感悟还是这个词：i CAN。为什么我这么说？因为这个活动做了13年，最重要的把学术界的学生跟企业界结合起来，让学生能够对这个社会有所了解，通过他所的创新有更好的一个结合点，其实就是想推动这个事，我感觉到特别开心在过去这些年里，不管是数学、物理、化学这些基础学科，还是计算机等等这些应用学科的同学变化都非常大，因为他们真的是更想用自己的技术去创新、去帮助，找到更多的点为这个社会服务。跟过去的不太一样，过去的学生想的更多的是如何找到工作，现在学生更多是想如何用我的创新创造为这个社会服务，在这一点，基础学科、应用学科都在逐渐跟社会挂钩挂的更紧，我相信这一点也会发展的更好，这是我最大的心得体会，所以我相信iCAN。陈天石：我最大的感悟就是我们现在培养了很多基础科学的人才，但是我们好像不需要那么多科学家，我完全同意您的观点。我以前在中科大的校友中呼吁，中科大不要变成“中国物理大学”，招了很多基础科学的学生，但最后注定大部分人都不会成为以这个为职业的科学家。所以我想，大家应该可以有更加多元化的价值观，鼓励大家做各种各样的事情，包括成为数学家或者赚很多的钱，再比如说做一个工程师，我觉得都挺好的。宣晓华：目前在企业里面，从总体来说，我们最想招的人就是数学好的，同时又喜欢算法的，从这个角度来说，这样的人才现在是远远不够的，这样的人才，不光在中国还是美国，我们现在看到很多非常年轻的人，刚毕业工资很高，原因是对这样人才的需求很大，提供的还不够大。所以我希望学校能更多培养这样的人才。从行业角度来说提供了非常好的舞台，对数学来说，现在这个时代非常好，因为这些数学家既可以研究本身数学理论，也就是我感兴趣的研究数学内部的一些问题，这是数学家是非常好的时代。陈亮：数学家对金融以及'''

abs = get_article_nlp_summary_data(text)
print("abs",abs)









