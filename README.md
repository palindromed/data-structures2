# linked-list
Implements a linked list with python

This repo holds sample code for some classic data structures, implemented in Python, including singly- and doubly-linked lists and stacks, heaps, queues, deques, priority queues, and graphs. Singly-linked lists are convenient for keeping a group of data nodes in order; adding and removing them is simple and efficient. They are most useful when we only need to traverse our data in one direction. Doubly-linked lists make their nodes more accessible since they can be inserted or removed at either end of the list; but navigating the list is costlier. Stacks, queues, and deques are more refined implementations.  Priority queues, heaps, and graphs illustrate more complex ways nodes of data can be related to each other.

It's a joint project of Michael Sullivan and A.J. Wohlfert.

--------------

paren_aj.py is AJ's implementation of a function to evaluate proper parenthetical statements in a given piece of text.  If the parens are broken, a -1 will be returned, if the parens are left open, a 1 will be returned and if the parens are properly closed a 0 will be returned.


______________

parenthetics.py implements the same function as paren_aj.py, but with a different approach by Michael. There are tests for both.


______________

Sources:

Our graph traversal functions adapt the algorithms found at:
http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
