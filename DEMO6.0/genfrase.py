import random
import sys
sys.stdout.reconfigure(encoding='utf-8')
arr = [ "I videogiochi violenti non aumentano l'aggressività.",
        "I giocatori di videogiochi violenti dopo aver giocato, non erano statisticamente più violenti rispetto a prima di giocare.",
        "Alcuni giovani hanno cercato di emulare la violenza dei videogiochi.",
        "Il protagonista nel videogioco che è estremamente popolare",
        "I giovani che giocano a videogiochi violenti mostrano più aggressività.",
        "Le persone sanno che la violenza nei videogiochi è fittizia.",
        "I giovani lo sanno: sanno che è finto con i videogiochi.",
        "Ci sono prove molto più solide nei telegiornali a sostegno dei danni psicologici derivanti dall'esposizione alla violenza.",
        "I videogiochi aiutano a sviluppare la mente, le abilità e la fiducia dei giovani.",
        "I videogiochi violenti rappresentano una vera minaccia per le menti giovani.",
        "Gli studi non provano che i videogiochi violenti causino azioni aggressive nei bambini. Effetti dimostrati sono piccoli e indistinguibili da quelli di altri media.",
        "In particolare, i videogiochi violenti sono probabilmente dannosi per i bambini.",
        "I dati mostrano che la violenza contro i giovani continua a diminuire."
        ]
elemento_casuale = random.choice(arr)
print(elemento_casuale)