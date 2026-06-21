import pyautogui
import time
import random
import json
import os
import sys

pyautogui.FAILSAFE = True 

def solicitar_desligamento():
    while True:
        opcao = input('Deseja desligar o PC após o fim? (1-SIM | 2-NÃO): ').strip()
        if opcao == '1':
            return True
        elif opcao == '2':
            return False
        print('Opção inválida!')

def executar_pesquisas(termos):
    print('O Script vai começar em 5 segundos... Mude para o navegador.')
    time.sleep(5)

    for i, termo in enumerate(termos, 1):
        pyautogui.hotkey('alt', 'd')
        time.sleep(0.5)
        
        pyautogui.write(termo,interval=0.1)
        pyautogui.press('enter')

        espera = random.uniform(15, 25)
        print(f'[{i}/20] Pesquisado: "{termo}". Aguardando {espera:.1f}s...')
        time.sleep(espera)

def main():
    if not os.path.exists('pesquisas.json'):
        print("Erro: arquivo 'pesquisas.json' não encontrado.")
        return

    with open('pesquisas.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        termos = data.get('termos', [])

    if len(termos) < 20:
        print("Erro: O JSON precisa de pelo menos 20 termos.")
        return

    deve_desligar = solicitar_desligamento()
    
    try:
        executar_pesquisas(random.sample(termos, k=20))
        print('Concluído!')
        
        if deve_desligar:
            print('Desligando em 40 minutos...')
            os.system("shutdown /s /t 2400")
            
    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário.")
        sys.exit()

if __name__ == '__main__':
    main()