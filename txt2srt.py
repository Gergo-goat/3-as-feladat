class IdozitettFelirat:
    def __init__(self,ido:str,felirat:str):
        self.Ido=ido
        self.Felirat=felirat

    def SzavakSzama(self):
        return len(self.Felirat.split(' '))

    def SrtIdozites(self):
        #00:01 - 00:03
        kezdes=self.Ido[0:5]
        print(kezdes)
        befejezes=self.Ido[8:13]
        #kezdés
        if int(kezdes[0:2])<60:
            kezdes="00:"+kezdes
        else:
            kezdes=str(int(kezdes[0:2])//60).rjust(2,'0')+':'+str(int(kezdes[0:2])%60).rjust(2,'0')+kezdes[2:5]

        #befejezes
        if int(befejezes[0:2])<60:
            befejezes="00:"+befejezes
        else:
            befejezes=str(int(befejezes[0:2])//60).rjust(2,'0')+':'+str(int(befejezes[0:2])%60).rjust(2,'0')+befejezes[2:5]
        return kezdes+' --> '+befejezes


feliratok:list[IdozitettFelirat]=[]

f=open('feliratok.txt','r',encoding='utf-8')
index=1
for sor in f:
    if index%2==0:
        feliratok.append(IdozitettFelirat(idobelyeg.strip(),sor.strip()))
    else:
        idobelyeg=sor
    index+=1
f.close()

print(f'5. feladat: Feliratok száma: {len(feliratok)}')

maxFeliratPoz=0
for i in range(len(feliratok)):
    if feliratok[i].SzavakSzama()>feliratok[maxFeliratPoz].SzavakSzama():
        maxFeliratPoz=i
print(f'7. feladat: Legtöbb szóból álló felirat:\n{feliratok[maxFeliratPoz].Felirat}')  

f=open('felirat.srt','w',encoding='utf-8')
for i in range(len(feliratok)):
    f.write(f'{i+1}\n{feliratok[i].SrtIdozites()}\n{feliratok[i].Felirat}\n\n')
f.close()
