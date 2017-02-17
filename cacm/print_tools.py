def boolean_print(s_dID, docs_backup):
    print("- - - - -")
    print("ID : ", s_dID)
    for word in docs_backup[s_dID]['.T']:
        print(word, "", end='')
    print("")
    print("Date: ", end='')
    for word in docs_backup[s_dID]['.B']:
        print(word, "", end='')
    print("")
    print("Snippet: ", end='')
    if len(docs_backup[s_dID]['.W']) == 0:
        print("No preview available for this article")
    else:
        if len(docs_backup[s_dID]['.W']) > 20:
            for word in docs_backup[s_dID]['.W'][:20]:
                print(word, "", end='')
            print("...")
        else:
            for word in docs_backup[s_dID]['.W']:
                print(word, "", end='')
    print("")


def doc_vectorial_print(dID, c, docs_backup):
    print("- - - - -")
    print("ID : ", dID)
    for word in docs_backup[dID]['.T']:
        print(word, "", end='')
    print("")
    print("Similarity: ", c)
    print("Date: ", end='')
    for word in docs_backup[dID]['.B']:
        print(word, "", end='')
    print("")
    print("Snippet: ", end='')
    if len(docs_backup[dID]['.W']) == 0:
        print("No preview available for this article")
    else:
        if len(docs_backup[dID]['.W']) > 20:
            for word in docs_backup[dID]['.W'][:20]:
                print(word, "", end='')
            print("...")
        else:
            for word in docs_backup[dID]['.W']:
                print(word, "", end='')
    print("")


def vectorial_print(docID_cos_sim, duration, docs_backup):
    """Print the results"""
    to_print = [(dID, c) for dID, c in docID_cos_sim if c != 0]
    print("Temps de réponse :", duration, "s.")
    if len(to_print) != 0:
        print("Voici les documents triés par ordre de pertinence (similarités nulles exclues) : ")
        for dID, c in to_print:
            doc_vectorial_print(dID, c, docs_backup)
    else:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    print("- - - - -")

