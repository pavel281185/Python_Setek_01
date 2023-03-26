import random
import string
import math
import os

# Python pro začátečníky - jeden z nejpopulárnějších backendových jazyků na světě

# 2
# print("Pavel Kvasnička")

# 3
# print("Dobrý den")
# print("Pavel")
# print("Kvasnička")

# 4
# print("Učím se Python")
# print("Funkce print začíná slovem print")
# print('Funkci print zavoláme print("nějaký text")')

# 5
# print("David\nadmin123")
# print("Harry" + " " + "Ron" + " " + "Hermiona")

# 7
# print("Naučili jsme se mnoho věcí o stringu")
# print('Spojení stringu děláme pomocí znaménka "+"')
# print("Také jsme používali print('nějaký text')")
# print("První řádek\nDruhý řádek se dělá pomocí lomítka a n")

# 10
# city = input("Zadejte město ")
# print("Bydlím ve městě " + city)

# 14
# print("Vítejte v aplikaci na generování vtioných jmen")
# jmeno = input("Jaké je tvé jméno ")
# vlastnost = input("Jaká je tvá typická vlastnost. Napiš ji s velkým písmenem. ")
# print("Tvoje vtipné jméno je " + jmeno + " " + vlastnost)

# print("Vítejte v aplikaci na generování vtipných jmen")
# print("Tvoje vtipné jméno je " + input("Jaké je tvé jméno ") + " " + input("Jaká je tvá typická vlastnost. Napiš ji s velkým písmenem. "))

# age = 40
# print(type(age))
# print("Je mi " + str(age))

# 17
# cislo = input("Napište dvoumístné číslo: ")
# print(int(str(cislo)[0])+int(str(cislo)[1]))

# 19
# vyska = input("Zadejte svou výšku v metrech: ")
# vaha = input("Zadejte svou váhu v kg: ")
# print("Váš BMI je: " +str(int(int(vaha)/float(vyska)**2)))

# 23
# vek = int(input("Kolik je vám let? "))
# roky = 90 - vek
# mesice = roky * 12
# tydny = roky * 52
# dny = roky * 365
# print(f"Zbývá vám {roky} let, {mesice} mesiců, {tydny} týdnů, {dny} dnů")

# 24
# print("Vítejte v kalkulátoru plateb.")
# cost = float(input("Kolik máte celkem zaplatit? "))
# percentage = float(input("Kolik chcete dát spropitného (%)? "))
# people = int(input("Mezi kolik lidí se má rozdělit částka?"))
# one_payment = (cost * (1 + percentage / 100)) / people
# print(f"Každý člověk by měl zaplatit {one_payment}")

# 27
# if input("Jste student? ").lower() == "ano":
#     print("Cena lístku je 120Kč")
# else:
#     print("Cena lístku je 150Kč")

# 33
# height = float(input("Vložte svoji váku v metrech: "))
# weight = float(input("Vložte svoji váhu v kg: "))
# bmi = weight/height**2
# if bmi < 18.5:
#     print(f"Vaše bmi je {round(bmi,2)} a máte podváhu")
# elif bmi >= 18.5 and bmi < 25:
#     print(f"Vaše bmi je {round(bmi,2)} a jste v normálu")
# elif bmi >= 25 and bmi < 30:
#     print(f"Vaše bmi je {round(bmi,2)} a máte nadváhu")
# elif bmi >= 30 and bmi < 35:
#     print(f"Vaše bmi je {round(bmi,2)} a jste obézní")
# else:
#     print(f"Vaše bmi je {round(bmi,2)} a máte extrémní obezitu")

# 34
# rok = int(input("Zadejte přestupný rok: "))
# if (rok % 4 == 0 and rok % 100 != 0) or (rok % 4 == 0 and rok % 100 == 0 and rok % 400 == 0):
#     print("Přestupný")
# else:
#     print("Nepřestupný")

# 35
# print("vítejte v aplikaci na objednání pizzy.")
# velikost = input("Zadejte velikost pizzy S/M/L: ").upper()
# if velikost == "S":
#     cena = 100
# elif velikost == "M":
#     cena = 150
# elif velikost == "L":
#     cena = 200
# else:
#     print("Nezadal jste požadovaný vstup")
# if input("Chcete feferonky? ") == "A":
#     if velikost == "S":
#         cena += 20
#     else:
#         cena += 30
# if input("Chcete extra sýr? ") == "A":
#     cena += 15
# print(f"Cena vaší pizzy je {cena}")

# 42
# if random.random() <= 0.5:
#     print("Hlava")
# else:
#     print("Orel")

# 47
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# clovek = int(input("Co si vyberete? Napi3te 0 pokud kámen, 1 pro papír a 2 pro nůžky. "))
# pocitac = random.randint(0,2)
# znak = [rock, paper, scissors]
# print(f"Uživatel si vybral:\n{znak[clovek]}")
# print(f"Počítač si vybral:\n{znak[pocitac]}")
# if clovek == pocitac:
#     print("Remíza")
# elif (clovek == 0 and pocitac == 2) or (clovek == 1 and pocitac == 0) or (clovek == 2 and pocitac == 1):
#     print("Vyhrál jsi, počítač prohrál")
# else:
#     print("Prohrál jsi, počítač vyhrál")

