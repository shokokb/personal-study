class BinaryTree:
    @staticmethod
    def mydepth(tree):
        d = 0
        l = len(tree)
        while d < l:
            if (2 ** d - 1 > l):

                break
            d += 1
        return d

if __name__ == "__main__":
    tree = [2, 3, 4, 5, 1, 7]
    d = BinaryTree.mydepth(tree)
    print(d)