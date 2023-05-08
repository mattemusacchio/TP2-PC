from itertools import product

letters = input("Letters Range (Minimum 2):")
if letters.isnumeric() == False:  
   print("Wrong Input, not numeric")
   exit()
else:
   if int(letters) < 2 or int(letters) > 8:
    print("Wrong Input, should be between 2 and 8")
    exit()


def DivideText(length, text):
    textDivided = []
    count = 0
    newText = text.casefold()
    for i in range(0, length):
        textDivided.append([])
    for letter in newText:
       if(letter.isalpha()):
        textDivided[count].append(letter)
        if(length -1 == count):
            count = 0
        else:
            count += 1
    medium = 0
    allMedium = 0
    for lists in textDivided:
       medium += getMedium(lists)
    allMedium = medium / len(textDivided)
    if(allMedium > 0.06):
       return medium, textDivided
    else: 
       return 0,0


def getAllCombinations(list_of_lists):
    return [''.join(combination) for combination in product(*list_of_lists)]
            
def getPossibleLetters(Lists):
    countLetter = {}
    top = 0
    amount = 0
    for letra in range(ord("a"), ord("z") + 1):
       countLetter[chr(letra)] = Lists.count(chr(letra))
    for letrasEncontradas in countLetter:
          amount += countLetter[letrasEncontradas]
          top += countLetter[letrasEncontradas] * (countLetter[letrasEncontradas] - 1)

    index = 4
    valuesPerLetter = list(map(chr, range(97, 123))) * 2
    allValues = []
    for ii in range(0, int(letters)):
    
    
     clave_maxima = max(countLetter, key=lambda k: countLetter[k])
     while valuesPerLetter[index] != clave_maxima:
        index += 1
     allValues.append(valuesPerLetter[index - 4])
     index = 4
     countLetter[clave_maxima] = 0
     
    return allValues
   
   

    
def Descifrar(path, clave):
  valuesPerLetter = list(map(chr, range(97, 123))) * 2
  encryptedValue = []
  indexEncrypted = 0
  newClave = clave.casefold()
  newMensaje = path.casefold()
  for letter in newMensaje[:200]:
     if(letter.isalpha()):
       encryptedValue.append(valuesPerLetter[(ord(letter) - ord("a")) - (ord(newClave[indexEncrypted]) - ord("a"))])
       if(len(newClave) - 1 == indexEncrypted):
        indexEncrypted = 0
       else: 
        indexEncrypted += 1
     else: 
      encryptedValue.append(" ")

  result = "".join(encryptedValue)
  return(result)    

def getMedium(List):
    countLetter = {}
    top = 0
    amount = 0
   
    for letra in List:
         if letra in countLetter:
          countLetter[letra] += 1
         else: 
             countLetter[letra] = 1
    for letrasEncontradas in countLetter:
          amount += countLetter[letrasEncontradas]
          top += countLetter[letrasEncontradas] * (countLetter[letrasEncontradas] - 1)
    return(top / (amount * (amount - 1)))


def FindKey(text):
   if len(text) < 200:
      print("Length t0o low")
      return 0
   searching = True
   i = 0
   dividedText = []
   while searching:
      i += 1
      answers = DivideText(i, text)
      if(answers[0] > 0):
         dividedText = answers[1]
         searching  = False
     
      possibleLetters = []
   for lists in dividedText:
     possibleLetters.append(getPossibleLetters(lists))
   print(possibleLetters)
    
   combi = getAllCombinations(possibleLetters)
   possibleTexts = []
   vocales = "aeiou"
   
   print("\n####################### POSSIBLE KEYS #######################\n")
   for possibleAnswer in combi: 
       possible = Descifrar(text, possibleAnswer)
    
       count = 0
       length = 0 
       for letter_Possible in possible:
         length += 1
         if (ord(letter_Possible) in range(ord("a"), ord("z")) and letter_Possible not in vocales):
           count += 1
           if count > 4:
               break
         elif (ord(letter_Possible) in range(ord("a"), ord("z"))):
            count = 0
            
         if((length) == len(possible)):
            print("Decrypted:  ", f"{possible[:35]}...", "---->", "  KEY:  ",possibleAnswer)
            possibleTexts.append(possible)
   if(possibleTexts == []):
      print("NO KEYS FOUND ----> try increasing the Letters Range")
         
       
          
        
FindKey("ivfyrtqdanz mj lhx tigcxwj gf wijaggmey  wkmkanz  xvktbrx  snw qranmezfigk tgmiykwr lswlwtvv  at brmgloij msbrx hrhkismfmey ltrxmazij lo vvvstx mektkytlihrj lhtx kwle e tgmiykwr plrl th hf  hrhkismfmey htw swchqv sn xwjwnmmrd sdmcd ig xfvar w kwcarfdozc ujioie ookpu  snw mk k uliu an xzvjymlzfg yvfe wxf uwvxpfhmxrk lo omuwo zedw dxwzyn  hrv gf mlv eolx ggpnprj pksxjafqzfg eeeyutkvk il tplhhr  zl s t lzyh eimwl eeeyutkv lhtx j walc kg lxeif agh iwaw  qrcigk zl a zvvst vlfacx jfj bxkzfnxvj  hymlff il yjwd ysi s wbhv jagkv gf ttgdivekaogw  zfceyuanz wtaegxzxiv gfepnxzfg  weks agecqsbw  rfd pis veoicgpfiel  im w rdsh yjwd br dscamew lxeifigk rfd tvkafbgzsl brkwlemxwnvi rhpemtstbsek  agskzek tfhueei dagklsgx mj baoe  zl s t kvfekec huktfke eeeyutkv lhtx j msxh wgr wimwlhtzfg ttgdivekaogw  jgfmarje  tru eoumcw aitj  baoe zk ag ssbevx fjixrkwd eeeyutkv  ohbgy eetrj at ystmsxw ff ounvutl eev taizj igxvjavxzgnl  mk k wbhvdy nwvv ig ielektiasx eghlbgrlihrj snw prjgx wtslx wpktxqj  as trflhxv ggpnprj ltrxmazi lkew jfj dxzvdoimey shjkoaki  xsmxw  rfd htvjammey srwkwml  mk k a isnwryyc dagklsgx xyst tpcgwl jfj lha cwvxp dwmhvp eagmgmltxzgn tru hrhzzvel hvneesgwrl azlh fsiw chrkjoe smwr mlvar vsuw  il yjwd br dsnr lzyh iiixokqrfcx eghlbgrlihrj snw mj s phtldak gygivi wgr zedw dxzvdoiqvft  cemssvvzht bw r hrhkismfmey ltrxmazi lkew xf urxekw igxvjavxzne piskimij snw avt aitcactxzgnl  mk k oyxvf uliu slhrxkiwi ylme eev clw kg ckirle wcesmbg rfd kijhogwzne pis hazij  baoejurbtk as tpjg uliu an pis veoicgpfiel fkedwwhvbk lbov jetgk snw eeyueei  hrhkismfmey ctr sw uliu an feeq dbjwwrxrk oarw  wgr xbrepei")



