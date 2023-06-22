import sys
import json
import random

sys.stdout.reconfigure(encoding='utf-8')

listaita = ["1","990508828755777", "769713311369783", "1441053826725524","3688814364684510","806810880871741","7","276932504724037","608301921260561","788519932625874","276295504910422","1209806639687527","13","633787468802816","1620839075091775","1322389648344659"]
listaing = ["1","774051217505822","2250974201766585","792387539072360","538245768325376","931879254542072","584513687147809","105424695909424","573088841665296","172700339102449","599429582288263","636646265018296","13","14","15","159585016945664"]
associazione = {}
associazioneing = {}
for indice, elemento in enumerate(listaita, start=1):
    associazione[elemento] = indice

for indiceing, elementoing in enumerate(listaing, start=1):
    associazioneing[elementoing] = indiceing

if len(sys.argv) != 5:
    print("Usage: python grafo.py [filename] [node_id]")
    sys.exit(1)

filename = sys.argv[1]
node_id = sys.argv[2]
colore = sys.argv[3]
lingua= sys.argv[4]
arr = []
frasi = {}
frasiing={}


def associa_id_a_frase(id,wit,frase):
    if id not in frasi:
        frasi[id] = {}
    frasi[id][wit] = frase


def associa_id_a_fraseing(id,wit,frase):
    if id not in frasiing:
        frasiing[id] = {}
    frasiing[id][wit] = frase

def recupera_frase_da_id(id):
    frase_dict = frasi.get(id)
    if frase_dict is None:
        return "ID non trovato"
    return next(iter(frase_dict.values()))

def recupera_frase_da_iding(id):
    frase_dicting = frasiing.get(id)
    if frase_dicting is None:
        return "ID non trovato"
    return next(iter(frase_dicting.values()))

associa_id_a_frase("1","1", "I videogiochi rendono aggressivi")
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


associa_id_a_fraseing("1","1", "The videogames")
associa_id_a_fraseing("2","774051217505822", "Violent video games do not addition aggression.")
associa_id_a_fraseing("3","2250974201766585", "Violent video games players in their beliefs about aggression after playing the game were not statistically different from the non-playing control group than they were before playing.")
associa_id_a_fraseing("4","792387539072360", "Some young people have tried to emulate gambling violence.")
associa_id_a_fraseing("5","538245768325376", "Protagonist in the video game which is wildly popular.")
associa_id_a_fraseing("6","931879254542072", "Young people playing violent games display more aggression.")
associa_id_a_fraseing("7","584513687147809", "Children who view violent television shows or films or who play violent video games are significantly more likely to behave aggressively in comparison to children who view nonviolent television shows or films, or who play nonviolent video games.")
associa_id_a_fraseing("8","105424695909424", "People know that the violence in video games is fake.")
associa_id_a_fraseing("9","573088841665296", "Young people know it: You know it's fake with video games.")
associa_id_a_fraseing("10","172700339102449", "There's far better evidence on TV news to support psychological harm from exposure to violence.")
associa_id_a_fraseing("11","599429582288263", "Games help to develop the minds, skills and confidence of young people.")
associa_id_a_fraseing("12","636646265018296", "Violent video games pose a real threat to young minds.")
associa_id_a_fraseing("14","14", "Psychological studies which show a connection between exposure to violent video games and harmful effects on children do not show that such exposure causes aggressive action by minors. Any demonstrated effects are both small and indistinguishable from other media-generated effects.")
associa_id_a_fraseing("15","15", "In particular, violent video games are likely to affect the baby.")
associa_id_a_fraseing("16","159585016945664", "The data shows that violence against young people is continuing to decline.")



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


if(lingua=='italiano'):

        convertito=associazione.get(node_id,None)
        if convertito is None:
            print("Scrivi una frase in italiano")
        else:
            trova_altro_nodo(filename,str(convertito))
else:
        convertito=associazioneing.get(node_id,None)
        if convertito is None:
            print("write in english pleah")
        else:
            trova_altro_nodo(filename,str(convertito))

    




if len(arr)!=0:

    elemento_casuale = random.choice(arr)
    if(lingua=='italiano'):
        risposta=recupera_frase_da_id(elemento_casuale)
    else:
        risposta=recupera_frase_da_iding(elemento_casuale)
else:
    risposta="Non ho trovato un nodo "+colore+" con freccia entrante di colore: "+colore

print(risposta)