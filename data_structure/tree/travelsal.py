def print_to_postorder(preorder, inorder) :
    root = preorder[0]
    root_index = inorder.index(root)
    if root_index != 0 :
        print_to_postorder(preorder[1:root_index+1],inorder[0:root_index])
    if root_index != len(inorder)-1 :
        print_to_postorder(preorder[root_index+1:],inorder[root_index+1:])
    print(root,'',end='')
    
N = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))
print_to_postorder(preorder,inorder)

    