from cacm.tokenization import *

from cacm.A_linguistic_processing import *
from cacm.B_indexation import *
from cacm.C_boolean_main import *
from cacm.D_1_vectorial_main import *
from cacm.E_pertinence_measures import *

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
    unique_useful_tokens = linguistic_processing(useful_tokens)

    print("\n------------------------------------------------------------")
    print("| 2.2 / B Indexation                                        |")
    print("------------------------------------------------------------")
    term_termID, docID_doc, termID_docID, docID_termID = indexation(unique_useful_tokens, docs)

    print("\n------------------------------------------------------------")
    print("| 2.2.1 / C Modèle de recherche booléen                     |")
    print("------------------------------------------------------------")
    boolean_main(term_termID, docID_doc, termID_docID, docs_backup)

    print("\n------------------------------------------------------------")
    print("| 2.2.2 / D Modèle de recherche vectoriel                  |")
    print("------------------------------------------------------------")
    vectorial_main(term_termID, docID_doc, termID_docID, docID_termID, docs_backup)

    print("\n------------------------------------------------------------")
    print("| 2.3 / E Mesures de pertinence                            |")
    print("------------------------------------------------------------")
    pertinence_measures(term_termID, docID_doc, termID_docID, docID_termID)

    # Ferme cacm.all
    cacm.close()
