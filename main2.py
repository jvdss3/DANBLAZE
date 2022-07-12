from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import requests





Chrome_options = Options()
Chrome_options.add_argument("-headless")
cdirver = webdriver.Chrome(options = Chrome_options)


while True:
    cdirver.get('https://blaze.com/pt/games/double')
    
    
    extrairdados = cdirver.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
    
    listanum = extrairdados.split()
    
    def qualnum(x):
        if x == '1':
            return 1
        if x == '2':
            return 2
        if x == '3':
            return 3
        if x == '4':
            return
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
        #PRETO
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
    
    
    pd = listanum [0:16]
    mapeando = map(qualcor,pd)
    
    finalcolor = list(mapeando)
    
    print(finalcolor)
    
    black = [x for x in finalcolor if x == 'P']
    red = [x for x in finalcolor if x == 'V']
    
    tamanho_black = len(black)
    tamanho_red = len(red)

    
    def qualresultado(cor1,cor2):
        c1 = 'P'
        c2 = 'V'
        if cor1 > 6:
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
            🎯 Aposte no 🔴 (VERMELHO)
            🛡 Proteger no ⚪ (BRANCO)
            ⚠ Entrar após a próxima rodada ⚠
            '''
        if m == 'P':
            return '''
            ✅ ENTRADA CONFIRMADA ✅ 
            🎯 Aposte no ⚫ (PRETO)
            🛡 Proteger no ⚪ (BRANCO)
            ⚠ Entrar após a próxima rodada ⚠
            '''

        if m == '''
            Fazendo análise mais detalhada
            Em breve o sinal virá, fique atento!
            ''':
            return '''
            Fazendo análise mais detalhada
            Em breve o sinal virá, fique atento!
            '''

    sinal_final = qualresultado(tamanho_black,tamanho_red)
    
    print(sinal_final)
    

    token = '5543259990:AAEGAWO-LnGzAGI7H8-YxohzFYA82fSmPWA'
    chat_id = '-1001409868981'
    
    retorno = f'{msg(sinal_final)}'
    
    #url = "https://api.telegram.org/bot{5543259990:AAEGAWO-LnGzAGI7H8-YxohzFYA82fSmPWA}/sendMessage?chat_id= -1001409868981 '&text='{retorno}"    
    
    url2 = f'https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + retorno'
    resposta1 = requests.get(url2)
    
    esperar = time.sleep(20)
    