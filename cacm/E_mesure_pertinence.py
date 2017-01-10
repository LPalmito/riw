from cacm.tokenization import render_documents
import nltk
from cacm.D_modele_vectoriel import vectorial_search


def mesure_pertinence(term_termID, docID_doc, termID_docID, docID_termID):

    # Initialisations
    queryID_query = get_queryID_query()
    qID_rdocID = get_qID_rdocID()

    # p = positive, n = negative
    # t = true, f = false
    # For example: 'tp'[m][qID] is the number of true positives for the request qID using method m+1
    t, p, tp, P, R = {}, {}, {}, {}, {}
    for qID in range(64):
        t[qID] = len(qID_rdocID[qID])
        p[qID] = [0, 0, 0]
        tp[qID] = [0, 0, 0]
        P[qID] = [0, 0, 0]
        R[qID] = [0, 0, 0]

    # Compute the p and tp matrices
    for qID, query in queryID_query.items():
        print(qID)
        for m in range(3):
            docID_cos_sim = vectorial_search(query, term_termID, docID_doc, termID_docID, docID_termID, m+1)[0]
            for docID, cos_sim in docID_cos_sim:
                if cos_sim > 0:
                    p[qID][m] += 1
                if docID in qID_rdocID[qID]:
                    tp[qID][m] += 1

    # Compute the P and R matrices
    for qID in queryID_query:
        print(qID)
        for m in range(3):
            if p[qID][m] != 0:
                P[qID][m] = tp[qID][m] / p[qID][m]
            else:
                P[qID][m] = 0
            if t[qID] != 0:
                R[qID][m] = tp[qID][m] / t[qID]
            else:
                R[qID][m] = 0
            print("m =", m, "P =", P[qID][m], "R =", R[qID][m])

# TODO: Use other notations to avoid the conflict P, R being matrices and integers


def e_measure(P, R):
    return 1-2*P*R/(P+R)


def f_measure(P, R):
    return 2*P*R/(P+R)


def r_measure(P, R):
    # TODO: Find what R-Measure actually is
    return 0


def get_queryID_query():
    query_file = open('./Resources/CACM/query.text')
    test_query = query_file.read()
    query_docs = render_documents(test_query)
    queryID_query = {}
    for i, doc in enumerate(query_docs):
        queryID_query[i] = " ".join(doc['.W'])
    query_file.close()
    return queryID_query


def get_qID_rdocID():
    """Return a dict with queryID as key and an array of docIDs as value"""
    rels_file = open('./Resources/CACM/qrels.text')
    text = rels_file.read()
    tokens = nltk.word_tokenize(text)
    rels_dict = {}
    for k in range(64):
        rels_dict[k] = []
    for i, token in enumerate(tokens):
        if i % 4 == 0:
            rels_dict[int(token)-1].append(int(tokens[i+1]))
    rels_file.close()
    return rels_dict
