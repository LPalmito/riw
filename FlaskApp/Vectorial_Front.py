from operator import itemgetter
from FlaskApp.Vectorial_Front_Tools import *


def vectorial_model_front(term_termID, docID_doc, termID_docID, docID_termID, docs_backup, query):

    docID_cos_sim = vectorial_search_front(query, term_termID, docID_doc, termID_docID, docID_termID, 1)
    search_to_front = []
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
                    search_to_front.append([element[0], title, date, text, element[1]])
                    list_sim.append(element[1])
                    min_max_sim = min(list_sim)
                    search_to_front = sorted(search_to_front, key=itemgetter(4), reverse=True)
                else:
                    if element[1] > min_max_sim:
                        del search_to_front[len(search_to_front)-1]
                        search_to_front.append([element[0], title, date, text, element[1]])
                        list_sim.append(element[1])
                        min_max_sim = min(list_sim)
                        search_to_front = sorted(search_to_front, key=itemgetter(4), reverse=True)
                    else:
                        pass
    return search_to_front
