voedingshoeveelheid = int(input("Voedingshoeveelheid / 1L in ml (op verpakking)"))
birchPercentage = int(input("ingesteld percentage op birchmaer: "))
gewensteLtoetedienen = int(input("Gewenste hoeveelheid toe te dienen in L:"))

AanlenghoeveelheidInBirchL = voedingshoeveelheid * birchPercentage
VoedingInBirchPerL =voedingshoeveelheid / birchPercentage
totaalVoedingInBirch = gewensteLtoetedienen * VoedingInBirchPerL
totaalAanlengInBirch = gewensteLtoetedienen * AanlenghoeveelheidInBirchL
totaalInBirch = totaalAanlengInBirch + totaalAanlengInBirch


print ("Voeding verhouding in birchmaer : ",VoedingInBirchPerL,"ml/l")
print ("Aanleng verhouding in birchmaer : ", AanlenghoeveelheidInBirchL,"ml/l")
print ("Totaal aantal voeding in birchmaer : " , totaalVoedingInBirch , "ml")
print ("Totaal aantal aan te lengen met water in birchmaer : ", totaalAanlengInBirch,"ml")
print ("Totale vloeistof in birchmaer :" , totaalInBirch, "ml")

if totaalInBirch > 1200 :
 print ("OPGELET, de totale hoeveelheid de maximum hoeveelheid van de birchmaer, \n overweeg het percentage te verlagen!")

