from cacm.tokenization import render_documents
import nltk
from cacm.D_modele_vectoriel import vectorial_search
import pprint
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from copy import deepcopy


def mesure_pertinence(term_termID, docID_doc, termID_docID, docID_termID):

    # General initialisations
    queryID_query = get_queryID_query()
    qID_rdocID = get_qID_rdocID()
    ranks = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100]

    # Initialisation of t
    t = {}
    for qID in range(64):
        t[qID] = len(qID_rdocID[qID])

    # Initialisation of p, tp, P, R, e_measures and f_measures
    # p = positive, n = negative
    # t = true, f = false
    # For example: 'tp[r][m][qID]' is the number of true positives for the request qID using method m+1 at rank r
    p = {}
    for r in ranks:
        p[r] = {}
        for m in range(2):
            p[r][m] = {}
            for qID in range(64):
                p[r][m][qID] = 0
    tp = deepcopy(p)
    P = deepcopy(p)
    R = deepcopy(p)
    e_measures = deepcopy(p)
    f_measures = deepcopy(p)

    # Compute p and tp
    docID_cos_sim = []
    for r in ranks:
        for m in range(2):
            count = 0
            for qID, query in queryID_query.items():
                if r == ranks[0]:
                    print('Calculs en cours...', m+1, '/ 2 |', qID, '/ 63')
                    docID_cos_sim = vectorial_search(query, term_termID, docID_doc, termID_docID, docID_termID, m+1)[0]
                for docID, cos_sim in docID_cos_sim:
                    if count <= r:
                        if cos_sim > 0:
                            p[r][m][qID] += 1
                            count += 1
                        if docID in qID_rdocID[qID]:
                            tp[r][m][qID] += 1
                    else:
                        break

    # Compute P, R, e_measures, and f_measures
    for r in ranks:
        for m in range(2):
            for qID in queryID_query:
                if p[r][m][qID] != 0:
                    P[r][m][qID] = tp[r][m][qID] / p[r][m][qID]
                else:
                    P[r][m][qID] = 1
                if t[qID] != 0:
                    R[r][m][qID] = tp[r][m][qID] / t[qID]
                else:
                    R[r][m][qID] = 1
            e_measures[r][m][qID] = e_measure(P[r][m][qID], R[r][m][qID])
            f_measures[r][m][qID] = f_measure(P[r][m][qID], R[r][m][qID])

    # Create patches for the legend
    patches = []
    colors = ['blue', 'green', 'yellow', 'orange', 'red']
    for i, r in enumerate(ranks):
        c = colors[i % len(colors)]
        l = 'Rang ' + str(r)
        patches.append(mpatches.Patch(color=c, label=l))

    # Create the graph
    plt.figure(1)
    plt.title('Précision en fonction du rappel')
    for r in ranks:
        plt.plot(list(P[r][0].values()), list(R[r][0].values()))
    plt.legend(handles=patches)
    print("Graphes affichés.")
    plt.show()

    # pprint.pprint(P)
    # pprint.pprint(R)
    # pprint.pprint(e_measures)
    # pprint.pprint(f_measures)


def e_measure(precision, recall):
    if precision + recall != 0:
        return 1 - 2 * precision * recall / (precision + recall)
    else:
        return 1


def f_measure(precision, recall):
    if precision + recall != 0:
        return 2 * precision * recall / (precision + recall)
    else:
        return 0


def r_measure(precision, recall):
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
