# 问题
# 怎样在一个序列上面保持元素顺序的同时消除重复的值？

# 解决方案
# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题。比如：

def deque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# 这个方法仅仅在序列中元素为 hashable 的时候才管用。 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话，你需要将上述代码稍微改变一下，就像这样：
