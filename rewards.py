import pyautogui
import time
import random
import json
import os

def automacao_rewards():
    pesquisas_hoje = []

    while True:
        try:
            print('Deseja desligar o pc após o fim das pesquisas?')
            desligar_pc = int(input('1 - SIM | 2 - NÃO '))

            if desligar_pc in [1, 2]:
                if desligar_pc == 1:
                    #Timer de 40 minutos para garantir que a missão de 30 minutos no edge seja cumprida
                    os.system("shutdown /s /t 2400") 
                break

            else:
                print('Opção inválida! Escolha 1 ou 2.')

        except ValueError:
            print('Digite apenas NÚMEROS INTEIROS.')

    try: 
        with open('pesquisas.json', 'r', encoding='utf-8') as arquivo:
            pesquisas = json.load(arquivo)
            pesquisas_hoje = random.sample(pesquisas['termos'], k=30)

    except FileNotFoundError:
        print("Arquivo pesquisas.json não encontrado!")
        return

    print('O Script vai começar em 5 segundos...')
    print('CLIQUE NA JANELA DO EDGE AGORA')
    time.sleep(5)

    for termo in pesquisas_hoje:
        pyautogui.hotkey('alt', 'd')
        time.sleep(1)

        pyautogui.write(termo, interval=0.1)
        time.sleep(0.5)
        pyautogui.press('enter')

        espera = 15 + random.uniform(2, 10)
        print(f'Pesquisou: {termo}. Próxima pesquisa em {espera:.1f} segundos.')
        time.sleep(espera)

    print('Fim das pequisas. Aguarde a finalização do script...')

if __name__ == '__main__':
    automacao_rewards()