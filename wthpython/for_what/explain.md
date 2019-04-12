#### 解释
- 来看上面的例子，enumerate(some_string)这个函数会在每次迭代的时候产生两个值，分别是i(一个从0开始的索引值)和一个字符（来自some_string的值）。然后这两个值会分别赋值给i和some_dict[i]。把刚才的循环展开来看就像是下面这样：
- ``` >>> i, some_dict[i] = (0, 'c')
>>> i, some_dict[i] = (1, 'r')
>>> i, some_dict[i] = (2, 'a')
>>> i, some_dict[i] = (3, 'z')
>>> i, some_dict[i] = (4, 'y')
>>> some_dict
```
- 