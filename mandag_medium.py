import math

##Oppgave 1##
''' Hvis du  blir tilbudt 300 krone for å vaske et hus, ville du gjort det
da? hva om du ble tilbudt dette i 2 månader, hvor betalingen ville økes 15%
hver dag. Det vil si kr300 første dag, 345 andre dag, kr396.75 neste dag, osv.  '''


### your task##
'''Lag en funksjon som regner ut total lønn etter 2 måneder, og lønn for 
dag 15, 30, 45 og 50. Bruk print() for å vise disse verdiene i terminalen'''

# Variabler for lønn, dager, prosent og total
print("\nOppgave 1")
pay = 300
days = range(1,60)
interest = 1.15
paydays = [15, 30, 45, 50]
total = 0

for day in days:
  pay *= 1.15
  total += pay
  pay = int(pay)
  if day in paydays:
    print("Lønn på dag " + str(day) + ": " + str(pay) + "kr")

total = int(total)
print("Totalen etter to måneder er " + str(total) + "kr")





##Oppgave 2##
''' Opprett en funksjon som kan tegne følgende figur i terminalen:
*
**
***
****
*****
******
*******
********
*********
**********
***********
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********
***********
'''
print("\nOppgave 2")

def figur(length, figure):

  length = int(length)
  counter = range(1, length)
  space = " "

  for num in counter:
    print(figure * num)
  length -= 1
  for num in counter:
    length -= 1
    print(space * length + figure * num)


figur(input("Hvor stor?:\n"), input("Hvilken figur?:\n"))






##Oppgave 3##
''' Opprett en funksjon som kan printe alle primtall i variabel prime_numbers '''
print("\nOppgave 3")

def primeNum():
  prime_numbers = [1, 5, 6, 7, 10, 11, 19, 23, 25, 26, 31, 26, 37, 40, 43, 67, 73, 99, 101]
  for num in prime_numbers:
    print(num)

primeNum()



















""" oppgaveNr = input("Velg oppgave!\n1, 2, 3\n")
if oppgaveNr == "1":
  print("\nOppgave 1")
  pay = 300
  days = range(1,60)
  interest = 1.15
  paydays = [15, 30, 45, 50]
  total = 0

  for day in days:
    pay *= 1.15
    total += pay
    pay = int(pay)
    if ((day==paydays[0]) or (day==paydays[1]) or (day==paydays[2]) or (day==paydays[3])):
      print("Lønn på dag " + str(day) + ": " + str(pay) + "kr")

  total = int(total)
  print("Totalen etter to måneder er " + str(total) + "kr")

elif oppgaveNr == "2":
    print("\nOppgave 2")
    counter = range(1, 11)
    figure = "*"
    for num in counter:
      print(figure * num)

elif oppgaveNr == "3":
  print("\nOppgave 3")
  prime_numbers = [1, 5, 6, 7, 10, 11, 19, 23, 25, 26, 31, 26, 37, 40, 43, 67, 73, 99, 101]
  for num in prime_numbers:
    print(num)

else:
  print("Nope!") """
