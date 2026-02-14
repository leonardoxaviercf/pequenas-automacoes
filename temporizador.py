import os

try:
    minutos = int(input('Em quanto tempo deseja desligar a máquina? [min] '))
    segundos = minutos * 60
    
    print(f'Agendado: O PC desligará em {minutos} minutos ({segundos}s).')
    os.system(f'shutdown /s /t {segundos}')
    
except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")