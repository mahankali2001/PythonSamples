import queue

class treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class solution:
    def levelorderorbfs(self, root):
        # Create a queue
        q = queue.Queue()

        q.put(root)
        while not q.empty():
            node = q.get()
            print(node.value, end="-> ")
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        print("None")
    
    def levelorderorbfsgroups(self, root):
        # Create a queue
        q = queue.Queue()
        result = []
        q.put(root)
        while not q.empty():
            level = []
            for i in range(q.qsize()):
                node = q.get()
                level.append(node.value)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            result.append(level)
        print(result)
    
    def dfs(self, root):
        st = []
        st.append(root)
        while len(st) !=0 :
            node = st.pop()
            print(node.value, end = " -> ")
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        print(None)

if __name__ == "__main__":
    root = treenode(60)
    node1 = treenode(30)
    node2 = treenode(70)
    root.left = node1
    root.right = node2
    node3 = treenode(20)
    node4 = treenode(50)
    node1.left = node3
    node1.right = node4
    node5 = treenode(65)
    node6 = treenode(80)
    node2.left = node5
    node2.right = node6
    s = solution()
    s.levelorderorbfs(root)

    s.levelorderorbfsgroups(root)

    s.dfs(root)

