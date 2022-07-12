from ast import Return
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests


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
    # if cor1 > 9 and cor2 <= 5:
    #     return c2
    # if cor1 <= 6 and cor2 >= 8:
    #     return c1
    # if cor1 == 3 and cor2 >= 7:
    #     return c1
    # if cor1 == 5 and cor2 == 7:
    #     return c1
    # if cor2 >= 9 and cor1 == 4:
    #     return c1
    # if cor1 == 6 and cor2 == 6:
    #     return c1
    # if cor1 == 4 and cor2 >= 6:
    #     return c2
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
        🔔⚠️🚨Atenção🚨⚠️🔔 
        ✅Entrada confirmada! 🔴
        ✅Proteção no: ⚪️
        ✅Ate Gale 2 🐓🐓 
        🎲Jogue agora Blaze Double🎲  
        (https://blaze.com/r/PZ9aVa) 
        By: @DANBLAZE
        '''
    if m == 'P':
        return '''
        🔔⚠️🚨Atenção🚨⚠️🔔 
        ✅Entrada confirmada! ⚫
        ✅Proteção no: ⚪️
        ✅Ate Gale 2 🐓🐓 
        🎲Jogue agora Blaze Double🎲  
        (https://blaze.com/r/PZ9aVa) 
        by: @DANBLAZE
        '''
    else:
        return'''
    Fazendo análise mais detalhada
    #         Em breve o sinal virá, fique atento!
    '''
    
def bot_telegram(bot):
    token = '5543259990:AAEGAWO-LnGzAGI7H8-YxohzFYA82fSmPWA'
    chat_id = '-1001626866194'
    mensagem = retorno
    

def vou_p(x):
    if x == 'V':
        return '🔴 (VERMELHO)'
    if x == 'P':
        return '⚫ (PRETO)'


def green(txt):
    if txt == guardasinal:
            return '✅✅ GREEN ✅✅'
    elif txt != guardasinal:
        return f'REALIZAR GALE 1⃣  NO {vou_p(sinal_final)}'


def green2(txt):
    
    if txt == guardasinal:
        return '✅✅ GREEN ✅✅'
    elif txt != guardasinal:
        return f'REALIZAR GALE 2⃣  NO {vou_p(sinal_final)}'

def green3(txt):
    if txt1 == guardasinal:
        return '✅✅ GREEN ✅✅'
    elif txt1 != guardasinal:
        return f'❌❌ LOSS ❌❌'

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
    
    url = ('https://api.telegram.org/bot{5460372550:AAEMoZWuuERMawqYRaW-X-F5ycQCJPXSgBQ}/sendMessage?chat_id=-1001626866194&text={retorno}')
    

    resp = requests.get(url)
    guardasinal = sinal_final
    
    espproximo = time.sleep(60)
    
    cdriver.get('https://blaze.com/pt/games/double')
    
    htc = time.sleep(3)
    
    pegardados7 = cdriver.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
    
    listanum7 = pegardados7.split()
    
    pd7 = listanum7[0:16]
    doc = time.sleep(3)
    dot = map(qualcor, pd7)
    
    retornofinal123 = list(dot)
    ret3 = retornofinal123 [0]
    
    qwd = green(ret3)
    
    url2 = ('https://api.telegram.org/bot{5460372550:AAEMoZWuuERMawqYRaW-X-F5ycQCJPXSgBQ}/sendMessage?chat_id= -1001626866194&text={qwd}')
    
    resp2 = requests.get(url2)
    
    if qwd != '✅✅ GREEN ✅✅':
        aguardar30 = time.sleep(30)

        cdriver.get('https://blaze.com/pt/games/double')
        htf = time.sleep(3)
        pegardados8 = cdriver.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

        pg8 = pegardados8.split()

        pd8 = pg8[0:16]
        htk = time.sleep(3)
        art4 = list(map(qualcor, pd8))

        finalret8 = art4[0]

        ret4 = finalret8
        
    repassando = sedeugreen2(ret4)
    
    url3 = ('https://api.telegram.org/bot{5460372550:AAEMoZWuuERMawqYRaW-X-F5ycQCJPXSgBQ}/sendMessage?chat_id= -1001626866194&text={repassando}')
    
    resp3 = requests.get(url3)
    
    if repassando != '✅✅ GREEN ✅✅':
        aguardar40 = time.sleep(30)

        cdriver.get('https://blaze.com/pt/games/double')
        dot = time.sleep(3)
        pegardados9 = cdriver.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

        pg9 = pegardados9.split()

        pd9 = pg9[0:16]
        tkd = time.sleep(5)
        art5 = map(qualcor, pd9)

        finalret9 = list(art5)

        ret5 = finalret9[0]
            
        repassando9 = sedeugreen3(ret5)
    
    url4 = ('https://api.telegram.org/bot{5460372550:AAEMoZWuuERMawqYRaW-X-F5ycQCJPXSgBQ}/sendMessage?chat_id= -1001626866194&text={repassando9}')
    
    resp5 = requests.get(url4)
    
    aguardar = time.sleep(180)