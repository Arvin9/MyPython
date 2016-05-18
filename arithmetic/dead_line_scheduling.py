# -*- encoding:utf-8 -*-
#模拟时限调度算法

#进程类
class MyProgress:
    def __init__(self,name,happen_time,execute_time,over_time):
        #事件名称
        self.name = name
        #发生时限
        self.happen_time = happen_time
        #执行时限
        self.execute_time = execute_time
        #结束时限
        self.over_time = int(over_time)


def f(a, b):
    return a.over_time - b.over_time

if __name__ == "__main__":
    #模拟生产
    progress_list = []
    progress_list.append(MyProgress('DA1', 0, 15, 30))
    progress_list.append(MyProgress('DA2', 30, 15, 60))
    progress_list.append(MyProgress('DA3', 60, 15, 90))
    progress_list.append(MyProgress('DB1', 0, 38, 75))
    progress_list.append(MyProgress('DB2', 75, 15, 150))
    progress_list.append(MyProgress('DB3', 150, 15, 225))
    list_tmp = sorted(progress_list,cmp=f)

    print '*'*5+'调度顺序'+'*'*5
    for i in list_tmp:
        print "进程"+str(i.name)+"发生时限"+str(i.happen_time)+"执行时限"+str(i.execute_time)+"结束时限"+str(i.over_time)


