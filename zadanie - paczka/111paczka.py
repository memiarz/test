waga_elementu = int(input())
waga_paczki = 0
wyslane_paczki = 0
waga_ostatniego_elementu = 0
suma_pustych_kg = 0
puste_kg = 0
razem_kg = 0

while waga_elementu and waga_elementu <10:

    waga_paczki = waga_paczki + waga_elementu

    if waga_paczki < 20:
        print("Dobieram element")
        waga_ostatniego_elementu = waga_paczki

    elif waga_paczki == 20:
        print("Idealnie! Wysyłam")
        razem_kg = razem_kg + waga_paczki
        puste_kg = 20 - waga_paczki
        suma_pustych_kg = suma_pustych_kg + puste_kg
        wyslane_paczki = wyslane_paczki + 1
        waga_paczki = 0
        waga_ostatniego_elementu = 0

    else:
        print("Maksymalna waga paczki przekroczona! Odejmuję element i wysyłam")
        waga_paczki = waga_paczki - waga_elementu
        wyslane_paczki = wyslane_paczki + 1
        puste_kg = 20 - waga_paczki
        suma_pustych_kg = suma_pustych_kg + puste_kg
        razem_kg = razem_kg + waga_paczki
        waga_paczki = waga_elementu
        waga_ostatniego_elementu = waga_elementu


    waga_elementu = int(input())

    if waga_elementu == 404 and waga_ostatniego_elementu > 0:
        print("Koniec elementów! Wysyłam resztę.")
        # waga_paczki = waga_paczki - waga_elementu
        wyslane_paczki = wyslane_paczki + 1
        puste_kg = 20 - waga_ostatniego_elementu
        suma_pustych_kg = suma_pustych_kg + puste_kg
        razem_kg = razem_kg + waga_ostatniego_elementu


print()

if waga_elementu < 1:
    print("BŁĄD! Element waży za mało!\nKONIEC")


if waga_elementu > 10 and waga_elementu != 404:
    print("BŁĄD! Element za ciężki!\nKONIEC")



szablon_podsumowania = ("Ilość wysłanych paczek to {} szt. Razem wysłano {} kg. Puste kilogramy: {}")
podsumowanie = szablon_podsumowania.format(wyslane_paczki, razem_kg, suma_pustych_kg)
print(podsumowanie)




















### === WŁAŚCIWIE NA GOTOWO, OPRÓCZ WSKAZANIA NAJBARDZIEJ PUSTEJ PACZKI

# waga_elementu = int(input())
# waga_paczki = 0
# wyslane_paczki = 0
# waga_ostatniego_elementu = 0
# suma_pustych_kg = 0
# puste_kg = 0
# razem_kg = 0
#
# while waga_elementu and waga_elementu <10:
#
#     waga_paczki = waga_paczki + waga_elementu
#
#     if waga_paczki < 20:
#         print("Dobieram element")
#         waga_ostatniego_elementu = waga_paczki
#
#     if waga_paczki == 20:
#         print("Idealnie! Wysyłam")
#         razem_kg = razem_kg + waga_paczki
#         puste_kg = 20 - waga_paczki
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         wyslane_paczki = wyslane_paczki + 1
#         waga_paczki = 0
#         waga_ostatniego_elementu = 0
#
#
#     if waga_paczki > 20:
#         print("Maksymalna waga paczki przekroczona! Odejmuję element i wysyłam")
#         waga_paczki = waga_paczki - waga_elementu
#         wyslane_paczki = wyslane_paczki + 1
#         puste_kg = 20 - waga_paczki
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         razem_kg = razem_kg + waga_paczki
#         waga_paczki = waga_elementu
#         waga_ostatniego_elementu = waga_elementu
#
#
#     waga_elementu = int(input())
#
#     if waga_elementu == 404:
#         print("Koniec elementów!")
#         # waga_paczki = waga_paczki - waga_elementu
#         if waga_ostatniego_elementu > 0:
#             wyslane_paczki = wyslane_paczki + 1
#             puste_kg = 20 - waga_ostatniego_elementu
#             suma_pustych_kg = suma_pustych_kg + puste_kg
#             razem_kg = razem_kg + waga_ostatniego_elementu
#             print("Wysyłam resztę")
#
# print()
#
# if waga_elementu < 1:
#     print("BŁĄD! Element waży za mało!\nKONIEC")
#
#
# if waga_elementu > 10 and waga_elementu != 404:
#     print("BŁĄD! Element za ciężki!\nKONIEC")
#
#
#
# szablon_podsumowania = ("Ilość wysłanych paczek to {} szt. Razem wysłano {} kg. Puste kilogramy: {}")
# podsumowanie = szablon_podsumowania.format(wyslane_paczki, razem_kg, suma_pustych_kg)
# print(podsumowanie)




