""" UY ISHI """

# def foydalanuvchi(a=int(input("Birinchi sonni kirting: ")),b=int(input("Ikkinchi sonni kirting: "))):
#     """Sonning kvadrati va kubini hisoblovchi funksiya"""
#     print(f"{a} ning kvadrati {a**2} ga teng\n"
#     f"{b} ning kubi {b**3} ga treng.")
# print(foydalanuvchi.__doc__)
# foydalanuvchi()
#
#
#
# def foydalanuvchi(a=int(input("Birinchi sonni kirting: ")),b=int(input("Ikkinchi sonni kirting: "))):
#     """Sonning juft yoki toqligini hisoblovchi funksiya"""
#     print(f"{a} soni  {a%2==0} juft son\n"
#           f"{b} soni {b%2==1} toq son")
# print(foydalanuvchi.__doc__)
# foydalanuvchi()



#  #  #  #  Ikkala misolni birga jamlab ishlaymiz.

def foydalanuvchi(a=int(input("Birinchi sonni kirting: ")),b=int(input("Ikkinchi sonni kirting: "))):
    """Sonning juft yoki toqligini hisoblovchi va
    kub-kvadratni hisoblovchi funksiya"""
    print(f"{a} soni  {a%2==0} {a} juft son\n"
          f"{b} soni {b%2==1} {b} toq son")
    print(f"{a} ning kvadrati {a**2} ga teng\n"
        f"{b} ning kubi {b**3} ga treng.")


print(foydalanuvchi.__doc__)
foydalanuvchi()


