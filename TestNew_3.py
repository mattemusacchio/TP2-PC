def getMedium(text):
    everyLetter = list(map(chr, range(97, 123)))
    countLetter = {}
    top = 0
    amount = 0
    for letra in text:
     if letra in countLetter:
        countLetter[letra] += 1
     else: 
       countLetter[letra] = 1
    for letrasEncontradas in countLetter:
       amount += countLetter[letrasEncontradas]
       top += countLetter[letrasEncontradas] * (countLetter[letrasEncontradas] - 1)
    
    return(top / (amount * (amount - 1)))



ratio  = (getMedium("esnsst") + getMedium("susueo") + getMedium("tnapc") + getMedium("emjer") + getMedium("eeere")) / 5

print(ratio)


