from cacm.tokenization import *

from cacm.A_traitements_linguistiques import *
from cacm.B_indexation import *
from cacm.C_modele_booleen import *
from cacm.D_modele_vectoriel import *
from cacm.E_mesure_pertinence import *

if __name__ == '__main__':

    # Ouvre et lit le cacm.all
    cacm = open('../Resources/CACM/cacm.all')
    text = cacm.read()

    # Prépare le corpus cacm
    docs, docs_backup = get_docs(text)
    useful_tokens = get_useful_tokens(docs)

    print("\n------------------------------------------------------------")
    print("| 2.1 / A Traitements linguistiques                         |")
    print("------------------------------------------------------------")
    unique_useful_tokens = traitements_linguistiques(useful_tokens)

    print("\n------------------------------------------------------------")
    print("| 2.2 / B Indexation                                        |")
    print("------------------------------------------------------------")
    term_termID, docID_doc, termID_docID, docID_termID = indexation(unique_useful_tokens, docs)

    print("\n------------------------------------------------------------")
    print("| 2.2.1 / C Modèle de recherche booléen                     |")
    print("------------------------------------------------------------")
    modele_booleen(term_termID, docID_doc, termID_docID, docs_backup)

    print("\n------------------------------------------------------------")
    print("| 2.2.2 / D Modèle de recherche vectoriel                  |")
    print("------------------------------------------------------------")
    modele_vectoriel(term_termID, docID_doc, termID_docID, docID_termID)

    print("\n------------------------------------------------------------")
    print("| 2.3 / E Mesures de pertinence                            |")
    print("------------------------------------------------------------")
    mesure_pertinence(term_termID, docID_doc, termID_docID, docID_termID)

    # Ferme cacm.all
    cacm.close()
