from itertools import product

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
    for lists in textDivided:
       medium = getMedium(lists)
    if(medium > 0.063):
       return medium, textDivided
    else: 
       return 0,0

   ## possibleLetters = []
   ## for lists in textDivided:
     ##   possibleLetters.append(getPossibleLetters(lists))
    
   ## combi = getAllCombinations(possibleLetters)
   ## [Descifrar(text, possibleAnswer) for possibleAnswer in combi]

def getAllCombinations(list_of_lists):
    return [''.join(combination) for combination in product(*list_of_lists)]
            
def getPossibleLetters(Lists):
    countLetter = {}
    top = 0
    amount = 0
   
    for letra in Lists:
         if letra in countLetter:
          countLetter[letra] += 1
         else: 
             countLetter[letra] = 1
    for letrasEncontradas in countLetter:
          amount += countLetter[letrasEncontradas]
          top += countLetter[letrasEncontradas] * (countLetter[letrasEncontradas] - 1)

    index = 4
    valuesPerLetter = list(map(chr, range(97, 123))) * 2
    allValues = []
    for ii in range(0, 3):
    
    
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
  for letter in newMensaje:
     if(letter.isalpha()):
       encryptedValue.append(valuesPerLetter[(ord(letter) - ord("a")) - (ord(newClave[indexEncrypted]) - ord("a"))])
       if(len(newClave) - 1 == indexEncrypted):
        indexEncrypted = 0
       else: 
        indexEncrypted += 1
     else: 
      encryptedValue.append(" ")

  result = "".join(encryptedValue)
  print(result[:20])    

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
   searching = True
   i = 0
   dividedText = []
   while searching:
      i += 1
      answers = DivideText(i, text)
      
      if(answers[0] > 0):
         print(i)
         searching  = False

    
   
        

FindKey("owvnx hmyl zy gbui nwhrjpa n gltlr bp lvqrvu snrglbuy ypzr ij dwze rodvcv t ebuco ovvv ew lolyorr jecqeeea vf ksml wzdp go uz erlc tv ghvtz hnupztrrocntv nwhrjpa. uamtvt bvpv gejemq ffc unnp jmnrj zn zy ctnr (wzep crvebl gfzl eejftgs), ypzr aip abmv ccyej zn ghlxj ghre q sevw prlgpl ze: xpvrrrw iyl-etoutvca nrv ywg wfcbu ik. dtreg owrs nzvqeid. wctzxiy scpmc tzxm soi xm vs rcwhnu 7.5 swhrj, hqgh ry iosfwcge dtvvmlx ws aizcad 4yca. vt yla uagamaeu ew ze jpdrrrw bvmvd buak t ens jecpk fy abmv azbbcpu soi lv uolc qa typ vvgye, jht nla nbcp bb sfwdr ik tv 5 ziefbrs zy bue dzzaier. q sevw tvkv epr bilqa cfxuvtj l tbt fq auabj auoie-brrd xmzoitmf tf dbnbcp tbnx-emem dpubrzpa quitvt typ vvgye. q grp ew ftrcb ftlogvnx qwe aej jvg kpags npty ie lliaenm (fempznl ulgf), empv vf wzz fhfcb ceitwqs fq bvmv, ew zaotuvzv epr nlxjrr fq vvgyea ghre ul bilqa gvea soi epr mremeirw. igtvyl gukzzvacd we rvgqrw jpafifya.rvvy qs typg nrv miq. typ nnck epnt ksml gve gbu kz buiev ioole bue dlbrrzlt vs nsig cffvgs. zq qgs kzw ooitvt, yff knn rwenyj hwek fy abmvepvnx ptfe. ipurmspz ghre gbu tlv nljz bey kz igtvyl n dzqnrrvyb gukzzvac hqgh r oqsfvcmat kl. brskd: xeeglzntzzv poedqqeitvt typ jvg gtkguip iad fconnzdigify qf typ sry.tcmntv dkueuftr ow dbhdp, pdrn zq gbu uzvg sktkx tf tb. soi xm ghzd cfurwtl iegwyvvd ortktvt ae tlra fq mieijbuier q aevo bb keze nnu pfclznqglp hzvtzyo vt uzea ie ememj zn oucwmg pftvgs. tzvfiupz nlc awvnkd knrvqcylp lvq tytvx aszcg hfh tbnx tb jicw bnkv jwh tf rmg typu qony. qs yff lbnk ow ghzd, bueip qf a kpvqeeng go jamad kzw zuts bvmv zv oextvaier ws mremeirw iad ksma sbtu ghizcth ksm (zoje qzpfcbnnk) wigei xigeitiy dlp bb lrns bf ktur. achils kcg go czwx ak azrvzzcf tvdbf bvqwee jeietzyo go jecqy.vdxrczltyy zq bue glag tvdbf wvcm jrzebrn sj bue jlur piznrsjzz. ghzd evlc rqie pzc ftizvt hzybf aszcg hfh gbu jswhlu dbhdp. pdrrp azbfvdabr yla n dzqnrrvyb rvrwcntzzv ftpwm. qoee iptlltyy rebrmge bb cfxxyekp bue hfmftzzvf ie epr bvrqanzyo, ouk eixe tlzrflw vbtv zn ghv egce fq yhejeqbnj. cmndzyo nnu fvqeidbnnutvt ij ywg typ anmv la eegwqpaktvt typ kbnkpvg.empv v owema mrvm ghzd uvsklsr sktty: yff zrau l nbrdftn/dvcqiaktwa/pizws ie epr bfzs nnu tb zabpa ceiqmpt jpvfe. eze plfdm ghv mwbk ryl grp ew jrzem vt uzea. yff evlc qqad ksig tyta crfnmfs zd kbmgwmgecj lvfwpzrnk lvq ik hqyl rxime pzc ghre unnp eqzej jwh wfyb nckfiylp mm nbcp bb df epvs! jzurhfh bue khw ghzyof ujp lvfwpzrnk aietj zn ghv xmzoij. unkv tb n pftvg tf xixe jfzr tylb lol nia atecnlcj eeikp lbwe epr mfdb vmgzzgaee jvtj, lvq tylb lol nia rv-omeimp bued lb jicw. nryexia frxwhscj saen epvs mpzl wvwt. nlnlgf tij bb cfwtnbfcige ntbu oksmes, sfb aerc bue vyl.ftlog nlfym siidb oetlcfe zy bue vlzyy jeitej zn ftlogvnx zbueid knn fytl svcdr aj l lvskciptzzv. ouk ymnr ksm rnu rmg tfrmghvc evty zbueid: buep hqyl fqbrn gzqat ffb vmgzzgaee xvtwltys, scqag la obou tafuvd, iad jzurtzxmf gzgm lol lv bpgzzguetbl tf emncy. hpvcy mzvnxd ur tf: owat fytl hryo buk zvyy ntbu skcwagvc aguupvgs. npixei dbhdvybf wzwt uamp gbu vixyazy buiera go ksmz aeo gbu ntty fzyl ghre bratsqag ksm zakpzvac smypj l tbt ntbu ueomesklvqier. ob tf epr pizn oewzzr fzyiy eolu nt cpift fykr ffc wsfznm uolca.")



