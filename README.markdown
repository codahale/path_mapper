PathMapper
==========

A path-to-options mapper with a difference.

Why You Should Use It
---------------------

1. Totally backend-agnostic. You don't need controllers, HTTP headers, or
   anything. Only the desire to map paths to options and back again.

2. Performance. PathMapper has been written from the ground up to be as fast as
   possible. Path mapping should be invisible and easy, regardless of how many
   routes you may have.

3. Awesomeness. Yeah. Pretty good.

How It Works
------------

### Static Paths

The best-case scenario is that you want to map a simple string -- say '/home' --
to a set of options:

    mapper.connect('/home', { 'controller': 'home', 'action': 'index' })

PathMapper places these static paths in a hash table, which has a roughly `O(1)`
access time. Regardless of how many static paths you specify, the complexity
remains the same. This is blazing fast.

### Component Paths

A bit slower than static paths are component paths:

    mapper.connect('/:controller/:action/:id')

These are compiled into a prefix tree (or "trie"), which has a `O(m)` access
time, where `m` is the number of path elements. So looking up `/posts/show/1`
requires two comparisons. This is fast, but we're not done yet. The prefix tree
is used to narrow the number of possible routes down to those which could
potentially match. (In practice, this tends to be `:id` vs `:id.:format`
comparisons.) This matching algorithm is `O(n)`, but the n is usually no more
than two or three.

### Regular Expressions

The last check which is done is against regular expression paths:

    mapper.connect(re.compile('/[a-z]{4,6}/DINGO'), { 'controller': 'funkenstein', 'action': 'dingo_hater' })

There's no good way of organizing these, so it's a `O(n)` comparison. Not a bad
tradeoff for much more powerful pattern matching.