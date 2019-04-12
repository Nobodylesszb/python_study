### 解释
- 当我们在一个循环中定义一个函数，并且在函数体中用了循环中的变量时，这个函数只会绑定这个变量本身，并不会绑定当前变量循环到的值。所以最终所有在循环中定义的函数都会使用循环变量最后的值做计算。

- 如果你想实现心中想的那种效果，可以把循环变量当做一个参数传递进函数体。**为什么这样可以呢？**因为这样在函数作用域内会重新定义一个变量，不是循环里面的那个变量了。
```python
funcs = []
for x in range(7):
    def some_func(x=x):
        return x
    funcs.append(some_func)
```

```python
funcs = []
for x in range(7):
    def some_func(x=x):
        return x
    funcs.append(some_func)
```
- output
``` python
>>> funcs_results = [func() for func in funcs]
>>> funcs_results
[0, 1, 2, 3, 4, 5, 6]
```


