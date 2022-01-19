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
    
        

class Binary Tree(Tree):
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
        

















































        
