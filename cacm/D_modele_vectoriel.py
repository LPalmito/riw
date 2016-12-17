import math
from cacm.C_modele_booleen import *


def modele_vectoriel(term_termID, doc_docID, termID_docID):
    # Take user input and calculate the cos of similitude
    docID_cos_sim = []
    m = int(input("Choisissez votre méthode de pondération entre les 3 suivantes en tapant son numéro: \n"
          "1/ tf-idf \n"
          "2/ tf-idf normalisé\n"
          "3/ fréquence normalisée\n"))
    query = input("Entrez votre recherche ici : ")
    tID_qID = termID_queryID(query, term_termID)
    for dID in range(len(doc_docID)):
        print("Computing cos for ", dID, "...")
        docID_cos_sim.append((dID, cos_sim(dID, termID_docID, tID_qID, len(term_termID), len(doc_docID), m)))
    docID_cos_sim.sort(key=lambda dID_cos: dID_cos[1], reverse=True)
    # Display properly the results
    print("Voici les documents triés par ordre de pertinence : ")
    for dID, c in docID_cos_sim:
        print("- - - - -")
        print("Similarité : ", c)
        print("ID : ", dID)
        print("Contenu : ", docID_to_docs(dID, doc_docID))
    print("- - - - -")


def tf_idf(termID, docID, termID_docID, N_docs):
    """Return the tf_idf"""
    tf = 0
    df = 0
    idf = 0
    for tID, dID in termID_docID:
        if tID == termID:
            df += 1
            if (tID, dID) == (termID, docID):
                tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    return tf*idf


def n_tf_idf(termID, docID, termID_docID, N_docs):
    """Return the normalized tf_idf"""
    tf = 0
    df = 0
    n_tf = 0
    idf = 0
    for tID, dID in termID_docID:
        if tID == termID:
            df += 1
            if (tID, dID) == (termID, docID):
                tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    if tf != 0:
        n_tf = 1 + math.log(tf(termID, docID, termID_docID), 10)
    return n_tf*idf


def n_freq(termID, docID, termID_docID, N_terms):
    """Return the normalized frequence"""
    num_tf = 0
    max_tf = 0
    for t_ID in range(N_terms):
        tf = 0
        for tID, dID in termID_docID:
            if (tID, dID) == (t_ID, docID):
                tf += 1
                if t_ID == termID:
                    num_tf += 1
        if tf > max_tf:
            max_tf = tf
    if max_tf == 0:
        return 0
    else:
        return num_tf/max_tf


# TODO: How to optimize the code here?
def cos_sim(docID, termID_docID, tID_qID, N_terms, N_docs, method):
    """Return the cos similarity"""
    # Create the vectors for the query and the doc according to the chosen method
    num = 0
    s_query = 0
    s_doc = 0
    # 1 <=> tf_idf | 2 <=> n_tf_idf | 3 <=> n_freq
    if method in [1, 2, 3]:
        for t_ID in range(N_terms):
            print("Computing dimension: ", t_ID, "/", N_terms)
            if method == 1:
                w_query_tID = tf_idf(t_ID, -1, tID_qID, N_docs)
                w_doc_tID = tf_idf(t_ID, docID, termID_docID, N_docs)
                num += w_query_tID*w_doc_tID
                s_query += w_query_tID**2
                s_doc += w_doc_tID**2
            elif method == 2:
                w_query_tID = n_tf_idf(t_ID, -1, tID_qID, N_docs)
                w_doc_tID = n_tf_idf(t_ID, docID, termID_docID, N_docs)
                num += w_query_tID * w_doc_tID
                s_query += w_query_tID ** 2
                s_doc += w_doc_tID ** 2
            elif method == 3:
                w_query_tID = n_freq(t_ID, -1, tID_qID, N_docs)
                w_doc_tID = n_freq(t_ID, docID, termID_docID, N_docs)
                num += w_query_tID * w_doc_tID
                s_query += w_query_tID ** 2
                s_doc += w_doc_tID ** 2
    else:
        print("La méthode de pondération que vous souhaitez utiliser n'existe pas ou n'a pas été implémentée.")
    if s_doc == 0 or s_query == 0:
        return 0
    else:
        return num/(s_doc**0.5*s_query**0.5)


def termID_queryID(query, term_termID):
    """Return the termID_queryID for the query"""
    q_tokens = list(set([x.upper() for x in query.split()]))
    tID_qID = []
    for q_token in q_tokens:
        if q_token in term_termID.keys():
            tID_qID.append((term_termID[q_token], -1))
    return tID_qID