test test test

tst333333






### === DZIAŁA (z 0 jako końcem pliku) === ####

# waga_elementu = int(input())
# waga_paczki = 0
# wyslane_paczki = 0
# waga_ostatniego_elementu = 0
# suma_pustych_kg = 0
# puste_kg = 0
# razem_kg = 0
#
# while waga_elementu and waga_elementu <10:
#
#     waga_paczki = waga_paczki + waga_elementu
#
#     if waga_paczki < 20:
#         print("Dobieram element")
#         waga_ostatniego_elementu = waga_paczki
#
#     if waga_paczki == 20:
#         print("Idealnie! Wysyłam")
#         razem_kg = razem_kg + waga_paczki
#         puste_kg = 20 - waga_paczki
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         wyslane_paczki = wyslane_paczki + 1
#         waga_paczki = 0
#         waga_ostatniego_elementu = 0
#
#
#     if waga_paczki > 20:
#         print("Waga przekroczona! Odejmuję i wysyłam")
#         waga_paczki = waga_paczki - waga_elementu
#         wyslane_paczki = wyslane_paczki + 1
#         puste_kg = 20 - waga_paczki
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         razem_kg = razem_kg + waga_paczki
#         waga_paczki = waga_elementu
#         waga_ostatniego_elementu = waga_elementu
#
#
#     waga_elementu = int(input())
#
#     if waga_elementu < 1:
#         print("Koniec elementów!")
#         # waga_paczki = waga_paczki - waga_elementu
#         if waga_ostatniego_elementu > 0:
#             wyslane_paczki = wyslane_paczki + 1
#             puste_kg = 20 - waga_ostatniego_elementu
#             suma_pustych_kg = suma_pustych_kg + puste_kg
#             razem_kg = razem_kg + waga_ostatniego_elementu
#             print("Wysyłam resztę")
#
#
#
# if waga_elementu < 1:
#     print("Element waży za mało!")
#     print("KONIEC")
#
# if waga_elementu > 10:
#     print("Element za ciężki!")
#     print("Koniec")
#
#
#
# szablon_podsumowania = ("Ilość wysłanych paczek to {} sztuk. Razem wysłano {} kg. Puste kilogramy: {}")
# podsumowanie = szablon_podsumowania.format(wyslane_paczki, razem_kg, suma_pustych_kg)
# print(podsumowanie)



# waga_elementu = int(input())
# waga_paczki = 0
# wyslane_paczki = 0
# razem_kg = 0
# suma_pustych_kg = 0
# koniec = input()
# ostatni_element = 0
# ostatnia_pelna_paczka = 0
#
#
#
# while waga_elementu and waga_elementu < 10: #musi być >1?
#
#     waga_paczki = waga_paczki + waga_elementu
#
#     if waga_paczki < 20:
#         print("Za mało! Dokładam element")
#         ostatni_element = waga_paczki
#
    # if waga_paczki == 20:
    #     print("Idealnie! Wysyłam")
    #     razem_kg = razem_kg + waga_paczki
    #     puste_kg = 20 - waga_paczki
    #     suma_pustych_kg = suma_pustych_kg + puste_kg
    #     wyslane_paczki = wyslane_paczki + 1
    #     waga_paczki = waga_paczki - waga_paczki
    #     ostatni_element == 0
