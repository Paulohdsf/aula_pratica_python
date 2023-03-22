#num1 = int(input('digite um numero:'))
#num2 = int(input('digite segundo numero:'))
#total = num1 + num2
#print(f"O valor da soma é"{total})


#salario = int(input("insira seu salario:"))

#if salario <= 1000:
  #aumento = salario + (salario*0.2)
  #print(f"seu salario sofreo um aumento de 20% totalinzando {aumento}")
#elif salario <= 5000:#aumento de 10%
  #aumento = salario + (salario*0.1)
#print(f"seu salario sofreo um aumento de 10% totalinzando {aumento}")

#boletim

#nome = input("digite seu nome:")
#nota1 = int(input("digite sua primeira nota:"))
#nota2 = int(input("digite sua segunda nota:"))
#media = (nota1 + nota2)/2

#if media >=6:
  #print("aprovado")
#else: 
  #print("reprovado")

#nome = input("qual seu nome: ")
#idade = int(input("digite sua idade: "))

#if  idade >=18:
 # print(f"olar {nome} voce e maior de idade")
#else:
 # print(f"ola {nome} voce e menor de idade")

#case tabuada
#tabuada = int(input("qual tabuada voce deseja:"))
#cont = 9
#soma = 0
#while cont !=0:
 # soma = tabuada + cont
  #print(f"{tabuada} + {cont} = {soma}")
  #cont = cont -1

#while  True:
 # fruta = input("insira o nome da fruta: ")
  #parada = input("deseja continuar S/N: ").upper()
  #if  parada != "S":
   # break

while True:
  nome = input("insira seu nome: ")
  idade = int(input("insira sua idade: "))
  estado = input("insira seu estadao: ")

  parada = input("deseja realiza mais um cadastro S/N: ").upper()
  if parada != "S":
    break
