# SplayTree

SplayTree is a Self Adjusting Binary Search Tree (RedBlack Trees, AVL Trees, Scapegoat Trees, 2-3 Trees and so on)

The splay tree was invented by Daniel Sleator and Robert Tarjan in 1985

All normal operations on a binary search tree are combined with one basic operation, called splaying. Splaying the tree for a certain element rearranges the tree so that the element is placed at the root of the tree. One way to do this with the basic search operation is to first perform a standard binary tree search for the element in question, and then use tree rotations in a specific fashion to bring the element to the top. Alternatively, a top-down algorithm can combine the search and the tree reorganization into a single phase.

Good performance for a splay tree depends on the fact that it is self-optimizing, in that frequently accessed nodes will move nearer to the root where they can be accessed more quickly. The worst-case height—though unlikely—is O(n), with the average being O(log n)

Unlike its "relatives", Splay Trees do not maintaing the extra state. Since Splay Trees maintain no state, they are also called "Lazy" Trees

Usage: caching, garbage collection

2 related intuitions:

* path shortening (if a search is long -> shorten paths). problem: shortening one path makes others longer. Release potential of doing the search
        
* rebalancing / rotation (double rotations [zig-zig which is children are left left or right right (bidirectional) and zig-zag which is left-right or right-left(one-directional, makes tree shorter)] )

**Single Rotation**

        y                       x     
       / \                     / \
      x   C        ==>        A   y
     / \                         / \
    A   B                       B   C 

**Double Rotations**
_**Zig-Zig**_

          z                      x
         / \                    / \
        y   D       ==>        A   y
       / \                        / \
      x   C                      B   z
     / \                            / \
    A   B                          C   D


_**Zig-Zag**_

         z                       x
        / \                     /  \
       y   D      ==>          y    z
      / \                     / \  / \
     A   x                   A   B C  D  
        / \                                   
       B   C                                
    
**Splay Tree Implementation**

* _**search**_: do a normal search -> splay found node to the root via double rotations and one final single rotation if necessary

* _**access theorem**_: deep fat subtree is bad and implies a large potential. Amortized time to splay x given root T is <= 3 (r(t) - r(x)) + 1 = O(log s(t) / s(x)). size s(x) - total weight of descendants, rank r(x) = log (s(x)), so O(log n) amortized search cost, because s(t, t is the root) = n (number of nodes in a tree), s(x) >= 1

* _**static optimality theorem**_: item access frequency 0 <= pi <= 1. Splay Tree Amortized access cost O(-E pi * log pi). according to access theorem if we take wi = pi , then O(log Epi/pi), and Epi = -1

* _**static finger theorem**_: splay tree beat last static finger

* _**working set theorem**_: if t items since last access to x then splay tree cost is O(log t)

## Time complexity in big O notation

| Algorithm     | Average       | Worst case        |
|:------------- |:-------------:|:-----------------:|
| Space         | O(n)          | O(n)              |
| Search        | O(log n)      | amortized O(log n)|
| Insert        | O(log n)      | amortized O(log n)|
| Delete        | O(log n)      | amortized O(log n)|

