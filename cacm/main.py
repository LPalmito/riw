from cacm.tokenization import *

from cacm.A_traitements_linguistiques import *
from cacm.B_indexation import *
from cacm.C_modele_booleen import *
from cacm.D_modele_vectoriel import *

if __name__ == '__main__':

    # Ouvre et lit le cacm.all
    cacm = open('./Resources/CACM/cacm.all')
    text = cacm.read()

    # Prépare le corpus cacm
    useful_tokens, docs = prepare_cacm(text)

    # 2.1 / A Traitements linguistiques
    traitements_linguistiques(useful_tokens)

    # 2.2 / B Indexation
    term_termID, doc_docID, termID_docID = indexation(useful_tokens, docs)

    # 2.2.1 / C Modèle de recherche booléen
    modele_booleen(term_termID, doc_docID, termID_docID)

    # 2.2.2 / D Modèle de recherche vectoriel
    modele_vectoriel(term_termID, doc_docID, termID_docID)

    # Ferme cacm.all
    cacm.close()
