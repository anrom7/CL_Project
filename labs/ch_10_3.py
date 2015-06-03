import nltk
#a) Angus likes someone and someone likes Julia.
"""
exists a. exists s. exists j. (like(a, s) & like(s, j))
"""

dom = set(['a', 'j', 's'])
v = """
Angus => a
Julia => j
sb => s
like => {(a, s), (s, j)}
"""
val = nltk.parse_valuation(v)
g = nltk.Assignment(dom, [('x', 'a'), ('y', 'j'), ('z', 's')])
m = nltk.Model(dom, val)
print "a.", m.evaluate('exists x. exists z. exists y. (like(x, z) & like(z, y))', g)


#b) Angus loves a dog who loves him.
"""
exists a. exists d. (love(a, d) & love(d, a))
"""

#c) Nobody smiles at Pat.
"""
- exists n. exists p. (smile(n,p))
"""

dom = set(['n', 'p'])
v = """
Nobody => n
Pat => p
smile => {-(n, p)}
"""
val = nltk.parse_valuation(v)
g = nltk.Assignment(dom, [('x', 'n'), ('y', 'p')])
m = nltk.Model(dom, val)
print "c.", m.evaluate('exists x. exists y. -(smile(x,y))', g)


#d) Somebody coughs and sneezes.
"""
exists x.(coughs(x) & sneezes(x))
"""

#e) Nobody coughed or sneezed.
"""
all x. -(coughed(x) | sneezed(x))
"""

#f) Bruce loves somebody other than Bruce.
"""
exists b. exists s. (-(love(b, b) & love(b, s)))
"""
dom = set(['b', 's'])
v = """
Bruce => b
sb => s
love => {(b, s), -(b, b)}
"""
val = nltk.parse_valuation(v)
g = nltk.Assignment(dom, [('x', 'b'), ('y', 's')])
m = nltk.Model(dom, val)
print "f.", m.evaluate('exists x. exists y. (-(love(x, x) & love(x, y)))', g)


#g) Nobody other than Matthew loves Pat.
"""
exists s. exists m. exists p. (-(love(s, p) & love(m, p)))
"""

#h) Cyril likes everyone except for Irene.
"""
exists c. all s. exists i. (-like(c, i) & like(c, s)))
"""

dom = set(['c', 's', 'i'])
v = """
Cyril => c
sb => s
Irene => i
like => {(c, s), -(c, i)}
"""
val = nltk.parse_valuation(v)
g = nltk.Assignment(dom, [('x', 'c'), ('y', 's'), ('z', 'i')])
m = nltk.Model(dom, val)
print "h.", m.evaluate('exists x. all y. exists z. (-(like(Cyril, Irene) & like(x, y)))', g)

#i) Exactly one person is asleep.
"""
(asleep(x))
"""

dom = set(['p'])
v = """
person => p
asleep => {(p)}
"""
val = nltk.parse_valuation(v)
g = nltk.Assignment(dom, [('x', 'p')])
m = nltk.Model(dom, val)
print "i.", m.evaluate('(asleep(x))', g)
