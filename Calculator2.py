allowedPercentage = tuple((0.2,0.5,1,2))
contnue = "y"
while contnue =="Y" or contnue =="y":
    voedingshoeveelheid = 99
    while voedingshoeveelheid > 20 :
        voedingshoeveelheid = float(input("Voedingshoeveelheid / 1L in ml (op verpakking)"))
        if voedingshoeveelheid > 20 :
            print ("FOUT : Birchmaer max is 20ml/L ")
    gewensteLtoetedienen = int(input("Gewenste hoeveelheid toe te dienen in L:"))

    for birchPercentage in allowedPercentage :
        print("\n================================")
        print("gebruik van " , birchPercentage , " %")
        print ("================================")
        
        VoedingInBirchPerL = float(voedingshoeveelheid / birchPercentage)
        #check if possible for birch to deliver with desigerd percentage
        if voedingshoeveelheid <=( birchPercentage * 10) :
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
                print ("!!!!!!!!!!!! \nOPGELET, Birchmaer capaciteit is 1200ml. Geef deze hoeveelheid in meerdere beurten")
        else :
            print ("Percentage niet geschikt! \nKan voeding niet geconcentreerder maken")
    contnue = input ("Nog eentje? : Y ")