class Node:
    def __init__(self) -> None:
        self.val  # store value
        self.next  # next address


class solution(Node):
    def preorderTraversal(self, root: Node):  # preorder
        nodelist_pre = []

        def traverse(root):
            if root:
                nodelist_pre.append(root.val)
                traverse(root=root.left)
                traverse(root=root.right)
            return nodelist_pre

        return traverse(root=root)

    def inorderTraversal(self, root: Node):  # inorder
        nodelist_in = []

        def traverse(root):
            if root:
                traverse(root=root.left)
                nodelist_in.append(root.val)
                traverse(root=root.right)
            return nodelist_in

        return traverse(root=root)

    def postorderTraversal(self, root: Node):  # postorder
        nodelist_post = []

        def traverse(root):
            if root:
                traverse(root=root.left)
                traverse(root=root.right)
                nodelist_post.append(root.val)
            return nodelist_post

        return traverse(root=root)


def main(args=None):
    pass


if __name__ == "__main__":
    pass
