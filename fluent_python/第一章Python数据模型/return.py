#@func:为了测试return的用法
def test():
    for  i in range(10):
        print(i)
        if i/3 ==0:
            print('————————')
            return 


if __name__ == "__main__":
    test()