# 使用栈,可以使用列表模拟
def print_links(links):
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print (stack.pop())

# 使用递归

def print_links_recursivion(links):
    if links:
        print_links_recursivion(links.next)
        print (links.val)