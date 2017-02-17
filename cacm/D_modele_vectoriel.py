import math
from cacm.C_modele_booleen import *
from cacm.print_tools import vectorial_print


def modele_vectoriel(term_termID, docID_doc, termID_docID, docID_termID, docs_backup):
    """Take user input and calculate the query-related vertices"""
    m = int(input("Choisissez votre méthode de pondération entre les 3 suivantes en tapant son numéro: \n"
          "1/ tf-idf \n"
          "2/ tf-idf normalisé\n"
          "3/ fréquence normalisée\n"))
    query = input("Entrez votre recherche ici : ")
    docID_cos_sim, duration = vectorial_search(query, term_termID, docID_doc, termID_docID, docID_termID, m)
    vectorial_print(docID_cos_sim, duration, docs_backup)


def tf_idf(termID, docID, termID_docID, N_docs):
    """Return the tf-idf"""
    tf, df, idf = 0, 0, 0
    df = len(termID_docID[termID])
    if docID in termID_docID[termID]:
        tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    return tf*idf


def n_tf_idf(termID, docID, termID_docID, N_docs):
    """Return the normalized tf-idf"""
    tf, df, idf, n_tf = 0, 0, 0, 0
    df = len(termID_docID[termID])
    if docID in termID_docID[termID]:
        tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    if tf != 0:
        n_tf = 1 + math.log(tf, 10)
    return n_tf*idf


def n_freq(termID, docID, termID_docID, N_terms):
    """Return the normalized frequency"""
    num_tf, max_tf = 0, 0
    for t_ID in range(N_terms):
        tf = 0
        if docID in termID_docID[t_ID]:
            tf += 1
            if t_ID == termID:
                num_tf += 1
        if tf > max_tf:
            max_tf = tf
    if max_tf == 0:
        return 0
    else:
        return num_tf/max_tf


def cos_sim(docID, termID_docID, docID_termID, N_docs, N_terms, method, w_query, s_query):
    """Return the cos similarity"""
    # Create the vectors for the query and the doc according to the chosen method
    num, s_doc = 0, 0
    # 1 <=> tf_idf | 2 <=> n_tf_idf | 3 <=> n_freq
    if method in [1, 2, 3]:
        for t_ID in docID_termID[docID]:
            if method == 1:
                w_doc_tID = tf_idf(t_ID, docID, termID_docID, N_docs)
                num += w_query[t_ID]*w_doc_tID
                s_doc += w_doc_tID**2
            elif method == 2:
                w_doc_tID = n_tf_idf(t_ID, docID, termID_docID, N_docs)
                num += w_query[t_ID] * w_doc_tID
                s_doc += w_doc_tID ** 2
            elif method == 3:
                w_doc_tID = n_freq(t_ID, docID, termID_docID, N_terms)
                num += w_query[t_ID] * w_doc_tID
                s_doc += w_doc_tID ** 2
    else:
        print("La méthode de pondération que vous souhaitez utiliser n'existe pas ou n'a pas été implémentée.")
    if s_doc == 0 or s_query == 0:
        return 0
    else:
        return num/(s_doc**0.5*s_query**0.5)


def vectorial_search(query, term_termID, docID_doc, termID_docID, docID_termID, m):
    """Return a list of tuples of docID and its associated cos"""
    # Initializations
    start = time.time()
    docID_cos_sim = []

    # Compute the query-related cosinus
    tID_dID = update_termID_docID(query, termID_docID, term_termID)
    w_query, s_query = get_w_query(tID_dID, len(docID_doc), len(term_termID), m)

    # Compute the corpus-related cosinus
    for dID in range(len(docID_doc)):
        docID_cos_sim.append(
            (dID, cos_sim(dID, termID_docID, docID_termID, len(docID_doc), len(term_termID), m, w_query, s_query)))
    docID_cos_sim.sort(key=lambda dID_cos: dID_cos[1], reverse=True)
    end = time.time()
    duration = end - start

    return docID_cos_sim, duration


def get_w_query(tID_dID, N_docs, N_terms, method):
    """Return the weight and the squared norm of the query"""
    w_query, s_query = [], 0
    for t_ID in range(N_terms):
        if method == 1:
            w_query.append(tf_idf(t_ID, -1, tID_dID, N_docs))
            s_query += w_query[t_ID] ** 2
        elif method == 2:
            w_query.append(n_tf_idf(t_ID, -1, tID_dID, N_docs))
            s_query += w_query[t_ID] ** 2
        elif method == 3:
            w_query.append(n_freq(t_ID, -1, tID_dID, N_terms))
            s_query += w_query[t_ID] ** 2
    return w_query, s_query


def update_termID_docID(query, termID_docID, term_termID):
    """Update the termID_docID with the query"""
    q_tokens = list(set([x.upper() for x in query.split()]))
    tID_dID = termID_docID
    for q_token in q_tokens:
        if q_token in term_termID.keys():
            tID_dID[term_termID[q_token]].append(-1)
    return tID_dID
