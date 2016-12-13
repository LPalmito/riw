def modele_booleen(term_termID, doc_docID, termID_docID):
    """Print the results of a single-word search and a CNF search"""
    # For a single word as search
    searched_term = input("Entrez un mot à rechercher dans les documents : ").upper()
    searched_docIDs = search_term_in_corpus(searched_term, term_termID, termID_docID)
    searched_docs = docIDs_to_docs(searched_docIDs, doc_docID)
    print(searched_docs)

    # For a normal conjunctive expression
    searched_expression = input("Entrez une expression booléenne sous forme normale conjonctive comme dans l'exemple"
                              "\nex: 1.2+3.4 = (1) AND (2 OR 3) AND (4) : ").upper()
    searched_docIDs_2 = search_expression_in_corpus(searched_expression, term_termID, termID_docID, len(doc_docID))
    searched_docs_2 = docIDs_to_docs(searched_docIDs_2, doc_docID)
    print(searched_docs_2)


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


def docIDs_to_docs(docIDs, doc_docID):
    """Return a list of docs corresponding to the docIDs given"""
    docs = []
    for doc, docID in doc_docID:
        if docID in docIDs:
            docs.append(doc)
    return docs
