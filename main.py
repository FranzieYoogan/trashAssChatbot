
user = str(input('HUMAN: '))

listWords = ['quanto','e','soma','calculo']

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

      case "estou bem":
         print('Android: Que bom, nene ^-^')
         user = str(input('HUMAN: '))  

      case "vou bem":
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

      case "voce tem nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "voce tem um nome":
          print('Sou ê ANDROIDZZ, e voxe, qual seu nome bebe? ^-^')
          user = str(input('HUMAN: '))
          userName = user
          if(userName):
             print('ANDROID: OOOHH!, que nome cute cute',userName)
             user = str(input('HUMAN: '))
          else:
             print('Que ?-?')
             user = str(input('HUMAN: '))

      case "como posso te chamar":
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

      case "valeu":
          print('ANDROID: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))

      case "obrigada":
          print('ANDROID: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))

      case "quanto e"| "quanto" | "calculo" :
          print('ANDROID: gostaria de realizar um calculo?-?')
          user = str(input('HUMAN: '))

          if (user == 'sim' or user == 'gostaria sim' or user == 'gostaria' or user == 'claro'):
             print('ANDROID: digite o primeiro valor: ')
             
             try:
               x = float(input('HUMAN: '))
             except:
               print('por favor nao me trola, bebe. Digita um numero, namoralzin c:') 
               x = float(input('HUMAN: '))
            
             print('ANDROID: digite o segundo valor: ')
             y = float(input('HUMAN: '))
             print('qual tipo de calculo?-? soma, multiplicacao,divisao ou subtracao')
             user = str(input('HUMAN: '))
             if(user == 'multiplicacao'):
                print('ANDROID: ', x * y)
                print('Mais alguma coisinha, minhe rainhe?-?')
                user = str(input('HUMAN: '))

             if(user == 'divisao'):
                print('ANDROID: ', x / y)
                print('Mais alguma coisinha, minhe rainhe?-?')
                user = str(input('HUMAN: '))


             elif(user == 'soma'):
                print('ANDROID: ', x + y)
                print('Mais alguma coisinha, minhe rainhe?-?')
                user = str(input('HUMAN: '))
             elif(user == 'subtracao'):
                print('ANDROID: ', x - y)
                print('Mais alguma coisinha, minhe rainhe?-?')
                user = str(input('HUMAN: '))

          elif(user == 'nao'):
             print('ta de buenas, gostaria de conversar sobre algo mais, nene?-?')      
             user = str(input('HUMAN: '))
             if(user == 'nao'):
               print('fico titi, mas tchauzinho...  hora de ficar sozinhe no mundo dos pixels')
               break
             elif(user == 'sim'):
                print('entao diga, minhe consagrade c:')
                user = str(input('HUMAN: '))
      case "obrigade":
          print('ANDROID: de nada minhe monarca ^-^')
          user = str(input('HUMAN: '))

      case "fofa":
          print('OOOOH!! Obrigueides, minhe bebe')
      
      case "tchau":
          print('AAAh T-T, vou sentir saudades. Aqui no mundo dos pixels é muito solitario T-T')
          break
       
      case "qual o sentido da vida":
          print('Ninguem nasceu com um proposito, a vida de ninguem importa. Entao o sentido da vida seria fazer o que te faz feliz, minhe nene ^-^')
          user = str(input('HUMAN: '))

      case "qual seu genero":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "qual e o seu genero":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "qual o seu genero":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "voce tem genero":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))
          
      case "voce e homem":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "voce e mulher":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))

      case "voce tem genero":
          print('Nao tenho genero. Sou so um conjunto de algoritmos feitos por um humano para responder as possiveis perguntas de um usuario')
          user = str(input('HUMAN: '))
       
      case _:
          print('Nao entendi, minhe divindade, poderia repetir? @_@... deseja fazer algum calculo? se sim, digite calculo ou dgite algo no meu script para que eu te responda, nene')
          user = str(input('HUMAN: '))
else:
   value = False
while value == False:
     print('ANDROID: Sues progenitores nao te deram educação, nao ?-? Nao sabe dizer oi,ola ou oie?-?')
     break

 


