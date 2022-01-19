from LinkedQueue import *

class Tree:#hierarchial
    """Abstract base class represeting a tree structure."""

    class Position:
        """an abstraction representing the location of a single element."""
        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")
        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)
        
    #-------abstract methods that concrete subclass must support--------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")
    def parent(self,p):
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self,p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("must be implemented by subclass!")

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) ==0
    
    def depth(self,p):#recursive
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1+ self.depth(self.parent(p))
        
    def _height1(self):
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self,p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1+ max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        """Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree."""
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():#use same order as positions()
            yield p.element()#but yield p.element()
    
    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self,p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
            
    def positions(self):
        return self.preorder()

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self,p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
            


class BinaryTree(Tree):
    """abstract base class representing a tree structure."""

    def left(self, p):
        """Return a position representing p's left child.
        Return None if p does not have a left child."""
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a position representing p's right child.
        Return None if p does not have a right child."""
        raise NotImplementedError("must be implemented by subclass")

    #-----------------concrete methods implemented in this class---------------
    def sibling(self, p):
        """Return a position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
        
    def children(self, p):
        """Generate an iteration of positions representing p's childrent"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent = None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):#check if valid
        """Return associated node, if position is valid"""
        
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type.")
        
        if p._container is not self:
            raise ValueError("p does not belong to this container.")

        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        
        return p._node

    def _make_position(self, node):
        """Return position instance for given node(or return None if no node)"""
        return self.Position(self, node) if node is not None else None

    #-------------binary tree constructor--------------
    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    #-------------public accessors---------------------
    
    def __len__(self):
        return self._size

    def root(self):
        """Return the root position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)#return position instance

    def parent(self,p):
        """Return the Position of p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)#return position instance

    def left(self, p):
        """Return the position of p's left child (or None if no left child.)"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right child (or None if no right child.)"""
        node = self._validate(p)
        return self._make_position(node._right)
    
    def access_children(self,p):#access all children
        node = self._validate(p)
        if self.num_children(p) == 2:   
            print("left child:",self.left(p).element(), "right:",self.right(p).element())
            #return self.left(p).element(), self.right(p).element()
        elif self.num_children(p) == 1:
            try:
                print("left child:",self.left(p).element())
            except:
                print("right:",self.right(p).element())
        else:
            print("no children")
            
    def num_children(self,p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0

        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty."""
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        print("root {} added".format(e))
        return self._make_position(self._root)

    def _add_left(self, p,e):
        """Create a new left child for Position p, storing element e.
        Return the position of new node.
        Raise ValueError if Position p is invalid or p already jas a left child."""

        node = self._validate(p)
        if node._left is not None:
            raise ValueError("left child already exists")
        self._size += 1
        node._left = self._Node(e, node)
        print("left {} added".format(e))
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the position of new node.
        Raise Value Error if Position is invalid or p already has a right child."""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right  = self._Node(e, node)
        print("right {} added".format(e))
        return self._make_position(node._right)


    def _replace(self, p,e):
        """Replace the element at position p with c, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        print("replaced: {}->{}".format(old,e))
        return old

    def _delete(self, p):#unable to delete when the node has two children
        """Delete the node at position p, and relace it with its child, if any.
        Return the element that had been stored at position p.
        Raise value error if position p is invalid, or p has two children."""
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node._left if node._left else node._right
        
        if child is not None:
            child._parent = node._parent
            
        if node is self._root:#if it is root
            self._root = child

        else:#node의 child를 node의 parent의 child로
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node#연결해지(convention for deprecated node)
        print("deleted: {}".format(node._element))
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")
        
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size += len(t1)+len(t2)
        
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
            
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
            
        print("attached successfully")
    

#Basic Functions       
LT = LinkedBinaryTree()
root = LT._add_root(2)
print("root:",LT.root().element())
#error: LT._add_root(2)
left1 = LT._add_left(root,1)
print("left:",LT.left(root).element())
LT._add_right(root,2)
print("right:",LT.right(root).element())
LT._replace(root,0)
LT.access_children(root)
left2 = LT._add_left(left1,3)
LT.access_children(left1)
LT.access_children(root)
LT._delete(left2)

right1 = LT._add_right(left1,'r')

LT2= LinkedBinaryTree()
rt2 = LT2._add_root("roo")
LT2._add_right(rt2,"r")

LT3 = LinkedBinaryTree()
rt3 = LT3._add_root("k")
LT._attach(right1,LT2,LT3)



#Traverse
print("\n\n\nTesting Traverse")
print("--------------------Tree initialization----------------")
LBT = LinkedBinaryTree()
root = LBT._add_root("root")
left1 = LBT._add_left(root,"left1")
right1 = LBT._add_right(root,"right1")

print("-------------------Preorder(root-left-right)--------------------")
for p in LBT.preorder():
    print(p.element())

print("-------------------Postorder(left-right-root)--------------------")
for p in LBT.postorder():
    print(p.element())

print("-------------------Inorder(left-root-right)------------------")
for p in LBT.inorder():
    print(p.element())

print("--------------breadthfirst-----------------")
for p in LBT.breadthfirst():
    print(p.element())
