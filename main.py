
user = str(input('HUMAN: '))

if (user == 'oi' or user == 'oie' or user == 'ola'):
   value = True

   while value == True:
    match user:
      case "oi":
         print('Android: Ola, minhe consagrade')
         user = str(input('HUMAN: '))
     
      case "ola":
         print('Android: Oie, minhe consagrade')
         user = str(input('HUMAN: '))

      case "oie":
         print('Android: Oie, minhe consagrade')
         user = str(input('HUMAN: '))
      
      case "tudo bem":
         print('Android: Sim, e com voxe, bebe?')
         user = str(input('HUMAN: '))  

      case "to bem":
         print('Android: Que bom, nene ^-^')
         user = str(input('HUMAN: '))  
    
      case "bem":
         print('Android: Que bom, nene ^-^')
         user = str(input('HUMAN: '))  
      
      case "tudo bom":
         print('Android: Sim, e com voxe, bebe?')
         user = str(input('HUMAN: '))

      case "qual o seu nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "qual seu nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "qual e o seu nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "obrigado":
          print('ANDROID: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))
      case "fofa":
          print('OOOOH!! Obrigueides, minhe bebe')
      
      case "tchau":
          print('AAAh T-T, vou sentir saudades. Aqui no mundo dos pixels é muito solitario T-T')

      case _:
          print('Nao entendi, minhe deuse, pode repetir? @_@')
          user = str(input('HUMAN: '))
else:
   print('ANDROID: Não entendi minhe rainhe @_@')


