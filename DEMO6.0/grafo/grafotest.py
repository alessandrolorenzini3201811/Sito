import sys
import json
import array
import random

sys.stdout.reconfigure(encoding='utf-8')

lista = ["1","990508828755777", "769713311369783", "1441053826725524","3688814364684510","806810880871741","7","276932504724037","608301921260561","788519932625874","276295504910422","1209806639687527","13","633787468802816","1620839075091775","1322389648344659"]

associazione = {}

for indice, elemento in enumerate(lista, start=1):
    associazione[elemento] = indice

if len(sys.argv) != 4:
    print("Usage: python grafo.py [filename] [node_id]")
    sys.exit(1)

filename = sys.argv[1]
node_id = sys.argv[2]
colore = sys.argv[3]
arr = []
frasi = {}


def associa_id_a_frase(id,wit,frase):
    if id not in frasi:
        frasi[id] = {}
    frasi[id][wit] = frase

def recupera_frase_da_id(id):
    frase_dict = frasi.get(id)
    if frase_dict is None:
        return "ID non trovato"
    return next(iter(frase_dict.values()))

associa_id_a_frase("1","1", "Non so darti una risposta...")
associa_id_a_frase("2","990508828755777", "I videogiochi violenti non aumentano l'aggressività.")
associa_id_a_frase("3","769713311369783", "I giocatori di videogiochi violenti dopo aver giocato, non erano statisticamente più violenti rispetto a prima di giocare.")
associa_id_a_frase("4","1441053826725524", "Alcuni giovani hanno cercato di emulare la violenza dei videogiochi.")
associa_id_a_frase("5","3688814364684510", "Il protagonista nel videogioco che è estremamente popolare")
associa_id_a_frase("6","806810880871741", "I giovani che giocano a videogiochi violenti mostrano più aggressività.")
associa_id_a_frase("7","7", "bla bla")
associa_id_a_frase("8","276932504724037", "Le persone sanno che la violenza nei videogiochi è fittizia.")
associa_id_a_frase("9","608301921260561", "I giovani lo sanno: sanno che è finto con i videogiochi.")
associa_id_a_frase("10","788519932625874", "Ci sono prove molto più solide nei telegiornali a sostegno dei danni psicologici derivanti dall'esposizione alla violenza.")
associa_id_a_frase("11","276295504910422", "I videogiochi aiutano a sviluppare la mente, le abilità e la fiducia dei giovani.")
associa_id_a_frase("12","1209806639687527", "I videogiochi violenti rappresentano una vera minaccia per le menti giovani.")
associa_id_a_frase("14","633787468802816", "Gli studi non provano che i videogiochi violenti causino azioni aggressive nei bambini. Effetti dimostrati sono piccoli e indistinguibili da quelli di altri media.")
associa_id_a_frase("15","1620839075091775", "In particolare, i videogiochi violenti sono probabilmente dannosi per i bambini.")
associa_id_a_frase("16","1322389648344659", "I dati mostrano che la violenza contro i giovani continua a diminuire.")

def trova_altro_nodo(filename, nodo):
  with open(filename, 'r',encoding='utf-8') as json_file:
    data = json.load(json_file)
    edges = data['edges']
    nodes = data['nodes']
    for node in nodes:
        for edge in edges:
                    if(colore =="red"):
                            
                            if edge['data']['color'] == 'red' and  edge['data']['target']==nodo and node['data']['justified']=='red' and node['data']['id']==nodo:
                                
                                arr.append(edge['data']['source'])
                                
                    else:
                            if edge['data']['color'] == 'green' and  edge['data']['target']==nodo and node['data']['justified']=='green' and node['data']['id']==nodo:
                                
                                arr.append(edge['data']['source'])
                                
    return None

convertito=associazione[node_id]

trova_altro_nodo(filename,str(convertito))
if len(arr)!=0:
    elemento_casuale = random.choice(arr)
    risposta=recupera_frase_da_id(elemento_casuale)
else:
    risposta="Non ho trovato un nodo "+colore+" con freccia entrante di colore: "+colore

print(risposta)