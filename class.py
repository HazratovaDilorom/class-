class Odam:
    def __init__(self,ism,familya,yosh):
        self.ism=ism
        self.familya=familya
        self.yosh=yosh
    def __str__(self):
        return f'Ismi:{self.ism} Familya:{self.familya} Yosh:{self.yosh}'
odam1=Odam('dilorom','hazratova',20)
print(odam1)



class Shifokor(Odam):
    def __init__(self,ism,yosh,mutahasislik):
        super().__init__(ism,yosh,None)
        self.mutahasislik=mutahasislik

    def __str__(self):
        return f'Ismi:{self.ism}  Yosh:{self.yosh} Mutahasisligi:{self.mutahasislik}'
odam2=Shifokor('dilorom',20,'bolalar  shifokori')
print(odam2)

class Oshpaz(Odam):
    def __init__(self,ism,familya,yosh,millat):
        super().__init__(ism,familya,yosh)
        self.millat=millat

    def __str__(self):
        return f'Ismi:{self.ism} Familyasi:{self.familya} Yosh:{self.yosh} Millati:{self.millat}'

odam3=Oshpaz('Diyor','Qosimov',20,'rus')
print(odam3)

class Stilist(Odam):
    def __init__(self,ism,familya,yosh,tajribasi,ishchilari):
        super().__init__(ism,familya,yosh)
        self.tajribasi=tajribasi
        self.ishchilari=ishchilari
    def __str__(self):
        return f'Ismi:{self.ism} Familyasi:{self.familya} Yoshi:{self.yosh} Tajribasi:{self.tajribasi} Ishchilari:{self.ishchilari} '

odam4=Stilist('Afruza','Dilova',27,'3yillik mutahasis','7ta')
print(odam4)

class Shafyor(Odam):
    def __init__(self,ism,familya,yosh,mashinasi,rangi,malumoti):
        super().__init__(ism,familya,yosh)
        self.mashinasi=mashinasi
        self.rangi=rangi
        self.malumoti=malumoti
    def __str__(self):
        return f'Ismi:{self.ism} Familyasi:{self.familya} Yoshi:{self.yosh} Mashinasi:{self.mashinasi} Rangi:{self.rangi} Mulumoti:{self.malumoti}'

odam5=Shafyor('Javohir','Raupov',32,'jentra','qora',"o'rta")
print(odam5)

class Turist(Odam):
    def __init__(self,ism,familya,yosh,millati,dini,malumoti):
        super().__init__(ism,familya,yosh)
        self.millati=millati
        self.dini=dini
        self.malumoti=malumoti
    def __str__(self):
        return f'Ismi:{self.ism} Familyasi:{self.familya} Yoshi:{self.yosh} Millati:{self.millati} Dini:{self.dini} Malumoti:{self.malumoti}'

odam6=Turist('Alyonka','Sergeyevna',23,'rus','xristian','oliy')
print(odam6) 

