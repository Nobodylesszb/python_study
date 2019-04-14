### bfs and dfs

[知乎解释](https://zhuanlan.zhihu.com/p/50187643)

####  栈和队列

- 说到DFS, 和 BFS ，我们先简单的复习一下数据结构的知识，我画了个简单的对比图

  ![img](https://pic3.zhimg.com/80/v2-42c30cdce1e2c2c77a5bec557fff4086_hd.jpg)

  

  > 队列是先进先出（FIFO, First-In-First-Out）的线性表，只允许在后端（称为*rear*）进行插入操作，在前端（称为*front*）进行删除操作。

  我把队列理解成水管的结构，先流进来的水总是先流出。

  > 栈是限定仅在表头进行插入和删除操作的线性表

  我把栈理解成球桶的结构，后放进来的球总是先取出。

  #### BFS

  **广度优先搜索算法**：（Breadth-First-Search，缩写为BFS），是一种图形搜索算法。简单的说，BFS是从根节点开始，沿着树的宽度遍历树的节点。如果所有节点均被访问，则算法中止。

  实现方法：

  1. 首先将根节点放入队列中。
  2. 从队列中取出第一个节点，并检验它是否已是当前分支最远叶子节点。
  3. 如果找到目标，则结束搜索并回传结果。
  4. 否则将它所有尚未检验过的直接子节点加入队列中。
  5. 若队列为空，表示整张图都检查过了

  结合上述题目，大概流程图如下：

  ![img](https://pic4.zhimg.com/80/v2-03f23a9cf2e7e256b571b11e28e55097_hd.jpg)

  

  ![img](https://pic4.zhimg.com/80/v2-155a6c9e77611c953e58cbc435d47a8f_hd.jpg)

  



利用队列先进先出的特性，可以优先遍历横向节点。代码实现如下

- ```js
  const maxDepth = root => {
      if (!root) return 0;
  
      let depth = 0;
      const queue = [];
  
      queue.push({ depth, root });
  
      while (queue.length > 0) {
          const item = queue.shift();
          const currentDepth = item.depth;
          root = item.root;
          depth = Math.max(depth, currentDepth);
  
          if (root) {
              queue.push({ depth: currentDepth + 1, root: root.left });
              queue.push({ depth: currentDepth + 1, root: root.right });
          }
      }
  
      return depth;
  };
  ```

#### DFS

- **深度优先搜索算法** ：（Depth-First-Search，DFS）是一种用于遍历或搜索树或图的算法。引入维基百科的定义：沿着树的深度遍历树的节点，尽可能深的搜索树的分支。当节点v的所在边都己被探寻过，搜索将回溯到发现节点v的那条边的起始节点。这一过程一直进行到已发现从源节点可达的所有节点为止。如果还存在未被发现的节点，则选择其中一个作为源节点并重复以上过程，整个进程反复进行直到所有节点都被访问为止。

  实现方法：

  1. 首先将根节点放入栈中。
  2. 从栈中取出最后一个节点，并检验它是否已是当前分支最远叶子节点。
  3. 如果找到目标，则结束搜索并回传结果。
  4. 否则将它所有尚未检验过的直接子节点加入栈中。
  5. 若栈为空，表示整张图都检查过了

结合上述题目，大概流程图如下：

- ![img](https://pic3.zhimg.com/80/v2-034e1959676e7e9a4d9f10eb91a16af2_hd.jpg)

![img](https://pic1.zhimg.com/80/v2-ea7a2992df18c0e455e76e97dd380f14_hd.jpg)

利用栈后进先出的特性，可以优先遍历纵向节点。代码实现如下

- ```js
  const maxDepth = root => {
      if (!root) return 0;
  
      let depth = 0;
      const stack = [];
      stack.push({ depth, root });
  
      while (stack.length > 0) {
          const item = stack.pop();
          const currentDepth = item.depth;
          root = item.root;
          depth = Math.max(depth, currentDepth);
  
          if (root) {
              stack.push({ depth: currentDepth + 1, root: root.left });
              stack.push({ depth: currentDepth + 1, root: root.right });
          }
      }
  
      return depth;
  
  };
  ```