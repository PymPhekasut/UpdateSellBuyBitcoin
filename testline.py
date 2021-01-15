
#testline.py




from songline import Sendline

token = 'hLvesbeIpOvIf12sT5fnSeODR7LUd2fO6qQP2OMhjRe'
messenger = Sendline(token)


messenger.sendtext('Hello')


messenger.sticker(3,1)

messenger.sendimage('https://miro.medium.com/max/2414/1*KQ1PyVB2XNSfEeDiejFvxA.png')
