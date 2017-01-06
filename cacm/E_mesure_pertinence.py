from cacm.tokenization import get_docs


def mesure_pertinence():
    # Create the docs for the query.text
    query_file = open('./Resources/CACM/query.text')
    test_query = query_file.read()
    query_docs = get_docs(test_query)
    # Create
    rels_file = open('./Resources/CACM/qrels.text')
    test_rels = rels_file.read()
    # TODO: CREATE A FUNCTION TO STORE THE PERTINENCE RESULTS


    query_file.close()
    rels_file.close()


def e_measure(P, R):
    return 1-2*P*R/(P+R)


def f_measure(P, R):
    return 2*P*R/(P+R)


def r_measure(P, R):
    return 0