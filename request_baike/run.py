# -*- coding: utf-8 -*-
import sys,os,time

reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(os.path.dirname(__file__)+"/../../")
sys.path.append("../../")
class Blasckwidow():
    def __init__(, *args, **kwargs):
        # 获取参数
        channel = kwargs.get("channel")
        city = kwargs.get("city")
        type = kwargs.get("type")
        jobtype = kwargs.get("jobtype")  # 任务类型
        task_type = kwargs.get("task_type")  # 任务类型
        page_type = kwargs.get("page_type", "all")
        run_type = kwargs.get("run_type", "prod")  # 配置文件
        channel_son = kwargs.get("channel_son", "")
        run_date = kwargs.get("run_date", "")
        blackwidow_task = blackwidow_task

        # 获取规则
        blackwidow = __getBlackwidowRules__()
        blackwidow_task = blackwidow.get("blackwidow_task", {})

        # 获取setting
        settings = Settings()
        __setSetting__()

        # 注册中间件
        __setMiddlewares__()

        # 注册pip
        __setPipelines__()

        # 注册spider
        process = CrawlerProcess(settings)
        __setSpider__()
        # 启动爬虫
        process.start()
        print "--------------------------->  爬虫启动"
