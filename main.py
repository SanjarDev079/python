""" FOR sikli"""
""" 1-DARS """

""" N1 """

# mehmonlar=["Sanjar","Ali","Vali", "Soli"]
# for a in mehmonlar:
#     print(f"Salom {a}, Klubimizga xush kelibsiz !")
#     print("Tashrifingizdan mamninmiz !")


""" N2 """

# mehmonlar=["Sanjar","Ali","Vali", "Soli"]
# for a in mehmonlar:
#     print(f"Salom {a}, sizni 20-Mart kuni oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")


""" N3 """

# sonlar=list(range(1,12))
# for a in sonlar:
#     print(f"{a} nig kvadrati {a**2} ga teng . ")


""" N4 """

# sonlar=list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)


""" N5 """

# dostlar=[]
# print("5 ta eng yaqin do'stingizni kirting. ")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizni ismini kirting: "))
# print(dostlar)


""" N6 """

# autolar=["audi", "bmw", "kia", "hunday", "bentli"]
#
# for a in autolar:
#     if a=='bmw':
#         print(a.upper())
#     else:
#         print(a.title())


""" N7 """

# ism=input("Ismingizni kirting: ")
# if ism.lower() != "sanjar":
#     print(f"Uzur, {ism.lower()} biz Sanjarni kutyapmiz. ")
# else:
#     print("Salom, Sanjar")


""" N8 """
# javob=float(input("12*6 nechiga teng: "))
# if javob != 72:
#     print("Javob XATO ")
# else:
#     print("Javob TO'G'RI ")
#

""" N9 """

# yil=int(input("Nechinchi yilda tug'ilgansiz? : "))
# if 2023-yil<18:
#     print(f"Sizning yoshingiz {2023-yil} da ekan, Sizga kirish mumkin emas. ")
# else:
#     print("Sizga kirish mumkin. ")


######################  AMALIYOT  #######################

# login=str(input("Loginingizni kirting: "))
# if login.lower() == "admin":
#     print("Xush kelibsiz Admin")
#     print("Foydalanuvchilar ro'yxatini ko'rasizmi ?")
# else:
#     print(f"Xush kelibsiz {login}")


# son1=int(input("Birinchi sonni kirting: "))
# son2=int(input("Ikkinchi sonni kirting: "))
# if son1==son2:
#     print("Sonlar teng.")
# else:
#     print("Sonlar teng emas.")


# son=int(input("Istalgan sonni kirting: "))
# if son<0:
#     print("Bu son manfiy.")
# else:
#     print("Bu son musbat.")


# son=int(input("Istalgan sonni kirting: "))
# if son>0:
#     print(f"{son} nig ildizi {son**(1/2)} ga teng. ")
# else:
#     print("Musbat son kirting. ")


# l=["olma","anor","uzum","nok","shaftoli","no'xat"]
# print(f"Ro'yxat uzunligi {len(l)} ga teng. ")
# for n in l:
#     print(n.title())


# ism=["Sanjar", "Ali", "Vali","Soli","Xasan", "Xusan"]
# print(ism[1:3])
# ism.append("Axad")
# ism.append("Said")
# print(ism)


# ism=["Sanjar", "Ali", "Vali","Soli","Xasan", "Xusan"]
# ism.insert(2,"Jamshid")
# print(ism)


# narx=[12000, 8000, 5000, 50000, 10000, 2000]
# print(narx[2]+narx[3])


# son = list(range(0,51,2))
# print(son)


# a = str(input("Hafta kunini kirting: "))
# if a.lower()=="yakshanba":
#     print("Bugun damolish kuni . ")
# else:
#     print("Bugun ish kuni. ")


# son=[45, 88, 22, 10, 1, 3, 7, 5, 1000, 200, 31]
# print(sorted(son))
# print(sorted(son,reverse=True))


# son=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)
# son=list(son)
# print(son)
# son.append(55)
# son.append(47)
# son=tuple(son)
# print(son)


"""  UY ISHI  """

# sonlar=list(range(11,100,2))
# for son in sonlar:
#     print(f"{son} ning kub ildizi {son**(1/3)} ga teng. ")
# print(f"Sikl {len(sonlar)} marta aylandi.")


# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# yosh=int(input("Yoshingizni kirting: "))
# if yosh>=20:
#     print("Sizga bu yer to'g'ri kelmaydi.")
# elif yosh>=18:
#     print("Sizga kirish mumkin.")
# elif yosh<18:
#     print("Sizga kirish mumkin emas.")


# ism =str(input("Ismingizni kiriting: "))
# if ism.lower() == "alibek":
#     print("Xush kelibsiz!")
# elif ism.lower() == "vali":
#     print("iltimos Alini  kutib turing.")


# son=int(input("Son kiriting: "))
# if son>0:
#     print(f"{son} ning ildizi {son**(1/2)} ga teng.")
# elif son<0:
#     print("Musbat son kirting.")
# else:
#     print("Musbat son kirting.")


""" if-elif-else ketma ketligi. """

""" 2-DARS """

""" N1 """

# yosh=int(input("Yoshingiz nechida?: "))
# if yosh<=4:
#     price=0
# elif yosh<=12:
#     price=5000
# else:
#     price=10000
# print(f"Sizga kirish {price} so'm")


""" N2 """

# yosh=int(input("Yoshingiz nechida?: "))
# if yosh<=4:
#     price=0
# elif yosh<=12:
#     price=5000
# elif yosh<65:
#     price=10000
# elif yosh>=65:
#     price=8000
# print(f"Sizga kirish {price} so'm")


""" N3 """

# kun=input("Bugun nma kun?>>> ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni. ")


""" N4 """

# kun=input("Bugun nima kun? ")
# harorat=float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik! ")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz. ")


""" N5 """

# kun=input("Bugun nima kun? ")
# harorat=float(input("Havo harorati qanday? "))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Cho'milgani ketdik! ")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print("Uyda dam olamiz. ")


""" N6 """

# narh=15000
# choy=1
# salat=0
#
# if choy and salat:
#     narh= narh+10000
# elif choy or salat:
#     narh= narh+5000
# print(f"Jami {narh} so'm")


""" N7 """

# narh=15000
# choy=1
# salat=0
# non=1
# kompot=1
# assorti=0
#
# if choy:
#     print("Mijoz choy oldi.")
#     narh= narh+3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh= narh+5000
# if non:
#     print("Mijoz non oldi.")
#     narh= narh+2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh= narh+5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh= narh+15000
# print(f"Jami {narh} so'm")


""" N8 """
###  in operato'ri bilan Ro'yhatda biror element borligini tekshiramiz.
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# "manti" in menu  # menuda Manti bormi ?

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nma ovqat yeysiz?>>> ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi. ")
# else:
#     print("Afsuskiy bizda bunday ovqat yo'q. ")


### not in operato'ri yordamida Ro'yhatda biror element yo'qligini tekshiramiz.

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nma ovqat yeysiz?>>> ")
# if ovqat.lower() not in menu:
#     print("Afsuskiy bizda bunday ovqat yo'q. ")
# else:
#     print("Buyurtma qabul qilindi. ")


""" N9 """
### 2 ro'yhatning tarkibini quydagicha tekshiramiz

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar=["osh", "somsa", "manti", "shashlik"]
#
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechrasiz, menuda {taom} yo'q. ")


""" N10 """

### Ro'yhat bo'sh emasligin tekshiramiz

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar=["osh", "somsa", "manti", "shashlik"]
#
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechrasiz, menuda {taom} yo'q")
# else:
#     print("Savatingiz bo'sh!")


"""  UY  ISHI """

# mahsulotlar = ['un', "choy", "sovun", 'shompun', 'sabzi', 'kartoshka', 'piva', 'kivi', 'uzum', "sholg'om"]
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Marketimizda {mahsulot} bor")
#     else:
#         print(f"Marketimizda {mahsulot} yo'q ")




# user=["sanjey@gmail.com",'xush@gmail.com', "shox@gmail.com", "ali@gmail.com"]
# a=input("Login tanlang: ")
# if a.lower() in user:
#     print(f"Uzur bu {a} gmail band, boshqa gmail krting. ")
# else:
#     print("Xush kelibsiz foydalanuvchi. ")



""" LUG'ATLAR """

""" 3-DARS """

""" N1 """

# car={'model':'ferrary','rang':'qizil'}
# print(car['model'])
# print(car['rang'])