#
#     if waga_paczki > 20:
#         print("Waga przekroczona! Odejmuję i wysyłam")
#         waga_paczki = waga_paczki - waga_elementu
#         puste_kg = 20 - waga_paczki
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         razem_kg = razem_kg + waga_paczki
#         wyslane_paczki = wyslane_paczki + 1
#         ostatnia_pelna_paczka = waga_paczki
#
#         waga_paczki = waga_elementu
#         ostatni_element = waga_paczki
#
#     waga_elementu = int(input())
#
#     if waga_elementu == 0:
#         print ("kurwa")
#         puste_kg = 20 - ostatnia_pelna_paczka
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         razem_kg = razem_kg + ostatnia_pelna_paczka
#         wyslane_paczki = wyslane_paczki + 1
#
#         print("Wysyłam ostatni element")
#         wyslane_paczki = wyslane_paczki + 1
#         puste_kg = 20 - ostatni_element
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         razem_kg = razem_kg + ostatni_element
#
#
#
#
#
#
# print()
#
#
#
# if waga_elementu: False
# print("Nieprawidłowa waga elementu")
# # if ostatni_element > 0:
# #     print("Wysyłam ostatni element")
# #     puste_kg = 20 - ostatni_element
# #     suma_pustych_kg = suma_pustych_kg + puste_kg
# #     razem_kg = razem_kg + ostatni_element
# #     wyslane_paczki = wyslane_paczki + 1
#
# print()
#
# szablon_podsumowania = ("Ilość wysłanych paczek to {} sztuk. Razem wysłano {} kg. Puste kilogramy: {}")
# podsumowanie = szablon_podsumowania.format(wyslane_paczki, razem_kg, suma_pustych_kg)
# print(podsumowanie)





#
# waga_elementu = int(input())
# waga_paczki = 0
# wyslane_paczki = 0
# razem_kg = 0
# suma_pustych_kg = 0
# koniec = input()
# ostatni_element = waga_paczki



# while waga_elementu and waga_elementu > 1: #musi być >1?
#
#     waga_paczki = waga_paczki + waga_elementu
#
#     if waga_paczki < 20:
#         print("Za mało! Dokładam element")
#         ostatni_element = waga_paczki
#
#     if waga_paczki == 20:
#         print("Idealnie! Wysyłam")
#         razem_kg = razem_kg + waga_paczki
#         puste_kg = 20 - waga_paczki
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         wyslane_paczki = wyslane_paczki + 1
#         waga_paczki = waga_paczki - waga_paczki
#
#     if waga_paczki > 20:
#         print("Waga przekroczona! Odejmuję i wysyłam")
#         waga_paczki = waga_paczki - waga_elementu
#         puste_kg = 20 - waga_paczki
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         razem_kg = razem_kg + waga_paczki
#         wyslane_paczki = wyslane_paczki + 1
#         ostatnia_paczka = waga_paczki
#         waga_paczki = waga_elementu
#
#
#     waga_elementu = int(input())
#
#     if waga_elementu == 0:
#         print("Element waży za mało!")
#         print("Błąd: Element musi mieć co najmniej 1kg!")
#         print("Wysyłam ostatni element")
#
#
#
#         puste_kg = 20 - ostatni_element
#         suma_pustych_kg = suma_pustych_kg + puste_kg
#         razem_kg = razem_kg + ostatni_element
#         wyslane_paczki = wyslane_paczki + 1
#
#
#     if waga_elementu > 10:
#         print("Element waży za dużo!")
#         break
#
#
# print()
#
# # if waga_elementu == 0:
# #
# #     print("Błąd: Element musi mieć co najmniej 1kg!")
# #     print("Wysyłam ostatni element")
# #     puste_kg = 20 - ostatni_element
# #     suma_pustych_kg = suma_pustych_kg + puste_kg
# #     razem_kg = razem_kg + ostatni_element
# #     wyslane_paczki = wyslane_paczki + 1
#
#
# print()
#
# szablon_podsumowania = ("Ilość wysłanych paczek to {} sztuk. Razem wysłano {} kg. Puste kilogramy: {}")
# podsumowanie = szablon_podsumowania.format(wyslane_paczki, razem_kg, suma_pustych_kg)
# print(podsumowanie)


## Przykład na czysto



# waga_elementu = int(input())
#
# count_paczek = 0
# suma_kg = 0
# ile_kg_w_paczce = 0
#
# while waga_elementu:
#     suma_kg += waga_elementu
#     ile_kg_w_paczce += waga_elementu
#     if ile_kg_w_paczce > 20:
#        ile_kg_w_paczce -= waga_elementu
#        count_paczek +=1
#        #teraz trzeba wsadzić ten wyjęty element do nowej paczki
#        ile_kg_w_paczce = waga_elementu
#        print("Paczka została wysłana")
#
#
#     waga_elementu = int(input())
#
# szablon_podsumowania = ("Ilość wysłanych paczek to {} sztuk. Razem wysłano {} kg")
# podsumowanie = szablon_podsumowania.format(count_paczek, suma_kg)
# print(podsumowanie)



## Druga wersja na czysto

