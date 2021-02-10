class User:
    pass


user1 = User()


user1


type(user1)


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created correctlyget_ipython().getoutput("')")


user1 = User('Eva', 'Eva Gonz', 'ava@gon.com')
user2 = User('john', 'John Doe', 'john@doe.com')


user2.email
user1.name


user2.name


user2.email, user2.username
user1.email, user1.name


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))

    def goodbye(self, guest_name):
        print("Goo bye {}, have a nice day.".format(guest_name))    


user3 = User('Dani', 'Dani H', 'danih@doe.com')


user3.introduce_yourself('Gabriel')


user3.goodbye('Dana')


User.introduce_yourself(user3, 'David')
User.goodbye(user2,'Gab')

# es decir, que self es igual a User


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()


user4 = User('jane', 'Jane Doe', 'jane@doe.com')


user4








class UserDatabase:
    def insert(self, user):
        pass
    
    def find(self, username):
        pass
    
    def update(self, user):
        pass
        
    def list_all(self):
        pass


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')


users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]


biraj.username, biraj.email, biraj.name


print(aakash)


users


'biraj' < 'hemanth'


class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users


database = UserDatabase()


database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)


user = database.find('siddhant')
user


database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))


user = database.find('siddhant')
user


database.list_all()


database.insert(biraj)


database.list_all()











get_ipython().run_cell_magic("time", "", """for i in range(100000000):
    j = i*i""")


get_ipython().getoutput("pip install jovian --upgrade --quiet")


import jovian


jovian.commit(project='python-binary-search-trees')


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)


node0


node0.key


node0.left = node1
node0.right = node2


tree = node0


tree.key


tree.left.key


tree.right.key








tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))


tree2


tree2.key


tree2.left.key, tree2.right.key


tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key


tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key


def tree_to_tuple(node):
    pass





def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)    


display_keys(tree2, '  ')








def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))


tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))


display_keys(tree, '  ')


traverse_in_order(tree)


jovian.commit()


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


tree_height(tree)


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)



tree_size(tree)


class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node


tree_tuple


tree = TreeNode.parse_tuple(tree_tuple)


tree


tree.display_keys('  ')


tree.height()


tree.size()


tree.traverse_in_order()


tree.to_tuple()











def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key


tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))


is_bst(tree1)


tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))


is_bst(tree2)








class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# Level 0
tree = BSTNode(jadhesh.username, jadhesh)


# View Level 0
tree.key, tree.value


# Level 1
tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)


# View Level 1
tree.left.key, tree.left.value, tree.right.key, tree.right.value








display_keys(tree)


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


tree = insert(None, jadhesh.username, jadhesh)


insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)


display_keys(tree)


tree2 = insert(None, aakash.username, aakash)
insert(tree2, biraj.username, biraj)
insert(tree2, hemanth.username, hemanth)
insert(tree2, jadhesh.username, jadhesh)
insert(tree2, siddhant.username, siddhant)
insert(tree2, sonaksh.username, sonaksh)
insert(tree2, vishal.username, vishal)


display_keys(tree2)


tree_height(tree2)








def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


node = find(tree, 'hemanth')


node.key, node.value








def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))


node = find(tree, 'hemanth')
node.value








def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


list_all(tree)


import jovian


jovian.commit()


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height


is_balanced(tree)


is_balanced(tree2)








def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root
    


data = [(user.username, user) for user in users]
data


tree = make_balanced_bst(data)


display_keys(tree)


tree3 = None
for username, user in data:
    tree3 = insert(tree3, username, user)











def balance_bst(node):
    return make_balanced_bst(list_all(node))


tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)


display_keys(tree1)


tree2 = balance_bst(tree1)


display_keys(tree2)


import math

math.log(100000000, 2)


get_ipython().run_cell_magic("time", "", """for i in range(26):
    j = i*i""")


get_ipython().run_cell_magic("time", "", """for i in range(100000000):
    j = i*i""")


class TreeMap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)


users


treemap = TreeMap()


treemap.display()


treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh


treemap.display()


treemap['jadhesh']


len(treemap)


treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal


treemap.display()


for key, value in treemap:
    print(key, value)


list(treemap)


treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')


treemap['aakash']











import jovian


jovian.commit()


import jovian


jovian.commit()



