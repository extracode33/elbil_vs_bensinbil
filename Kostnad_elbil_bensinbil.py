"""
Arbeidskrav 1 - Elbil vs bensinbil
Vidar Due (vidar_due@hotmail.com)
Oppdatert 2025.09.26

"""

"Dette er et program for å sammenligne de årlige kostnadene ved elbil sammenliknet med bensinbil"

Kjørelengde = 10000 #km/år
Trafikkforsikringsavgift = (8.38*365)

#Elbil
Forsikring_elbil = 5000
Drivstofforbruk_elbil = (Kjørelengde*0.2)*2
Bomavgift_elbil = (Kjørelengde*0.1)
Kostnad_elbil = (Forsikring_elbil+Trafikkforsikringsavgift+Bomavgift_elbil+Drivstofforbruk_elbil)

print("Årlig kostnad ved elbil: kr", Kostnad_elbil)

#Bensinbil
Forsikring_bensinbil = 7500
Drivstofforbruk_bensinbil = (Kjørelengde*1.0)
Bomavgift_bensinbil = (Kjørelengde*0.3)
Kostnad_bensinbil = (Forsikring_bensinbil+Trafikkforsikringsavgift+Bomavgift_bensinbil+Drivstofforbruk_bensinbil)

print("Årlig kostnad for bensinbil: kr", Kostnad_bensinbil)

print("Kostnadsdifferanse mellom elbil og bensinbil: kr", Kostnad_bensinbil-Kostnad_elbil)
