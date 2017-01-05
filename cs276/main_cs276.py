from tokenization import *

from A_traitements_linguistiques import *

if __name__ == '__main__':

    # Prepare cs276 corpus
    useful_tokens = get_cs276_tokens()

    print("\n------------------------------------------------------------")
    print("| 2.1 / A Traitements linguistiques                         |")
    print("------------------------------------------------------------")
    traitements_linguistiques(useful_tokens)

    # print("\n------------------------------------------------------------")
    # print("| 2.2 / B Indexation                                        |")
    # print("------------------------------------------------------------")
    # term_termID, doc_docID, termID_docID = indexation(useful_tokens, docs)
    #
    # print("\n------------------------------------------------------------")
    # print("| 2.2.1 / C Modèle de recherche booléen                     |")
    # print("------------------------------------------------------------")
    # modele_booleen(term_termID, doc_docID, termID_docID)
    #
    # print("\n------------------------------------------------------------")
    # print("| 2.2.2 / D Modèle de recherche vectoriel                  |")
    # print("------------------------------------------------------------")
    # modele_vectoriel(term_termID, doc_docID, termID_docID)

