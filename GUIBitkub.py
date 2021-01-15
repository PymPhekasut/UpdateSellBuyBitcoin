#BitkubChecker.py


import requests
from pprint import pprint
import time

#pip install songline

from songline import Sendline

token = 'hLvesbeIpOvIf12sT5fnSeODR7LUd2fO6qQP2OMhjRe'
messenger = Sendline(token)

line_condition = True


API_HOST ='https://api.bitkub.com'
mycoin = ['THB_BTC',
          'THB_ETH',
          'THB_DOGE']

condition = {'THB_BTC':{'buy':950000,'sell':1005000},
             'THB_ETH':{'buy':20000,'sell':30000},
             'THB_DOGE':{'buy':0.459,'sell':0.615},}

#print(condition['THB_BTC'])


def CheckCondition(coin,price):
    #coin = 'THB_BTC',price = 1050000
    text = ''
    check_buy = condition[coin]['buy']
    if price <= check_buy:
        txt = '{} Low price! is {:,.3f} Go to buy!\n price want to trade: {:,.3f}'.format(coin,price,check_buy)
        print(txt)
        text += txt + '\n--------'
        
    check_sell = condition[coin]['sell']
    if price >= check_sell:
        txt = '{} High price! is {:,.3f} Go to sell!\nprice want to trade: {:,.3f}'.format(coin,price,check_sell)
        print(text)
        text +=txt + '\n'

    return text

current_text = ''


def CheckPrice():
    global current_text #change
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    #pprint(result)


    alltext = ''
    text_line = ''
    
    for c in mycoin:
        sym = c
        data = result[sym]
        last = data['last']
        #print(data)
        #print(sym,last)
        pchange = data['percentChange']
        text = ' {} price: {:,.3f} ({})'.format(sym,last,pchange)
        alltext += text + '\n' #alltext = alltext + text
        if line_condition == True:
            if c in condition:
                checktext = CheckCondition(c,last)
                if len(checktext)> 0:
                    text_line += checktext
                

    
    if line_condition == True and current_text != text_line:
        print('Condition: ',text_line)
        current_text = text_line
        #sendline
        messenger.sendtext(text_line)


        
        
    #print(type(last))
    v_result.set(alltext)    
    #print('--------------')
    R1.after(100,CheckPrice)
    #.after = Refresh R1 every 200 ms



################GUI###################

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry ('500x300')
GUI.title('Checking Bitcoin price from Bitkub')

FONT1 = ('Angsana New',30)

L1 = ttk.Label(GUI,text='Lastest price on Bitkub')
L1.pack()

#B1= ttk.Button(GUI,text='Check!',command=CheckPrice)
#B1.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('------------result-----------')
R1 = ttk.Label(textvariable=v_result,font=FONT1)
R1.pack()


#run function everytime when open
CheckPrice()
GUI.mainloop()