# waga_elementu = int(input())
#
# count_paczek = 0
# suma_kg = 0
# ile_kg_w_paczce = 0
#
# while waga_elementu:
#      suma_kg += waga_elementu
#      ile_kg_w_paczce += waga_elementu
#      if ile_kg_w_paczce >= 20:
#          if ile_kg_w_paczce > 20:
#              ile_kg_w_paczce -= waga_elementu
#              ile_kg_w_paczce = waga_elementu
#
#          else:
#              ile_kg_w_paczce = 0
#          count_paczek +=1
#          print("Paczka została wysłana")
#      waga_elementu = int(input())
# szablon_podsumowania = ("Ilość wysłanych paczek to {} sztuk. Razem wysłano {} kg")
# podsumowanie = szablon_podsumowania.format(count_paczek, suma_kg)
# print(podsumowanie)











# # import sys
# # sys.argv moźna wczytywać liczbę paczek którą ma się do wysłania
#
# waga_elementu = int(input())
#
# count_paczek = 0
# suma_kg = 0
# ile_kg_w_paczce = 0
#
# while waga_elementu:
# #pierw czy waga elementu nie jest 0
# #while rzutowane jest na bool
#     suma_kg += waga_elementu #zlicza łączną wagę wszystkich paczek, ale jeszcze nie dodało się nic do paczki
# #na razie nie mamy nic dodanego do paczki
#     ile_kg_w_paczce += waga_elementu
# #jeżeli mamy element w paczce to decydujemy: czy dalej wysłać, czy jeszcze dołożyć
#    # if ile_kg_w_paczce <= 20: #nie trzeba tego warunku robić?
#     if ile_kg_w_paczce > 20: #jeżeli dodamy tu też = to musimy w pętli sprawdzić jeszcze jednego if-a
#        ile_kg_w_paczce -= waga_elementu
#        count_paczek +=1 #count paczek +1 to już wysłanie elementu
#        #teraz trzeba wsadzić ten wyjęty element do nowej paczki
#        ile_kg_w_paczce = waga_elementu
#        print("Paczka została wysłana")
#        #w jakich jeszcze innych sytuacjach można wysłaś paczkę?
#
#     waga_elementu = int(input())
#
# szablon_podsumowania = ("Ilość wysłanych paczek to {} sztuk. Razem wysłano {} kg")
# podsumowanie = szablon_podsumowania.format(count_paczek, suma_kg)
# print(podsumowanie)





# waga_elementu = int(input())
#
# count_paczek = 0
# suma_kg = 0
# ile_kg_w_paczce = 0
#
# while waga_elementu:
#      suma_kg += waga_elementu
#      ile_kg_w_paczce += waga_elementu
#      if ile_kg_w_paczce >= 20: # robimy teraz od razu sprawdzanie z =
#          if ile_kg_w_paczce > 20:
#              ile_kg_w_paczce -= waga_elementu
#              ile_kg_w_paczce = waga_elementu
#
#          #teraz musimy zobaczyć, którą linijkę z potrzedniego przykładu musimy usunąć
#          #jeżlei nowa paczka to równe 20, to następna jest już pusta
#          else:
#              ile_kg_w_paczce = 0
#          count_paczek +=1
#          print("Paczka została wysłana")
#          # jest już ograne wysyłanie paczek
# # trzeba dodać kiedy waga elementu = 0
# # rozrysowywanie problemów na kartce?
#      waga_elementu = int(input())
# szablon_podsumowania = ("Ilość wysłanych paczek to {} sztuk. Razem wysłano {} kg")
# podsumowanie = szablon_podsumowania.format(count_paczek, suma_kg)
# print(podsumowanie)





### === PRZYKLAD 2

#while waga_elementu będzie się wykonywać tylko wtedy, kiedy waga elementu będzie rózna od 0 (bo to booleen)

#dodawanie inputu już w pętli

# w każdym if wstawiać print by zobaczyć w którą pętle wchodzi, np print("1")

# waga_elementu = int(input())
# waga_paczki = 0
# waga_paczki += waga_elementu
# paczki_wyslane = 0
# pierwszy_element = 1
# kg_wyslane = 0
# najlzejsza_paczka = 0 #powinno być 20
#
# while waga_elementu and pierwszy_element == 1:      #while sprawdza, czy waga elementu jest true
#
#
# waga_elementu = input() #pobranie kolejnego elementu


# 1h:22min(
#
# )





















