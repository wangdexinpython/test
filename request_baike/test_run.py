# -*- coding: utf-8 -*-
import sys
sys.path.append("../../")
if __name__ == '__main__':
    info = sys.argv[1]
    len_split_info = len(info.split('_'))
    split_info = info.split('_')
    if len_split_info == 2:
        task_type = split_info[0]
        jobtype = split_info[1]
        Blasckwidow(task_type=task_type, jobtype=jobtype, page_type="all", run_type="dmp")
    elif len_split_info > 2:
        #qingdao_five8app_fang_sell_seeds
        city = split_info[0]
        channel = split_info[1]
        task_type = split_info[2]
        type = split_info[3]
        jobtype = split_info[4]
        Blasckwidow(channel=channel, city=city, task_type=task_type, type=type, jobtype=jobtype, page_type="all",
                    run_type="dmp")