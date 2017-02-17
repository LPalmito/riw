from cacm.tokenization import render_documents
import nltk
from cacm.D_1_vectorial_main import vectorial_search
from cacm.print_tools import print_pertinence
from copy import deepcopy


def pertinence_measures(term_termID, docID_doc, termID_docID, docID_termID):

    # General initialisations
    queryID_query = get_queryID_query()
    qID_rdocID = get_qID_rdocID()
    ranks = [5, 10, 20, 50, 100, 200]

    # Initialize all the needed variables
    t, tp, p, P, R, e_measures, f_measures = initialize(ranks, qID_rdocID)

    # Compute p and tp
    p, tp = get_p_and_tp(ranks, docID_termID, queryID_query, term_termID, docID_doc, termID_docID, qID_rdocID, p, tp)

    # Compute P, R, e_measures, and f_measures
    P, R, e_measures, f_measures = get_P_R_e_f(ranks, queryID_query, P, R, p, tp, t, e_measures, f_measures)

    # Compute MAP
    map = get_map(P, ranks)

    # Print the results
    print_pertinence(ranks, P, R, e_measures, f_measures, map)


def e_measure(precision, recall):
    """Return the e-measure"""
    if precision + recall != 0:
        return 1 - 2 * precision * recall / (precision + recall)
    else:
        return 1


def f_measure(precision, recall):
    """Return the f-measure"""
    if precision + recall != 0:
        return 2 * precision * recall / (precision + recall)
    else:
        return 0


def get_queryID_query():
    """Return a dict with queryID as key and the query as value"""
    query_file = open('../Resources/CACM/query.text')
    test_query = query_file.read()
    query_docs = render_documents(test_query)
    queryID_query = {}
    for i, doc in enumerate(query_docs):
        queryID_query[i] = " ".join(doc['.W'])
    query_file.close()
    return queryID_query


def get_qID_rdocID():
    """Return a dict with queryID as key and an array of docIDs as value"""
    rels_file = open('../Resources/CACM/qrels.text')
    text = rels_file.read()
    tokens = nltk.word_tokenize(text)
    rels_dict = {}
    for k in range(64):
        rels_dict[k] = []
    for i, token in enumerate(tokens):
        if i % 4 == 0:
            rels_dict[int(token)-1].append(int(tokens[i+1])-1)
    rels_file.close()
    return rels_dict


def initialize(ranks, qID_rdocID):
    """Initialize t (true), tp (true positive), p (positive), P (precision), R (recall), e_measures, f_measures"""

    # Initialisation of t
    t = {}
    for qID in range(64):
        t[qID] = len(qID_rdocID[qID])

    # Initialisation of p, tp, P, R, e_measures and f_measures
    # For example: 'tp[r][m][qID]' is the number of true positives for the request qID using method m+1 at rank r
    p = {}
    for r in ranks:
        p[r] = {}
        for m in range(3):
            p[r][m] = {}
            for qID in range(64):
                p[r][m][qID] = 0
    tp = deepcopy(p)
    P = deepcopy(p)
    R = deepcopy(p)
    e_measures = deepcopy(p)
    f_measures = deepcopy(p)

    return t, tp, p, P, R, e_measures, f_measures


def get_p_and_tp(ranks, docID_termID, queryID_query, term_termID, docID_doc, termID_docID, qID_rdocID, p, tp):
    """Return the positives and true positives"""
    docID_cos_sim = []
    N_docs = len(docID_termID)
    for r in ranks:
        for m in range(3):
            for qID, query in queryID_query.items():
                count, k = 0, 0
                if r == ranks[0]:
                    print('Calcul en cours...', m + 1, '/ 3 |', qID + 1, '/ 64')
                    docID_cos_sim = \
                        vectorial_search(query, term_termID, docID_doc, termID_docID, docID_termID, m + 1)[0]
                while count < r and k < N_docs:
                    docID, cos_sim = docID_cos_sim[k]
                    if cos_sim > 0:
                        p[r][m][qID] += 1
                        count += 1
                        if docID  in qID_rdocID[qID]:
                            tp[r][m][qID] += 1
                    k += 1
    return p, tp


def get_P_R_e_f(ranks, queryID_query, P, R, p, tp, t, e_measures, f_measures):
    """Return the precision, the recall, the e-measure and the f-measure"""
    for r in ranks:
        for m in range(3):
            for qID in queryID_query:
                if p[r][m][qID] != 0:
                    P[r][m][qID] = tp[r][m][qID] / p[r][m][qID]
                else:
                    P[r][m][qID] = 0
                if t[qID] != 0:
                    R[r][m][qID] = tp[r][m][qID] / t[qID]
                else:
                    R[r][m][qID] = 1
            e_measures[r][m][qID] = e_measure(P[r][m][qID], R[r][m][qID])
            f_measures[r][m][qID] = f_measure(P[r][m][qID], R[r][m][qID])
    return P, R, e_measures, f_measures


def get_map(P, ranks):
    """Compute MAP (Mean Average Precision) for each rank and each method"""
    map = {}
    for m in range(3):
        map[m] = {}
        for r in ranks:
            map[m][r] = sum(list(P[r][m].values()))/len(list(P[r][m].values()))
    return map