# 49
# vyska = input("Vložte výšku lidí oddělené čárkou a mezerou. ").split(", ")
# mezi_vysledek = 0
# for jedna_vyska in vyska:
#     mezi_vysledek += int(jedna_vyska)
# vysledek = mezi_vysledek / len(vyska)
# print(f"Průměrná výška je: {round(vysledek, 2)}")

# 52
# vysledek = 0
# for cislo in range(1, 101):
#     if (cislo % 2) == 0:
#         vysledek += cislo
# print(f"Součet je {vysledek}")

# 53
# for cislo in range(1, 101):
#     if cislo % 3 == 0 and cislo % 5 == 0:
#         print("FizzBuzz")
#     elif cislo % 3 == 0:
#         print("Fizz")
#     elif cislo % 5 == 0:
#         print("Buzz")
#     else:
#         print(cislo)

# 55
# heslo = []
# string_heslo = ""
# for pismeno in range(0, int(input("Kolik písmen chcete mít ve svém heslu? "))):
#     heslo.append(random.choice(string.ascii_letters))
# for cislo in range(0, int(input("Kolik čísel chcete mít ve svém heslu? "))):
#     heslo.append(random.choice(string.digits))
# for znak in range(0, int(input("Kolik speciálních znaků chcete mít ve svém heslu? "))):
#     heslo.append(random.choice(string.punctuation))
# random.shuffle(heslo)
# for letter in heslo:
#     string_heslo += letter
# print(string_heslo)

# 64
# def pokryti(vyska, sirka, pokryti):
#     return math.ceil((vyska*sirka)/pokryti)
# print(f"Budete potřebovat {pokryti(int(input('Výška zdi: ')), int(input('Šířka zdi: ')), 4)} plechovek barvy.")

# 65
# cislo_ke_kontrole = int(input("Zadejte číslo ke kontrole. "))
# kontrola = 0
# for cislo in range(1, cislo_ke_kontrole + 1):
#     if cislo_ke_kontrole == 1:
#         kontrola += 1
#     if cislo_ke_kontrole % cislo == 0:
#         kontrola += 1
# if kontrola == 2:
#     print(f"{cislo_ke_kontrole} - Jedná se o prvočíslo")
# else:
#     print(f"{cislo_ke_kontrole} - Nejedná se o prvočíslo")

# 66
# def encode(text, posun):
#     encoded_text = ""
#     for letter in text:
#         if abeceda.index(letter) + posun + 1 > len(abeceda):
#             pocet = abeceda.index(letter) + posun - len(abeceda)
#         else:
#             pocet = abeceda.index(letter) + posun
#         encoded_text += abeceda[pocet]
#     print(f"Encrypted text is: {encoded_text}")
#
#
# def decode(text, posun):
#     decoded_text = ""
#     for letter in text:
#         if abeceda.index(letter) - posun < 0:
#             pocet = abeceda.index(letter) - posun + len(abeceda)
#         else:
#             pocet = abeceda.index(letter) - posun
#         decoded_text += abeceda[pocet]
#     print(f"Decrypted text is: {decoded_text}")
#
#
# abeceda = string.ascii_lowercase
# konec = "yes"
# while konec == "yes":
#     typ = input("Type 'encode' to encrypt, type 'decode' to decrypt. ")
#     text = input("Type your message. ").lower()
#     posun = int(input("Type the shift number. "))
#     if typ == "encode":
#         encode(text, posun)
#     elif typ == "decode":
#         decode(text, posun)
#     konec = input("Type 'yes' if you want to go again. Othervise type 'no'. ")

# 69
# students_results = {
#     "Harry": 85,
#     "Ron": 71,
#     "Hermione": 98,
#     "Draco": 69
# }
# empty_dictionary = {}
# for student in students_results:
#     if students_results[student] >= 91:
#         empty_dictionary[student] = "Excelentní"
#     elif students_results[student] >= 81:
#         empty_dictionary[student] = "Vynikající"
#     elif students_results[student] >= 71:
#         empty_dictionary[student] = "Splněno"
#     else:
#         empty_dictionary[student] = "Nesplněno"
# print(empty_dictionary)

# 71
# travel_diary = [
#     {
#         "country": "Spain",
#         "visited_cities": ["Madrid", "Leon", "Valencia"],
#         "visits": 5
#     },
#     {
#         "country": "France",
#         "visited_cities": ["Paris", "Nice", "Rennes"],
#         "visits": 2
#     }
# ]
#
#
# def add_country(diary, country_name, town_list, visits_number):
#     new_dictionary = {}
#     new_dictionary["country"] = country_name
#     new_dictionary["visited_cities"] = town_list
#     new_dictionary["visits"] = 1
#     diary.append(new_dictionary)
#
#
# add_country(travel_diary, "Czech Republic", ["Prague", "Brno", "Pilsen"], 1)
# print(travel_diary)
# print(travel_diary[2]["visits"])

# 72
# print("Vítejte v programu pro tichou dražbu")
# pokracovat = "ano"
# nabidky = {}
# vitez = ""
# max = 0
# while pokracovat == "ano":
#     vitez = input("Jaké je Vaše jméno? ")
#     max = int(input("Jaká je Vaše nabídka v dolarech? "))
#     nabidky[vitez] = max
#     pokracovat = input("Jsou další nabízející? ano/ne. ")
# for davajici in nabidky:
#     if nabidky[davajici] > max:
#         vitez = davajici
#         max = nabidky[davajici]
#
# for davajici in nabidky:
#     if nabidky[davajici] == max:
#         print(f"{davajici}, {nabidky[davajici]}")
