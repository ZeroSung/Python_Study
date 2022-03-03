from bst import BST

if __name__ == "__main__":
    t = BST() 
    t.put(500,'apple')
    t.put(600,'banana')
    t.put(200,'melon')
    t.put(100,'orange')
    t.put(400,'lime')
    t.put(250,'kiwi')
    t.put(150,'grape')
    t.put(800,'peach')
    t.put(700,'cherry')
    t.put(50,'pear')
    t.put(350,'lemon')
    t.put(10,'plum')
    
    print('전위순회:\t',end='')
    t.preorder(t.root)
    print('\n중위순회:\t',end='')
    t.inorder(t.root)
    print('\n250:\t',t.get(250))
    t.delete(200)
    print('200 삭제 후:')
    print('전위순회:\t',end='')
    t.preorder(t.root)
    print('\n중위순회:\t',end='')
    t.inorder(t.root)
    
    