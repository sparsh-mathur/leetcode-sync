/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findBottomLeftValue = function(root) {
    const dq = [root]
    let node = null
    while(dq.length){
        node = dq.shift()
        if (node.right){
            dq.push(node.right)
        }
        if (node.left){
            dq.push(node.left)
        }
    }
    return node.val
    
};