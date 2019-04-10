
//this code is bfs
const maxDepth = root =>{
    if(!root) return 0;
    let depth = 0;
    const queue = [];
    queue.push({depth,root})
    while (queue.length>0){
        const item = queue.shift();
        const currentDepth = item.depth
        root = item.root;
        depth = Math.max(depth,currentDepth)
        if (root){
            queue.push({depth:currentDepth+1,root:root.left});
            queue.push({depth: currentDepth + 1, root: root.right})
        }
    }
    return depth;

}