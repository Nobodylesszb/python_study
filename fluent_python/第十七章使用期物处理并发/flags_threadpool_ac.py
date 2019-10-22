from concurrent import futures

def dowanload_one():
    pass

def dowwnload_many(cc_list):
    list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(list):
            future = executor.submit()# 排定可调用对象的执行时间，然后返回一个期物，表示这个待执行的操作
            to_do.append(future) #储存这个期物，后面传给as_completed函数
            msg = 'scheduled for {}:{}'
            print(msg.format(cc,future))

        results = []
        for future in futures.as_completed(to_do): # 期物完成后产出期物
            res = future.result() #获得改期物的结果
            results.append(res)

    return len(results)
