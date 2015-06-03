#Translate the following sentences into predicate-argument formulas of first-order logic.

# a. Angus likes Cyril and Irene hates Cyril.
# Like(Angus,Cyril) & hate(Irene, Cyril)
# like(a,b) & hate(c,b)
print 'sentence_A  =  Angus likes Cyril and Irene hates Cyril.'
print 'predicate-argument formulas of first-order logic =  like(a,b) & hate(c,b)'
print '-------------------------------------------------------------------------'

#b. Tofu is taller than Bertie.
#be_taller(Tofu,Bertie) 
#be_taller(a,b)
print 'sentence_B =  Tofu is taller than Bertie.'
print 'predicate-argument formulas of first-order logic = be_taller(a,b)'
print '-------------------------------------------------------------------------'

#c. Bruce loves himself and Pat does too.
#love(Bruce,Bruce) & love(Pat,Pat) 
#love(a,a)  & love(b,b)
print 'sentence_C = Bruce loves himself and Pat does too.'
print 'predicate-argument formulas of first-order logic = love(a,a)  & love(b,b)'
print '-------------------------------------------------------------------------'

#d. Cyril saw Bertie, but Angus didn’t.
#see(Cyril,Bertie) & -see(Angus,Bertie)
#see(a,b) & -see(c,b)
print 'sentence_D = Cyril saw Bertie, but Angus didn’t.'
print 'predicate-argument formulas of first-order logic = see(a,b) & -see(c,b)'
print '-------------------------------------------------------------------------'

#e. Cyril is a four-legged friend.
#be_friend(Cyril)
#be_friend(a)
print 'sentence_E =  Cyril is a four-legged friend.'
print 'predicate-argument formulas of first-order logic = be_friend(a)'
print '-------------------------------------------------------------------------'

#f. Tofu and Olive are near each other.
#be_near(Tofu, Olive)
#be_near(a, b)
print 'sentence_F = Tofu and Olive are near each other.'
print 'predicate-argument formulas of first-order logic = be_near(a, b)'
print '-------------------------------------------------------------------------'
