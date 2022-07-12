from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
#import requests


chrome_options = Options()
chrome_options.add_argument("-headless")
cdriver = webdriver.Chrome(options = chrome_options)


def qualnum(x):
    
    if x == '1':
        return 1

    if x == '2':
        return 2

    if x == '3':
        return 3

    if x == '4':
        return 4

    if x == '5':
        return 5

    if x == '6':
        return 6

    if x == '7':
        return 7

    if x == '8':
        return 8

    if x == '9':
        return 9

    if x == '10':
        return 10

    if x == '11':
        return 11

    if x == '12':
        return 12

    if x == '13':
        return 13
    if x == '14':
        return 14

def qualcor(x):
    ## VERMELHOS
    if x == '1':
        return 'V'
    if x == '2':
        return 'V'
    if x == '3':
        return 'V'
    if x == '4':
        return 'V'
    if x == '5':
        return 'V'
    if x == '6':
        return 'V'
    if x == '7':
        return 'V'
    ## PRETOS
    if x == '8':
        return 'P'
    if x == '9':
        return 'P'
    if x == '10':
        return 'P'
    if x == '11':
        return 'P'
    if x == '12':
        return 'P'
    if x == '13':
        return 'P'
    if x == '14':
        return 'P'

def qualresultado(cor1, cor2):
    c1 = 'P'
    c2 = 'V'
    if cor1 > 6:
            return c2
    if cor1 > 9 and cor2 <= 5:
        return c2
    if cor1 <= 6 and cor2 >= 8:
        return c1
    if cor1 == 3 and cor2 >= 7:
        return c1
    if cor1 == 5 and cor2 == 7:
        return c1
    if cor2 >= 9 and cor1 == 4:
        return c1
    if cor1 == 6 and cor2 == 6:
        return c1
    if cor1 == 4 and cor2 >= 6:
        return c2
    elif cor1 == cor2:
        return '''
        Fazendo análise mais detalhada
        Em breve o sinal virá, fique atento!
        '''
    else:
        return '''
        Fazendo análise mais detalhada
        Em breve o sinal virá, fique atento!
        '''

def msg(m):
    if m == 'V':
        return '''
        ✅ ENTRADA CONFIRMADA ✅
        #     🎯 Aposte no 🔴 (VERMELHO)
        #     🛡 Proteger no ⚪ (BRANCO)
        #     ⚠ Entrar após a próxima rodada ⚠
        '''
    if m == 'P':
        return '''
        ✅ ENTRADA CONFIRMADA ✅ 
        #         🎯 Aposte no ⚫ (PRETO)
        #         🛡 Proteger no ⚪ (BRANCO)
        #         ⚠ Entrar após a próxima rodada ⚠
        #         
        '''
    else:
        return'''
    Fazendo análise mais detalhada
    #         Em breve o sinal virá, fique atento!
    '''
    

while True:
    cdriver.get('https://blaze.com/pt/games/double')
    
    extrairdados = cdriver.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
    
    numlist = extrairdados.split()
    
    pd = numlist[0:16]
    
    mapeando2 = map(qualcor, pd)
    
    finalcolor = list(mapeando2)
    
    print(finalcolor)    
    
    black = [x for x in finalcolor if x == 'V']
    red = [d for d in finalcolor if d == 'P']
    
    tamanho_black = len(black)
    tamanho_red = len(red)
    
    sinal_final = qualresultado(tamanho_black, tamanho_red)
    
    print(sinal_final)
    
    retorno = f'{msg(sinal_final)}'
    
    aguardar = time.sleep(20)