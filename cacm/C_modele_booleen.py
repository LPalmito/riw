def modele_booleen(term_termID, doc_docID, termID_docID):
    """Print the results of a single-word search and a CNF search"""
    # Take user input for a single word as search
    searched_term = input("Entrez un mot à rechercher dans les documents : ").upper()
    searched_docIDs = search_term_in_corpus(searched_term, term_termID, termID_docID)
    # Display properly the results
    if len(searched_docIDs) == 0:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    else:
        print("Les documents correspondant à votre recherche sont :")
        for s_dID in searched_docIDs:
            print("- - - - -")
            print("ID : ", s_dID)
            print("Contenu : ", docID_to_docs(s_dID, doc_docID))
    print("- - - - -")
    # Take user input for a normal conjunctive expression
    searched_expression = input("Entrez une expression sous forme normale conjonctive comme dans l'exemple suivant :\n"
                                "ex: 1.2+3.4 = (1) AND (2 OR 3) AND (4)\n").upper()
    searched_docIDs_2 = search_expression_in_corpus(searched_expression, term_termID, termID_docID, len(doc_docID))
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
        for termID, docID in termID_docID:
            if termID == searched_termID:
                searched_docIDs.append(docID)
        return searched_docIDs
    else:
        # If the searched term is not in the corpus
        return []


def search_expression_in_corpus(searched_expression, term_termID, termID_docID, len_corpus):
    """Return ths list of docIDs where the searched expression is"""
    # Produce 'search_terms' as a list of list of tuples:
    # ex: A.B+C.-D <=> (A) AND (B OR C) AND (NOT D) <=> [ [(A,True)], [(B,True),(C,True)], [(D, False)] ]
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
    result = result_list[0]
    for i, r in enumerate(result_list[0]):
        for sub_res in result_list[1:]:
            if r not in sub_res:
                del result[i]
    return result


def docID_to_docs(docID, doc_docID):
    """Return the doc corresponding to the given docID"""
    for d, dID in doc_docID:
        if docID == dID:
            return d