# talaba={'ism':'murod olimov','yosh':20,'t_yil':2001}
# print(f"{talaba['ism'].title()}, \n{talaba['t_yil']}-yilda tug'ilgan, \n{talaba['yosh']} yoshda.")
#
# talaba['kurs']=4 # Yangi 'kurs' dagan kalit so'zga 4 ni yuklaymiz
# talaba['fakultet']='informatika' # 'fakultet' ga esa 'informatika'
# print(talaba)



""" N2 """

# talaba={}
# talaba['ism']='qobil rasulov'
# talaba['kurs']=3
# talaba['yosh']=20
# print(talaba)
# print(f"Talaba {talaba['ism'].title()} {talaba['kurs']}-kurs, yoshi {talaba['yosh']} da")


""" N3 """

# talaba_0 = {'ism':"Jonibek O'ralov",'yosh':20,'t_yil':2001}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)



""" N4 """

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")
#
# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")
#
# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# print(phone)
# phone = telefonlar.get('hasan')
# print(phone)




"""  UY  ISHI  """


# sevimli_taom={
#     'dadam':'osh',
#     'onam':'somsa',
#     'opam':'honim',
#     'akam':'shashlik',
#     'men':'lavash'
# }
#
# print(f"\nDadamning savmli taomi {sevimli_taom['dadam']}.\
#          \nOnamning sevmli taomi {sevimli_taom['onam']}.\
#          \nAkamning sevli taomi {sevimli_taom['akam']}.")





# python_i_lugat={
#     'for':'uchun',
#     'if':'agar',
#     'elif':'agar-aksxold',
#     'else':'akisxolda',
#     'del':"o'chrish",
#     'int':'butun son',
#     'float':"o'nlik son",
#     'str':'matin',
#     'list':"ro'yhat",
#     'print':'chqarish',
#     'input':'kiritish'
# }

# kalit=input("Kalit so'z kirting: ").lower()
# print(python_i_lugat.get(kalit,"Bunday so'z mavjud emas."))





""" LUG'ATLAR - 2 """

""" 4-DARS """

""" N1 """


# talaba={
#     'ism':'Sanjar',
#     'familiya':"Ro'zmatov",
#     'yosh':20,
#     'fakulted':'kompyuter injineringi',
#     'kurs':3
# }
# print(talaba.items())
#
# for kalit,qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")


""" N2 """

# mahsulotlar={
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
# }
# print(mahsulotlar.keys())
# print("Do'kondagi mahsulotlar.")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


""" N3 """

# mahsulotlar={
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
# }

# bozorlik=['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")


# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling.")


# print("Do'konimizdagi mahsulotlar.")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())


""" N4 """

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'jamshid':'nokia 3310',
#     'ali': 'iphone x',
#     'jahon': 'iphone x',
#
# }
# print(telefonlar.values())
# print("Foydalanuvchilar quydagi telefonlarni ishlatadi.")
# for tel in telefonlar.values():
#     print(tel)
#
# print("Foydalanuvchilar quydagi telefonlarni ishlatadi.")
# for tel in set(telefonlar.values()):
#     print(tel)



"""   UY  ISHI  """


# python = {
#     'bekmurod': 'lavash',
#     'temur':'palov',
#     'shoxrux': 'shaverma',
#     'odil': 'manti',
#     'kamoron': 'shurpa',
#     'laziz': 'norin',
#     'hamid': 'shashlik',
#     'hurmat':'osh',
#     'aiz':'barak',
#     'nemat':'galupsi'
# }
# print(python.items())
#
# for kalit,qiymat in sorted(python.items()):
#     print(f"{kalit.title()} - {qiymat.title()}")



# Davlatlar={
#     "o'zbekiston":"toshkent",
#     "aqsh":"washington",
#     "italia":"rim",
#     'rassiya':'maskva',
#     'qozoqiston':'bishkek',
# }
# print('Dunyo davlatlari:')
# for davlat in sorted(Davlatlar):
#     print(davlat.upper())
#
# print('\nDavlatlarning poytaxtlari:')
# for poytaxt in sorted(Davlatlar.values()):
#     print(poytaxt.title())



""" NSETING """

""" 5-DARS"""

""" N1 """


