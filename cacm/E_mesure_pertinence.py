from cacm.tokenization import render_documents
import nltk


def mesure_pertinence():

    # Create the dict for queries
    query_file = open('./Resources/CACM/query.text')
    test_query = query_file.read()
    query_docs = render_documents(test_query)
    queryID_query = {}
    for i, doc in enumerate(query_docs):
        queryID_query[i] = " ".join(doc['.W'])

    # Create the dict for relevant docs
    rels_file = open('./Resources/CACM/qrels.text')
    test_rels = rels_file.read()
    qID_rdocID = get_qID_rdocID(test_rels)

    query_file.close()
    rels_file.close()


def e_measure(P, R):
    return 1-2*P*R/(P+R)


def f_measure(P, R):
    return 2*P*R/(P+R)


def r_measure(P, R):
    # TODO: Find what R-Measure actually is
    return 0


def get_qID_rdocID(text):
    """Return a dict with queryID as key and an array of docIDs as value"""
    tokens = nltk.word_tokenize(text)
    rels_dict = {}
    for i, token in enumerate(tokens):
        if i % 4 == 0:
            if int(token)-1 not in rels_dict.keys():
                rels_dict[int(token)-1] = [int(tokens[i+1])]
            else:
                rels_dict[int(token)-1].append(int(tokens[i+1]))
    return rels_dict