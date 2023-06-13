visszaSzamlalas=int(input('Hány órás visszaszámlálást tervezünk? '))
felfugesztes=0

for i in range(visszaSzamlalas,0,-1):  #pl 4-től 0-ig -1 lépéskösszel
    print(f'Visszaszámlálás: {i}')
    valasz=input('Fel kell függeszteni a visszaszámlálást (i/n)? ')
    if valasz=='i':
        felfugesztes+=1

print(f'A rakéta a visszaszámlálást követően ennyi órával indult: {visszaSzamlalas+felfugesztes}')