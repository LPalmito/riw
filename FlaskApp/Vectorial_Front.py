from cacm.D_1_vectorial_main import *
import pprint


def modele_vectoriel_front(term_termID, docID_doc, termID_docID, docID_termID, docs_backup, query):

    docID_cos_sim = vectorial_search_front(query, term_termID, docID_doc, termID_docID, docID_termID, docs_backup, 1)
    search_to_front = {}
    list_sim = []
    min_max_sim = 0
    if len(docID_cos_sim) == 0:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    else:
        for element in docID_cos_sim:
            if element[1] != 0:
                title = ""
                for word_in_title in docs_backup[element[0]]['.T']:
                    title += word_in_title + " "
                date = ""
                for word_in_date in docs_backup[element[0]]['.B']:
                    date += word_in_date + " "
                text = ""
                for word_in_text in docs_backup[element[0]]['.W']:
                    text += word_in_text + " "
                if len(list_sim) < 10:
                    search_to_front[element[0]] = [title, date, text, element[1]]
                    list_sim.append(element[1])
                    min_max_sim = min(list_sim)
                else:
                    if element[1] > min_max_sim:
                        search_to_front.pop(min_max_sim)
                        search_to_front[element[0]] = [title, date, text, element[1]]
                        min_max_sim = min(list_sim)
                    else:
                        pass
    return search_to_front


def vectorial_search_front(query, term_termID, docID_doc, termID_docID, docID_termID, docs_backup, m):
    # Initialisations
    docID_cos_sim = []
    # Compute the query-related cosinus
    tID_dID = update_termID_docID_front(query, termID_docID, term_termID)
    w_query, s_query = get_w_query_front(tID_dID, len(docID_doc), len(term_termID), m)
    # Compute the corpus-related cosinus
    for dID in range(len(docID_doc)):
        if cos_sim_front(dID, termID_docID, docID_termID, len(docID_doc), len(term_termID), m, w_query, s_query) != 0:
            docID_cos_sim.append(
                [dID, cos_sim_front(dID, termID_docID, docID_termID, len(docID_doc), len(term_termID), m, w_query, s_query)])
    docID_cos_sim.sort(key=lambda dID_cos: dID_cos[1], reverse=True)
    return docID_cos_sim


def update_termID_docID_front(query, termID_docID, term_termID):
    """Update the termID_docID with the query"""
    q_tokens = list(set([x.upper() for x in query.split()]))
    tID_dID = termID_docID
    for q_token in q_tokens:
        if q_token in term_termID.keys():
            tID_dID[str(term_termID[q_token])].append(-1)
    return tID_dID


def tf_idf_front(termID, docID, termID_docID, N_docs):
    """Return the tf-idf"""
    tf, df, idf = 0, 0, 0
    df = len(termID_docID[str(termID)])
    for dID in termID_docID[str(termID)]:
        if dID == docID:
            tf += 1
    if df != 0:
        idf = math.log(N_docs / df, 10)
    return tf*idf


def get_w_query_front(tID_dID, N_docs, N_terms, method):
    """Return the weight and the squared norm of the query"""
    w_query, s_query = [], 0
    for t_ID in range(N_terms):
        w_query.append(tf_idf_front(t_ID, -1, tID_dID, N_docs))
        s_query += w_query[t_ID] ** 2
    return w_query, s_query


def cos_sim_front(docID, termID_docID, docID_termID, N_docs, N_terms, method, w_query, s_query):
    """Return the cos similarity"""
    # Create the vectors for the query and the doc according to the chosen method
    num, s_doc = 0, 0
    # 1 <=> tf_idf | 2 <=> n_tf_idf | 3 <=> n_freq
    for t_ID in docID_termID[str(docID)]:
        w_doc_tID = tf_idf_front(t_ID, docID, termID_docID, N_docs)
        num += w_query[t_ID]*w_doc_tID
        s_doc += w_doc_tID**2
    if s_doc == 0 or s_query == 0:
        return 0
    else:
        return num/(s_doc**0.5*s_query**0.5)