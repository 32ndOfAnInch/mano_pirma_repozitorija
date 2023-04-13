# biblioteka dazniausiai pasikartojancios raides skaiciavimui
from collections import Counter

#
# programele praso ivesti zodi arba fraze, paklausti vartotojo kokio nori efekto su zodziu ir pateikti statistika
#

# zodzio ivedimas
print()
zodziai = input("Iveskite kokia nors fraze ar zodi: ")

# tikrina ar ivesta kas nors ir jei taip tai praso pasirinkti efekta
if not zodziai.strip():
    efektas = 0
    print("Jus nieko neivedete")
else:
    # efekto pasirinkimas
    print()
    print("Efektu sarasas: 1-visos raides mazosios, 2-visos raides didziosios, 3-tarpai tarp raidziu, bet koks kitas sk-jokio efekto")
    print()
    efektas = int(input("pasirinkite efekta: "))

# logines operacijos su efektais
if (efektas == 1) and (zodziai != ""):
    zodziai_efekt=zodziai.lower()
    print(f"Jusu zodis arba fraze mazosiomis raidemis: {zodziai_efekt}")
elif (efektas == 2) and (zodziai != ""):
    zodziai_efekt=zodziai.upper()
    print(f"Jusu zodis arba fraze didziosiomis raidemis: {zodziai_efekt}")
elif (efektas == 3) and (zodziai != ""):
    zodziai_efekt=" ".join(zodziai)
    print(f"Jusu zodis arba fraze, kai tarpai tarp raidziu: {zodziai_efekt}")
else:
    print("nepasirinkote jokio efekto")


# statistika
if zodziai != "":
    print()
    print("----------------------------------------")
    print("---------------STATISTIKA---------------")
    print("----------------------------------------")
    zodziai_be_tarp = zodziai.replace(" ", "")
    print(f"Jusu ivesto zodzio arba frazes {zodziai} ilgis, iskaitant tarpus: {len(zodziai)}")
    print(f"Jusu ivesto zodzio arba frazes {zodziai} ilgis, neiskaitant tarpu: {len(zodziai_be_tarp)}")

    # iterpiau svetima koda kad surast dazniaiusiai pasikartojancia raide
    res = Counter(zodziai)
    res = max(res, key = res.get)
 
    # dazniausiai pasikartojanti raide
    print (f"Dazniausiai pasikartojanti raide zodziuose {zodziai} yra : {str(res)}")
