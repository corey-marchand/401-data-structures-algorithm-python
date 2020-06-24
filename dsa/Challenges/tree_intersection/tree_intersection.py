def tree_intersection(binarytree1, binarytree2):
    t1 = []
    t2 = []

    while 1:
        if binarytree1:
            t1.append(binarytree1)
            binarytree1 = binarytree1.left

        elif binarytree2:
            t2.append(binarytree2)
            binarytree2 = binarytree2.left

        elif len(t1) != 0 and len(t2) != 0:
            binarytree1 = t1[-1]
            binarytree2 = t2[-1]

            if binarytree1.key == binarytree2.key:
                t1.pop(-1)
                t2.pop(-1)

                binarytree1 = binarytree1.right
                binarytree2 = binarytree2.right

            elif binarytree1.key < binarytree2.key:
                t1.pop(-1)
                binarytree1 = binarytree1.right
                binarytree2 = None

            elif binarytree1.key > binarytree2.key:
                t2.pop(-1)
                binarytree2 = binarytree2.right
                binarytree1 = None

        else:
            print("No values")
