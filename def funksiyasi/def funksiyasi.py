""" UY ISHI """

def foydalanuvchi(a=int(input("Birinchi sonni kirting: ")),b=int(input("Ikkinchi sonni kirting: "))):
    """Sonning kvadrati va kubini hisoblovchi funksiya"""
    print(f"Birinchi sonning kvadrati {a**2} ga teng\n"
    f"Ikkinchi sonning kubi {b**3} ga treng.")
print(foydalanuvchi.__doc__)
foydalanuvchi()



def foydalanuvchi(a=int(input("Birinchi sonni kirting: ")),b=int(input("Ikkinchi sonni kirting: "))):
    """Sonning juft yoki toqligini hisoblovchi funksiya"""
    print(f"Brinchi son {a%2==0} juft son\n"
          f"Ikkinchi son {b%2==1} toq son")
print(foydalanuvchi.__doc__)
foydalanuvchi()
