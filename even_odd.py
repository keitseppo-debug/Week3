from colorama import Fore, Style
#Programm palub kasutajal sisestada arvu. Kasutaja sisestatud arvu.
#Programm määrab, kas arv on paaris või paaritu, ja annab vastava tagasiside.

#Modulus (%)

n = int(input("Sisesta täisarv: "))

# if n % 2 == 0:
#     print("Arv on paaris.")
# else:
#     print("Arv on paaritu.")

#tenary operator
# print("Arv on paaris." if n % 2 == 0 else "Arv on paaritu.")

match n % 2:
    case 0:
        print(Fore.GREEN + "Arv on paaris." + Style.RESET_ALL)
    case _:
        print(Fore.RED + "Arv on paaritu." + Style.RESET_ALL)