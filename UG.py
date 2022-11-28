class Node:
    def __init__(self,data):
        self._data = data
 
class Tree:
    def __init__(self,head):
        self._head = head
        self._children = []
        self._parent = None

     #menambahkan child
    def addChild(self, parent,data):
        self._children.append(data)
        print(self._children)
        self._parent = parent
    
    #def
    #mendapatkan isi elemen
    def operator(self):
        return self._children
 
    #mendapatkan node parent
    def parent(self):
        return self._parent
 
    #mendapatkan node children
    def children(self):
        return self._children
 
    #mengecek apakah node merupakan root
    def isRoot(self):
        return self._parent is None
 
    #mengecek apakah node merupakan external/leaf
    def isExternal(self):
        return len(self._children) == 0
 
def preorder(node):
    print(node.operator(), end = ' ')
    for i in node.children():
        preorder(i)
 
def postorder(node):
    for i in node.children():
        postorder(i)
    print(node.operator(), end = ' ')
 
 
 
# child daftar ke parent
if __name__ =='__main__':
    val300 = Node(300)
    t = Tree(val300) #Level 0
 
    #Level 1 parent 120
    val9 = t.addChild(val300, 9) 
    val1 = t.addChild(val300, 1)
 
    #Level 2 parent 9
    val11 = t.addChild(val9, 11) 
    val99 = t.addChild(val9, 99) 
 
    #Level 2 parent 1
    val17 = t.addChild(val1, 17) 
 
    #Level 3 parent 11
    val28 = t.addChild(val11, 28) 
    val72 = t.addChild(val11, 72)
 
    #Level 3 parent 99
    val90 = t.addChild(val99, 90) 
    val33 = t.addChild(val99, 33)
 
    #Level 3 parent 17
    val17 = t.addChild(val17, 2)
    val17 = t.addChild(val17, 4)
    val17 = t.addChild(val17, 43)
 
    # No 2. #
    #print(f'Sisa hasil pengurangan dari node {val300.data} adalah {t.minus(val300)}')
 
    # No 3. #
    #print(f'Total nilai dari semua saudara pada node {val90.data} adalah {t.sibling(val90)}')
print(val11._children)
#print(val17)
#print("=== Preorder ===")
#preorder(val300)
#print()
#print("=== Postorder ===")
#postorder(val300)