# car0={
#     'model':'lacetti',
#     'rang':"oq",
#     'yil':2018,
#     'narh':13000,
#     'km':50000,
#     'korobka':'avtomat'
# }
#
#
#
#
# car1={
#     'model':'cobalt',
#     'rang':"oq",
#     'yil':2020,
#     'narh':20000,
#     'km':60000,
#     'korobka':'avtomat'
# }
#
# car2={
#     'model':'gentra',
#     'rang':"oq",
#     'yil':2019,
#     'narh':12000,
#     'km':45000,
#     'korobka':'avtomat'
# }



# car=car0
# print(f"{car['model'].title()},\
# {car['rang']} rang,\
# {car['yil']}-yil,{car['narh']}$")
#
# car=car1
# print(f"{car['model'].title()},\
# {car['rang']} rang,\
# {car['yil']}-yil,{car['narh']}$")
#
# car=car2
# print(f"{car['model'].title()},\
# {car['rang']} rang,\
# {car['yil']}-yil,{car['narh']}$")



# cars = [car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()},\
# {car['rang']} rang,\
# {car['yil']}-yil,{car['narh']}$")
#
#
# print(cars[0])
# print(cars[0]['model'].title())
# print(f"{cars[2] ['rang'].title()}\
# {cars[2] ['model'].title()}")


# malibus=[]
# for n in range(10):
#     new_car={
#
#         'model': 'gentra',
#         'rang': None,
#         'yil': 2019,
#         'narh': None,
#         'km': 0,
#         'korobka': 'avtomat'
#
#     }
#     malibus.append(new_car)
# print(malibus)
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# print(malibus)
#
# for malibu in malibus:
#     if malibu['korobka']=='avtomat':
#         malibu['narh']=40000
#     else:
#         malibus['narh']=35000
# print(malibus)



""" while """

""" 7-DARS"""

""" N1 """

# savol = "Yoshingizni kiriting: "
#
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
#
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")




""" N2 """

# ismlar = []
#
# print("Yaqin do'slaringiz ro'yxatini tuzamiz.")
# n=1
# while True:
#     ism = input(f"{n}-do'stingiz ismini kirting: ")
#     ismlar.append(ism)
#     javob=input("Yana ism qo'shasizmi (ha/yoq)")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print(ismlar)
#
# print("Do'slaringiz ro'yxati")
# for ism in ismlar:
#     print(ism.title())

""" N3 """

# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingiz ismini kirting: ")
#     yosh=input(f"{ism.title()}ning yoshini kirting: ")
#     dostlar[ism]=int(yosh)
#
#     javob=input("Yana malumot qo'shasizmi? (yes/no)")
#     if javob == 'no':
#         ishora=False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda.")


""" N3 """

# cars=['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia'in cars:  # toki nexia cars ro'yhati ichida ekan.....
#     cars.remove('nexia') # nexia ni ro'yhatdan olib tashla
# print(cars)



""" N4 """

# talabalar=['sanjar','dilshod','qaxramon','suhrob','ogabek']
# b_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()}ning bahosini kirting: ")
#     print(f"{talaba.title()} baholandi.")
#     b_talabalar[talaba]=baho
# print(b_talabalar)



""" UY ISHI """

# print("Menyumizda bor ovqatlar (burger  shashlik  shaurma somsa shurpa")
# menu = ['burger', 'shashlik', 'shaurma', 'somsa', 'shurpa']
# savat = []
# a = 1
# while True:
#     ovqat = input(f'{a}-qaysi ovqatni buyurtma qilasz?')
#     savat.append(ovqat)
#     javob = input("Yana buyurtma qilasizmi? (yes/no)")
#     if javob.lower() == 'yes':
#         a += 1
#         continue
#     else:
#         break
# print(f"Sz buyurtma qilgan ovqat {savat}")



# while True:
#     ovqat = input(f"{a}-qaysi ovqatni buyurtma qilasz?")
#     if ovqat not in menu:
#         print(f"uzr bizda {ovqat.title()} yo'q")
#         break
#     elif ovqat in menu:
#         savat.append(ovqat)
#         javob = input("Yana buyurtma qilasizmi? (yes/no)")
#     if javob.lower() == 'yes':
#         a += 1
#         continue
#     else:
#         break
# print(f"Sz buyurtma qilgan ovqat {savat}")



"""  """

""" 8-DARS"""

""" N1 """
