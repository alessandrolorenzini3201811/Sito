import networkx as nx

def find_target(graph, label):
    for edge in graph.edges(data=True):
        if  graph.nodes[edge[0]]['label'] == label:
            return graph.nodes[edge[1]]['label']
    return None

# Carica il grafo dal file GML
file_path = 'soloatt.gml'
graph = nx.read_gml(file_path, label='id')

# Specifica il label di cui vuoi trovare il target
label_to_find = '990508828755777'

# Trova il target corrispondente al label
target = find_target(graph, label_to_find)

# Stampa il risultato
if target:
    print(f"Il target corrispondente al label '{label_to_find}' è '{target}'.")
else:
    print(f"Nessun target trovato per il label '{label_to_find}'.")



frasi = {}  # Dizionario vuoto per associare ID a frasi

def associa_id_a_frase(id, frase):
    frasi[id] = frase

def recupera_frase_da_id(id):
    return frasi.get(id, "ID non trovato")  # Restituisce "ID non trovato" se l'ID non è presente nel dizionario

associa_id_a_frase(990508828755777, "I videogiochi violenti non aumentano l'aggressività.")
associa_id_a_frase(3, "ATTACCO")
associa_id_a_frase(769713311369783, "I giocatori di videogiochi violenti nelle loro convinzioni sull'aggressività dopo aver giocato al gioco non erano statisticamente diversi dal gruppo di controllo non giocante rispetto a prima di giocare.")
associa_id_a_frase(1441053826725524, "Alcuni giovani hanno cercato di emulare la violenza dei videogiochi.")
associa_id_a_frase(3688814364684510, "Il protagonista nel videogioco che è estremamente popolare")
associa_id_a_frase(806810880871741, "I giovani che giocano a videogiochi violenti mostrano più aggressività.")
associa_id_a_frase(276932504724037, "Le persone sanno che la violenza nei videogiochi è fittizia.")
associa_id_a_frase(6083019212605612, "I giovani lo sanno: sanno che è finto con i videogiochi.")
associa_id_a_frase(788519932625874, "Ci sono prove molto più solide nei telegiornali a sostegno dei danni psicologici derivanti dall'esposizione alla violenza.")
associa_id_a_frase(276295504910422, "I videogiochi aiutano a sviluppare la mente, le abilità e la fiducia dei giovani.")