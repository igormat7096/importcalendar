#Import biblioteca do calendario
import calendar

mes = int(input("Informe o número do mês desejado:  "))
ano = int(input("Informe o ano desejado:  "))

if mes > 0 and mes <= 12:
   print(calendar.month)
else: 
   print("Mês invalido.")
if ano > 1900 and ano <= 2030:
   print(calendar.month(ano,mes))
else: 
   print("Ano invalido.")


