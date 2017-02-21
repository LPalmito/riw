from cacm.C_boolean_main import *


def boolean_model_front(term_termID, docID_doc, termID_docID, docs_backup, search):
    """Print the results of a single-word search and a CNF search"""
    # Take user input for a single word as search
    searched_term = search
    searched_docIDs_1 = search_term_in_corpus(searched_term, term_termID, termID_docID)
    # Display properly the results
    search_to_front = {}
    if len(searched_docIDs_1) == 0:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    else:
        for s_dID in searched_docIDs_1:
            title = ""
            for word_in_title in docs_backup[s_dID]['.T']:
                title += word_in_title + " "
            date = ""
            for word_in_date in docs_backup[s_dID]['.B']:
                date += word_in_date + " "
            text = ""
            for word_in_text in docs_backup[s_dID]['.W']:
                text += word_in_text + " "
            search_to_front[s_dID] = [title, date, text]
    return search_to_front
