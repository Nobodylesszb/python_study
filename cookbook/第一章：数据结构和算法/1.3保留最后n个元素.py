from collections import deque
"""
使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
当新的元素加入并且这个队列已满的时候， 
最老的元素会自动被移除掉。
"""


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines  # 生成器
        previous_lines.append(line)


if __name__ == "__main__":
    with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
