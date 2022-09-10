from logging import exception


allowedPercentage = tuple((0.2,0.5,1,2))

voedingshoeveelheid = 99
while voedingshoeveelheid > 20 :
    voedingshoeveelheid = int(input("Voedingshoeveelheid / 1L in ml (op verpakking)"))
    if voedingshoeveelheid > 20 :
        print ("Birchmaer max is 20ml/L ")


birchPercentage=0
while birchPercentage not in allowedPercentage:
 birchPercentage = float(input("ingesteld percentage op birchmaer: "))
 if birchPercentage not in allowedPercentage:
    print ("vul geldige waarde in! : " , allowedPercentage)

gewensteLtoetedienen = int(input("Gewenste hoeveelheid toe te dienen in L:"))
VoedingInBirchPerL = float(voedingshoeveelheid / birchPercentage)

#check if possible for birch to deliver with desigerd percentage
if voedingshoeveelheid >( birchPercentage * 10) :
    exception("Kan gewenste voeding niet halen, met ingesteld percentage!")

#check if extra mix with water is required or not
if voedingshoeveelheid < (birchPercentage*10):
    AanlenghoeveelheidInBirchL = float(voedingshoeveelheid * birchPercentage)
else:
    AanlenghoeveelheidInBirchL=0


totaalVoedingInBirch = float(gewensteLtoetedienen * VoedingInBirchPerL)
totaalAanlengInBirch = float(gewensteLtoetedienen * AanlenghoeveelheidInBirchL)
totaalInBirch = float(totaalAanlengInBirch + totaalVoedingInBirch)


print ("Voeding verhouding in birchmaer : ",VoedingInBirchPerL,"ml/l")
print ("Aanleng verhouding in birchmaer : ", AanlenghoeveelheidInBirchL,"ml/l")
print ("Totaal aantal voeding in birchmaer : " , totaalVoedingInBirch , "ml")
print ("Totaal aantal aan te lengen met water in birchmaer : ", totaalAanlengInBirch,"ml")
print ("Totale vloeistof in birchmaer :" , totaalInBirch, "ml")

if totaalInBirch > 1200 :
 print ("$$$$$$$$$$$$$$$$$$$$$$$ \n OPGELET, de totale hoeveelheid de maximum hoeveelheid van de birchmaer,\n overweeg het percentage te verlagen! \n $$$$$$$$$$$$$$$$$$$$$$$")
 percentageIndex = allowedPercentage.index(birchPercentage)
 for i in range(percentageIndex) :
    print("/n ##############################")
    print("gebruik van " , allowedPercentage[i] , " %")
    print ("================================")
    birchPercentage =float(allowedPercentage[i])
    VoedingInBirchPerL = float(voedingshoeveelheid / birchPercentage)

    #check if possible for birch to deliver with desigerd percentage
    if voedingshoeveelheid <=( birchPercentage * 10) :
        #check if extra mix with water is required or not
        if VoedingInBirchPerL < voedingshoeveelheid:
            AanlenghoeveelheidInBirchL = float(voedingshoeveelheid * birchPercentage)
        else:
            AanlenghoeveelheidInBirchL=0

        totaalVoedingInBirch = float(gewensteLtoetedienen * VoedingInBirchPerL)
        totaalAanlengInBirch = float(gewensteLtoetedienen * AanlenghoeveelheidInBirchL)
        totaalInBirch = float(totaalAanlengInBirch + totaalVoedingInBirch)
        print ("Voeding verhouding in birchmaer : ",VoedingInBirchPerL,"ml/l")
        print ("Aanleng verhouding in birchmaer : ", AanlenghoeveelheidInBirchL,"ml/l")
        print ("Totaal aantal voeding in birchmaer : " , totaalVoedingInBirch , "ml")
        print ("Totaal aantal aan te lengen met water in birchmaer : ", totaalAanlengInBirch,"ml")
        print ("Totale vloeistof in birchmaer :" , totaalInBirch, "ml")
    else :
         print ("Percentage niet geschikt!")
