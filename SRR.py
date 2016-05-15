# -*- encoding:utf-8 -*-
#2016年5月7日
# 实现线性优先调度策略（SRR）

#进程类
class MyProgress:
    def __init__(self,creation_time,level,sever_time):
        self.creation_time = int(creation_time)
        self.level = int(level)
        self.sever_time = int(sever_time)

if __name__ == "__main__":
    a = 2
    b = 1
    ready_list = []
    serve_list = []
    t = 1
    flag = True
    # 新创建进程就绪队列
    p = MyProgress(t,0,0)
    ready_list.append(p)
    # 享受服务队列中进程
    p = MyProgress(t,0,t)
    serve_list.append(p)
    count = 1
    while flag:
        if count > 20:
            break
        count = count + 1

        t = t + 1
        #计算队列中进程的优先级别
        for p in ready_list:
            p.level = a * (t - p.creation_time)
        for p in serve_list:
            p.level = a * (p.sever_time - p.creation_time) + b * (t - p.sever_time)
        #判断，如果等待队列的第一个进程优先级别大于服务队列最后一个优先级别
        #将等待队列的第一个进程转入服务队列
        if (serve_list[-1].level < ready_list[0].level):
            ready_list[0].sever_time = t
            serve_list.append(ready_list.pop(0))

        if (len(ready_list) == 0):
            p = MyProgress(t, 0, t)
            ready_list.append(p)
        #模拟创建时刻
        if (t%5 == 0):
            p = MyProgress(t,0,t)
            ready_list.append(p)


    print '#'*3, u"就绪队列",'#'*3
    for p in ready_list:
        print p.level
    print '#'* 3, u"服务队列",'#'*3
    for p in serve_list:
        print p.level,(p.sever_time-p.creation_time)
