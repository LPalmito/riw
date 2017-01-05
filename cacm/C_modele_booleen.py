import time


def modele_booleen(term_termID, doc_docID, termID_docID):
    """Print the results of a single-word search and a CNF search"""
    # Take user input for a single word as search
    searched_term = input("Entrez un mot à rechercher dans les documents : ").upper()
    start_1 = time.time()
    searched_docIDs_1 = search_term_in_corpus(searched_term, term_termID, termID_docID)
    end_1 = time.time()
    duration_1 = (end_1-start_1)*1000
    print("Temps de réponse :", duration_1, "ms.")
    # Display properly the results
    if len(searched_docIDs_1) == 0:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    else:
        print("Les documents correspondant à votre recherche sont :")
        for s_dID in searched_docIDs_1:
            print("- - - - -")
            print("ID : ", s_dID)
            print("Contenu : ", docID_to_docs(s_dID, doc_docID))
    print("- - - - -")
    # Take user input for a normal conjunctive expression
    searched_expression = input("Entrez une expression sous forme normale conjonctive comme dans l'exemple suivant :\n"
                                "ex: 1.2+3.-4 = (1) AND (2 OR 3) AND (NOT 4)\n").upper()
    start_2 = time.time()
    searched_docIDs_2 = search_expression_in_corpus(searched_expression, term_termID, termID_docID, len(doc_docID))
    end_2 = time.time()
    duration_2 = (end_2-start_2)*1000
    print("Temps de réponse :", duration_2, "ms.")
    # Display properly the results
    if len(searched_docIDs_2) == 0:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    else:
        print("Les documents correspondant à votre recherche sont :")
        for s_dID in searched_docIDs_2:
            print("- - - - -")
            print("ID : ", s_dID)
            print("Contenu : ", docID_to_docs(s_dID, doc_docID))
    print("- - - - -")


def search_term_in_corpus(searched_term, term_termID, termID_docID):
    """Return the list of docIDs where the search term is"""
    if searched_term in term_termID:
        # Retrieve the corresponding termID
        searched_termID = term_termID[searched_term]
        # Retrieve the corresponding docIDs
        searched_docIDs = []
        for termID, docIDs in termID_docID.items():
            if termID == searched_termID:
                searched_docIDs.extend(docIDs)
        return searched_docIDs
    else:
        # If the searched term is not in the corpus
        return []


def search_expression_in_corpus(searched_expression, term_termID, termID_docID, len_corpus):
    """Return ths list of docIDs where the searched expression is"""
    # Produce 'search_terms' as a list of list of tuples:
    # ex: 1.2+3.-4 <=> (1) AND (2 OR 3) AND (NOT 4) <=> [ [(1,True)], [(2,True),(3,True)], [(4, False)] ]
    search_list = searched_expression.split('.')
    searched_terms = []
    for searched_term in search_list:
        tuple_list = []
        for s in searched_term.split('+'):
            if s[0] == '-':
                tuple_list.append((s[1:], False))
            else:
                tuple_list.append((s, True))
        searched_terms.append(tuple_list)
    # Save the sub results in 'result_list'
    result_list = []
    for or_list in searched_terms:
        res = []
        for term, b in or_list:
            r = search_term_in_corpus(term, term_termID, termID_docID)
            if b:
                res.extend(r)
            else:
                not_r = [x for x in range(len_corpus) if x not in r]
                res.extend(not_r)
        res = list(set(res))
        result_list.append(res)
    # Combine the results of 'result_list'
    result_0, result = result_list[0], []
    while len(result_0) > 0:
        in_every_sub_result = True
        for sub_res in result_list:
            if result_0[0] not in sub_res:
                in_every_sub_result = False
        if in_every_sub_result:
            result.append(result_0[0])
        result_0 = result_0[1:]
    return result


def docID_to_docs(docID, doc_docID):
    """Return the doc corresponding to the given docID"""
    for d, dID in doc_docID:
        if docID == dID:
            return d
