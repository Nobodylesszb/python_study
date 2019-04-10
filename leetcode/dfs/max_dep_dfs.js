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