# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:20:05 2019
SadFotovoltaicoAlphaVersion
@author: sidnei lopes ribeiro

Com base em dados de Boreal Solar pesquisados por Mario Benassi Junior
e em dados da Elektro S.A., pesquisados por Luiz Carlos da Silva
"""

# import tkinter as tk
import matplotlib.pyplot as plt

## Entrada de dados ##
'''
Variáveis - Área: m2; 
            Potência: Kw/h; 
            Conta de Energia: R$.
'''

print (" ")
print ("Esclarecimento - Os dados vieram das empresa Boreal Solar (Mario) e Elektro (Luiz)")
print ("'Fins estritamente educacionais'") 
print ("'Não somos seus representantes comerciais!'")

## Declaração e inicialização de variáveis
inv1 = 0.0 # capital investido na empresa 1 - boreal solar
inv2 = 0.0 # capital investido na empresa 2 - Elektro - S.A
conta = 0.0
kwp = 0.0 # Kilowatt hora pico (potência do sistema)
numero1 = 0 # número de painéis
numero2 = 0
# Empresa 1# 
SEG_1 = 1.8105 # margem de segurança da empresa 1 (81,05%)
SEG_2 = 2.64 # margem de segurança da empresa 2 (164%)
PAINEL_1 = 0.340 # potência em watts (340 w)
PAINEL_2 = 0.330 # potência em watts (330 w)
PRECO_1 = 1117.370892
PRECO_2 = 1071.84375 # preço de cada painel solar
AREA = 2.64 # área de cada painel ; 2,64 m2

#n Entrada dos dados#

potencia = input("Qual é a potência do sistema em KW pico/hora? ")
potencia = int(potencia)
area_2 = input("Qual é a área total disponível em m2? ")
area_2 = int (area_2)
print (" ")
print ("Agora, para saber o tempo no qual o sistema se pagará... ")
conta = input ("... digite o valor da conta de energia deste estabelecimento: ")
conta = int(conta)
print (" ")

# Cálculos
kwp_1 = potencia * SEG_1
kwp_2 = potencia * SEG_2
numero1 = kwp_1/PAINEL_1
numero2 = kwp_2/PAINEL_2
cobertura1 = AREA * numero1
cobertura2 = AREA * numero2
inv1 = PRECO_1 * numero1
inv2 = PRECO_2 * numero2
payback_meses1 =  inv1/conta
payback_ano1 = payback_meses1/12
payback_meses2 =  inv2/conta
payback_ano2 = payback_meses2/12

## Apresentação de resultados

if cobertura1 and cobertura2 < area_2:
   print ("Resultados para a empresa Boreal Solar") 
   print ("A área coberta será de .......... %.2f"% (cobertura1), "metros")
   print ("A potência do sistema será de ... %.2f"% (kwp_1), "Kilowatt/hora pico")
   print ("O valor a investir será de R$ %.2f"% (inv1))
   print ("O investimento será pago em %.1f"% (payback_meses1), "meses.")
   print ("Isso equivale a %.1f"% (payback_ano1), "anos.")   
   print ("")
   print ("Resultados para a Elektro S.A.") 
   print ("A área coberta será de .......... %.2f"% (cobertura2), "metros")
   print ("A potência do sistema será de ... %.2f"% (kwp_2), "Kilowatt/hora pico")
   print ("O valor a investir será de R$ %.2f"% (inv2))
   print ("O investimento será pago em %.1f"% (payback_meses2), "meses.")
   print ("Isso equivale a %.1f"% (payback_ano2), "anos.")   
   print ("")
else:
   print ("A área é insuficiente para o projeto.")
   print ("Por favor, refaça seus cálculos")

# Plotagem dos gráficos
# Apresentação dos mesmos dados em formato gráfico"   

# 1. Gráfico da área de cobertura
x = [1, 2]
y = [cobertura1, cobertura2]
     
#títulos do gráfico
titulo = "1. Área de Cobertura dos painéis fotovoltaicos (m2)"
eixox = "1. Boreal Solar, 2. Elektro"
eixoy = "(m2)"

#impresssão das legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()   


# 2. Gráfico da geração em KW pico
x = [1, 2]
y = [kwp_1, kwp_2]
titulo = "2. Geração máxima em Kilowatt pico - KWp"
eixox = "1. Boreal Solar, 2. Elektro"
eixoy = "(KW pico)"

#impresssão das legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()   

# 3. Gráfico dos investimentos (R$)
x = [1, 2]
y = [inv1, inv2]
titulo = "3. Investimentos em Reais (R$)"
eixox = "1. Boreal Solar, 2. Elektro"
eixoy = "(R$)"

#impresssão das legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()   

# 4. Gráfico do Payback simples (tempo em meses)
x = [1, 2]
y = [payback_meses1, payback_meses2] 
titulo = "4. Payback Simples - tempo em que o investimento se paga (em meses)"
eixox = "1 e 2. Boreal Solar, 3 e 4. Elektro"
eixoy = "(meses)"

#impresssão das legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show() 

# 5. Gráfico do Payback simples (em anos)
x = [1, 2]
y = [payback_ano1, payback_ano2]  
titulo = "5. Payback Simples: tempo em que o investimento se paga (em anos)"
eixox = "1. Boreal Solar, 2. Elektro"
eixoy = "(anos)"

#impresssão das legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()

print ("")
print ("Informação de suporte à decisão do gestor ou proprietário: ")
print ("")
print ("O sistema da empresa Elektro S.A., devido ao seu superdimensionamento,")
print ("também propiciará um fornecimento de, no máximo, 65,6 KWp à rede elétrica")
print ("que poderá abastecer as residências vizinhas de eletricidade e")
print ("se reverter em renda à escola, caso a legislação continue como está.")

# return sid7b1