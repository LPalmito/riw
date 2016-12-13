import math
from enum import Enum
from cacm.C_modele_booleen import *


def modele_vectoriel(term_termID, doc_docID, termID_docID):
    docID_cos_sim = []
    query = input("Entrez votre recherche ici : ")
    for dID in range(len(doc_docID)):
        docID_cos_sim.append((dID, cos_sim(query, dID, termID_docID, term_termID, len(term_termID), len(doc_docID), W.n_tf_idf)))
    print(docID_cos_sim)
    # TODO: Organize the list of tuples and print the results


class W(Enum):
    tf_idf = 1
    n_tf_idf = 2
    n_freq = 3


def tf(termID, docID, termID_docID):
    """Return the tf"""
    tf = 0
    for tID, dID in termID_docID:
        if (tID, dID) == (termID, docID):
            tf += 1
    return tf


def n_tf(termID, docID, termID_docID):
    """Return the normalized tf"""
    if tf(termID, docID, termID_docID) > 0:
        return 1 + math.log(tf(termID, docID, termID_docID), 10)
    else:
        return 0


def idf(termID, termID_docID, N_docs):
    """Return the idf"""
    df = 0
    for tID, dID in termID_docID:
        if tID == termID:
            df += 1
    if df == 0:
        return 0
    else:
        return math.log(N_docs / df, 10)


def tf_idf(termID, docID, termID_docID, N_docs):
    """Return the tf_idf"""
    return tf(termID, docID, termID_docID)*idf(termID, termID_docID, N_docs)


def n_tf_idf(termID, docID, termID_docID, N_docs):
    """Return the normalized tf_idf"""
    return n_tf(termID, docID, termID_docID)*idf(termID, termID_docID, N_docs)


def n_freq(termID, docID, termID_docID, N_terms):
    """Return the normalized frequence"""
    max_tf = max(tf(t_ID, docID, termID_docID) for t_ID in range(N_terms))
    return tf(termID, docID, termID_docID)/max_tf


def cos_sim(query, docID, termID_docID, term_termID, N_terms, N_docs, method):
    """Return the cos similarity"""
    # Create the vectors for the query and the doc according to the chosen method
    tID_qID = termID_queryID(query, term_termID)
    w_query = []
    w_doc = []
    for t_ID in range(N_terms):
        if method == W.tf_idf:
            w_query.append(tf_idf(t_ID, -1, tID_qID, N_docs))
            w_doc.append(tf_idf(t_ID, docID, termID_docID, N_docs))
        elif method == W.n_tf_idf:
            w_query.append(n_tf_idf(t_ID, -1, tID_qID, N_docs))
            w_doc.append(n_tf_idf(t_ID, docID, termID_docID, N_docs))
        elif method == W.n_freq:
            w_query.append(n_freq(t_ID, -1, tID_qID, N_docs))
            w_doc.append(n_freq(t_ID, docID, termID_docID, N_docs))
        else:
            print("La méthode de pondération que vous souhaitez utiliser n'existe pas ou n'a pas été implémentée.")
    # Calculate the cos similarity and return it
    num_list = []
    doc_norm_list = []
    q_norm_list = []
    for i in range(N_terms):
        num_list.append(w_doc[i]*w_query[i])
        doc_norm_list.append(w_doc[i]**2)
        q_norm_list.append(w_query[i]**2)
    num = sum(num_list)
    doc_norm = sum(doc_norm_list)**0.5
    q_norm = sum(q_norm_list)**0.5
    return num/(doc_norm*q_norm)


def termID_queryID(query, term_termID):
    """Return the termID_queryID for the query"""
    q_tokens = list(set([x.upper() for x in query.split()]))
    tID_qID = []
    for q_token in q_tokens:
        if q_token in term_termID.keys():
            tID_qID.append((term_termID[q_token], -1))
    return tID_qID
