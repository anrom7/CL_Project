print """'a) feed Cyril and give a capuccino to Angus'
'λxλyλz.(feed(x) ^ give(y,z))(Cyril, capuccino, Angus)'

'b) be given ‘War and Peace’ by Pat'
'λxλy.(give(x,y) (Pat, War and Peace)'

'c) be loved by everyone'
'∀x.(person(x))-> ∃z.(person(z))^love(x,z)'

'd) be loved or detested by everyone'
'∀x.(person(x))-> ∃z.(person(z))^love(x,z)?detest(x,z)'

'e) be loved by everyone and detested by no-one'
'∀x.(person(x))-> ∃z.(person(z))^love(x,z)?-detest(x,z)'"""
