from riw.cacm.C_modele_booleen import *


def modele_booleen_front(term_termID, docID_doc, termID_docID, docs_backup, search):
    """Print the results of a single-word search and a CNF search"""
    # Take user input for a single word as search
    searched_term = search
    start_1 = time.time()
    print(searched_term)
    searched_docIDs_1 = search_term_in_corpus(searched_term, term_termID, termID_docID)
    end_1 = time.time()
    duration_1 = (end_1-start_1)*1000
    print("Temps de réponse :", duration_1, "ms.")
    # pprint.pprint(docs_backup[:4])
    # pprint.pprint((docID_doc))
    # Display properly the results
    search_to_front = {}
    if len(searched_docIDs_1) == 0:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    else:
        print("Les documents correspondant à votre recherche sont :")
        for s_dID in searched_docIDs_1:
            search_to_front[s_dID] = [docs_backup[s_dID]['.T'], docs_backup[s_dID]['.B'], docs_backup[s_dID]['.W']]
    return str(search_to_front)
    #         print("- - - - -")
    #         print("ID : ", s_dID)
    #         for word in docs_backup[s_dID]['.T']:
    #             print(word, "", end='')
    #         print("")
    #         print("Date: ", end='')
    #         for word in docs_backup[s_dID]['.B']:
    #             print(word, "", end='')
    #         print("")
    #         print("Text: ", end='')
    #         if len(docs_backup[s_dID]['.W']) == 0:
    #             print("No preview available for this article")
    #         else:
    #             if len(docs_backup[s_dID]['.W']) > 20:
    #                 for word in docs_backup[s_dID]['.W'][:20]:
    #                     print(word, "", end='')
    #                 print("...")
    #             else:
    #                 for word in docs_backup[s_dID]['.W']:
    #                     print(word, "", end='')
    #         print("")
    # print("- - - - -")