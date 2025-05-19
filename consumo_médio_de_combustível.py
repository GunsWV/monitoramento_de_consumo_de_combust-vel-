#Neste exercício, vamos revisar os principais conceitos de entrada de dados, operadores matemáticos e condicionais em Python com uma aplicação externa para o mundo automotivo!

#Crie um programa em Python que ajude os motoristas a calcular o consumo médio de combustível do seu veículo e forneça uma mensagem com base na eficiência da média obtida.

nome_do_cliente = input("Seja bem vindo a nossa central de atendimento, aqui ajudaremos você a calcular e monitorar seu consumo de combustível. Qual seu nome por gentileza? :")

distancia_km = float(input("Qual a distancia percorrida? :"))

quant_combustivel_gasto_litros = float(input("Quanto foi gasto de combustivel em litros? :"))

consumo_medio = distancia_km / quant_combustivel_gasto_litros

print(f"o consumo médio do seu veículo é: {consumo_medio}")

if consumo_medio < 8.0:
    print("Seu veículo tem um alto consumo 🚨")
elif 8.0 < consumo_medio < 12.0:
    print("Seu veículo tem um consumo moderado⚠️")
else: 
    print("Seu veículo tem um consumo econômico! 🚗💨")
