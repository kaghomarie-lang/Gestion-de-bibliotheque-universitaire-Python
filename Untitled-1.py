solde =input(float("Entrez votre solde"))
taux =0.0
intere =0.0
nouv_solde =0.0

if solde >=1000000:
    taux ==0.05
    intere =(solde*taux)
    nouv_solde =solde-intere
    print("Votre taux d'interet est de " +str(intere) +"FCFA et votre nouveau solde est de " + str(nouv_solde) )
elif solde >=500000 and solde <=999999:
    taux == 0.03
    intere = (solde * taux)
    nouv_solde = solde - intere
    print("Votre taux d'interet est de " + str(intere) + "FCFA et votre nouveau solde est de " + nouv_solde)
elif solde <500000:
    taux == 0.01
    intere = (solde * taux)
    nouv_solde = solde - intere
    print("Votre taux d'interet est de " + intere + "FCFA et votre nouveau solde est de " + nouv_solde)
else:
    print("ERREUR")
