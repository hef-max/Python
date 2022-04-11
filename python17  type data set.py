# set, himpunan
superhero = {'superman',
             'batman',
             'catwomen',
             'robin'}
print(superhero)

superhero.add('joker') # for menambahkan himpunan
superhero.add('robin') # can't menambahkan already exist
print(superhero)

# for menguruktkan himpunan
print(sorted(superhero))

print(100*'=')

# himpunan can in write like this too
hero = set()

hero.add('spiderman')
hero.add('ironman')
hero.add('hulk')
hero.add('thor')
hero.add(212) # can also menambahkan with num, but can't use sorted

print(hero)

print(100*'=')

# try with bil
ganjil = {1,3,5,7}
genap = {2,4,6,8}
prime = {2,3,5,7}

print(ganjil.union(genap)) # menggabungkan bil
print(ganjil.intersection(prime)) # irisan or num to find as same
