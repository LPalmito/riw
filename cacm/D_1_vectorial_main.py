from cacm.C_boolean_main import *
from cacm.print_tools import vectorial_print
from cacm.D_3_query_updates import *
from cacm.D_2_ponderation_methods import *


def vectorial_main(term_termID, docID_doc, termID_docID, docID_termID, docs_backup):
    """Take user input and calculate the query-related vertices"""
    m = int(input("Choisissez votre méthode de pondération entre les 3 suivantes en tapant son numéro: \n"
          "1/ tf-idf \n"
          "2/ tf-idf normalisé\n"
          "3/ fréquence normalisée\n"))
    query = input("Entrez votre recherche ici : ")
    docID_cos_sim, duration = vectorial_search(query, term_termID, docID_doc, termID_docID, docID_termID, m)
    vectorial_print(docID_cos_sim, duration, docs_backup)


def cos_sim(docID, termID_docID, docID_termID, N_docs, method, w_query, s_query, docID_mtf):
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
                w_doc_tID = n_freq(t_ID, docID, termID_docID, docID_mtf)
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

    docID_mtf = get_docID_mtf(docID_doc, docID_termID, termID_docID, m)

    # Compute the query-related cosinus
    tID_dID = update_termID_docID(query, termID_docID, term_termID)
    dID_tID = update_docID_termID(query, docID_termID, term_termID)
    dID_mtf = update_docID_mtf(docID_mtf, dID_tID, tID_dID)
    w_query, s_query = get_w_query(tID_dID, len(docID_doc), len(term_termID), m, dID_mtf)

    # Compute the corpus-related cosinus
    for dID in range(len(docID_doc)):
        docID_cos_sim.append(
            (dID, cos_sim(dID, termID_docID, docID_termID, len(docID_doc), m, w_query, s_query, docID_mtf)))
    docID_cos_sim.sort(key=lambda dID_cos: dID_cos[1], reverse=True)
    end = time.time()
    duration = end - start

    return docID_cos_sim, duration


def get_w_query(tID_dID, N_docs, N_terms, method, dID_mtf):
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
            w_query.append(n_freq(t_ID, -1, tID_dID, dID_mtf))
            s_query += w_query[t_ID] ** 2
    return w_query, s_query


def get_docID_mtf(docID_doc, docID_termID, termID_docID, m):
    """Compute max_tf for dID"""
    docID_mtf = {}
    for docID in range(len(docID_doc)):
        docID_mtf[docID] = 0
        for t_ID in docID_termID[docID]:
            tfj = 0
            for dID in termID_docID[t_ID]:
                if dID == docID:
                    tfj += 1
            if tfj > docID_mtf[docID]:
                docID_mtf[docID] = tfj
    return docID_mtf
