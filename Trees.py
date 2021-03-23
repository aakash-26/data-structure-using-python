"""
Create Tree structure using python

"""

class TreeNode:
    
    def __init__(self,data):
        
        self.data = data
        self.parent = None
        self.childs = []
        
    def add_childs(self,node_object):
        
        node_object.parent = self
        self.childs.append(node_object)

    def tree_height(self):
        h = 0
        p=self.parent
        
        while p:
            h += 1
            p = p.parent
            
        return h
        
    def print_tree(self):

        sp =" " * self.tree_height() * 3
        
        if self.parent:
            p = sp + "|---"
        else:
            p =""
        
        print(p + str(self.data))
        
        for children in self.childs:
            children.print_tree()
            
if __name__ == "__main__":
    
    root = TreeNode(10)
    one_node = TreeNode(1)
    
    root.add_childs(one_node)
    root.add_childs(TreeNode(2))
    root.add_childs(TreeNode(3))
    root.add_childs(TreeNode(4))
    
    ele_node = TreeNode(11)
    
    one_node.add_childs(ele_node)
    one_node.add_childs(TreeNode(21))
    
    ele_node.add_childs(TreeNode(100))
    
    new_node = TreeNode(5)
    root.add_childs(new_node)
    new_node.add_childs(TreeNode(6))
    
    root.print_tree()
        