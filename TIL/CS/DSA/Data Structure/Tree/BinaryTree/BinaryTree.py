# 1. Binary tree를 parent, left, right로 저장
def get_adj_mat():
    N = int(input())
    arr = list(map(int, input().split()))               # 값을 저장하는 배열
    parent = list(map(int, input().split()))            # 부모 노드의 index
    left = list(map(int, input().split()))              # 왼쪽 자식의 index
    right = list(map(int, input().split()))             # 오른쪽 자식의 index
    
# 2. 1차원 배열을 사용
# root : 1, root.left = 2, root.right = 3
# parent : n => left : 2 * n, right : 2 * n + 1
tree = [0, 1, 2, 3]

# 3. Linked List를 사용한 Binary tree
class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.parent = None

    def add_children(self, left_value=None, right_value=None):
        if left_value is not None:
            self.left = TreeNode(left_value)
            self.left.parent = self
        if right_value is not None:
            self.right = TreeNode(right_value)
            self.right.parent = self

    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.value, end=" ")
        if self.right is not None:
            self.right.inorder_traversal()


root = TreeNode(0)
root.add_children(1, 2)
root.left.add_children(3, 4)
root.right.add_children(5, 6)
root.inorder_traversal()
