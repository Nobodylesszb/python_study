funcs = []
results = []
for x in range(7):
    def some_func():
        return x
    funcs.append(some_func)
    results.append(some_func())  # note the function call here

funcs_results = [func() for func in funcs]
print(results)
"""
output:
[0, 1, 2, 3, 4, 5, 6]
"""
print(funcs_results)
"""
output:
[6, 6, 6, 6, 6, 6, 6]
"""