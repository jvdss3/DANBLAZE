from imp import reload
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import telegram
import os


os.system('cls')
        #Por informações do seu bot aqui #.
api_key = '5460372550:AAEMoZWuuERMawqYRaW-X-F5ycQCJPXSgBQ' 
user_id = '978591783'
bot=telegram.Bot(token=api_key)

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options=chrome_options)

WAIT = 10
delta = 0
xx = 0
nav.get('https://blaze.com/pt/games/double')
while True:
    time.sleep(3) 
    girando = nav.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    
    if girando == 'Girando...':
        xx = 1
        print('Analisando')
        delta = WAIT
        time.sleep(12)
        pegardados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
        tfg = pegardados.split()
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
            if x == '1':
                return 'Vermelho'

            if x == '2':
                return 'Vermelho'

            if x == '3':
                return 'Vermelho'

            if x == '4':
                return 'Vermelho'

            if x == '5':
                return 'Vermelho'

            if x == '6':
                return 'Vermelho'

            if x == '7':
                return 'Vermelho'

            if x == '8':
                return 'Preto'

            if x == '9':
                return 'Preto'

            if x == '10':
                return 'Preto'

            if x == '11':
                return 'Preto'

            if x == '12':
                return 'Preto'

            if x == '13':
                return 'Preto'

            if x == '14':
                return 'Preto'


        pd = tfg[0:4]


        mapeando = map(qualnum, pd)
        mapeando2 = map(qualcor, pd)

        finalnum = list(mapeando)
        finalcor = list(mapeando2)


    if xx == 1:
        xx = 0

        def verificarsaida(num):
            if num == ['Preto','Preto','Preto','Preto']:
                return bot.send_message(chat_id=user_id, text='''
                    🔔⚠️🚨Atenção🚨⚠️🔔 
                    ✅Entrada confirmada! 🔴
                    ✅Proteção no: ⚪️
                    ✅Ate Gale 2 🐓🐓 
                    🎲Jogue agora Blaze Double🎲  
                    (https://blaze.com/r/VX9z7Y)   
                    ''')
            if num == ['Vermelho','Vermelho','Vermelho','Vermelho']:
                return bot.send_message(chat_id=user_id, text='''
                    🔔⚠️🚨Atenção🚨⚠️🔔 
                    ✅Entrada confirmada! ⚫
                    ✅Proteção no: ⚪️
                    ✅Ate Gale 2 🐓🐓 
                    🎲Jogue agora Blaze Double🎲  
                    (https://blaze.com/r/VX9z7Y)
                    by: @HACK_BLAZE_36 🥷🏾
                    ''')
            if num == ['Vermelho','Vermelho','Preto','Preto']:
                return bot.send_message(chat_id=user_id, text='''
                    🔔⚠️🚨Atenção🚨⚠️🔔 
                    ✅Entrada confirmada! ⚫
                    ✅Proteção no: ⚪️
                    ✅Ate Gale 2 🐓🐓 
                    🎲Jogue agora Blaze Double🎲  
                    (https://blaze.com/r/VX9z7Y)
                    by: @HACK_BLAZE_36 🥷🏾
                    ''')
            if num == ['Preto','Preto','Vermelho','Vermelho']:
                return bot.send_message(chat_id=user_id, text='''
                    🔔⚠️🚨Atenção🚨⚠️🔔 
                    ✅Entrada confirmada! 🔴
                    ✅Proteção no: ⚪️
                    ✅Ate Gale 2 🐓🐓 
                    🎲Jogue agora Blaze Double🎲  
                    (https://blaze.com/r/VX9z7Y)    
                    by: @HACK_BLAZE_36 🥷🏾
                    ''')
#             if num == ['Vermelho','Preto','Vermelho','Preto']:
#                 return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! ⚫
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Preto','Vermelho','Preto','Vermelho']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! 🔴
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Preto','Preto','Preto','Vermelho']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! 🔴
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Vermelho','Vermelho','Vermelho','Preto']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! ⚫
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Vermelho','Preto','Preto','Preto']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! 🔴
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Preto','Vermelho','Vermelho','Vermelho']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! ⚫
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Preto', 'Preto', 'Vermelho', 'Preto']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! ⚫
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Preto', 'Vermelho', 'Vermelho', 'Preto']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! ⚫
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Vermelho','Preto','Preto','Vermelho']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! 🔴
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
#                 if num == ['Preto', 'Vermelho', 'Preto', 'Preto']:
#                     return bot.send_message(chat_id=user_id, text='''
# 🔔⚠️🚨Atenção🚨⚠️🔔 
# ✅Entrada confirmada! ⚫
# ✅Proteção no: ⚪️
# ✅Ate Gale 2 🐓🐓 
# 🎲Jogue agora Blaze Double🎲  
#   (https://blaze.com/r/VX9z7Y)      
#                                              💬 
# by: @HACK_BLAZE_36 🥷🏾
#                 ''')
        print(finalnum)
        print(finalcor)
        testando = verificarsaida(finalcor)
        print(testando)

        time.sleep(27)
        print(time.sleep)
