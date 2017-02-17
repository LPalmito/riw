import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def boolean_print(s_dID, docs_backup):
    print("- - - - -")
    print("ID : ", s_dID)
    for word in docs_backup[s_dID]['.T']:
        print(word, "", end='')
    print("")
    print("Date: ", end='')
    for word in docs_backup[s_dID]['.B']:
        print(word, "", end='')
    print("")
    print("Snippet: ", end='')
    if len(docs_backup[s_dID]['.W']) == 0:
        print("No preview available for this article")
    else:
        if len(docs_backup[s_dID]['.W']) > 20:
            for word in docs_backup[s_dID]['.W'][:20]:
                print(word, "", end='')
            print("...")
        else:
            for word in docs_backup[s_dID]['.W']:
                print(word, "", end='')
    print("")


def doc_vectorial_print(dID, c, docs_backup):
    print("- - - - -")
    print("ID : ", dID)
    for word in docs_backup[dID]['.T']:
        print(word, "", end='')
    print("")
    print("Similarity: ", c)
    print("Date: ", end='')
    for word in docs_backup[dID]['.B']:
        print(word, "", end='')
    print("")
    print("Snippet: ", end='')
    if len(docs_backup[dID]['.W']) == 0:
        print("No preview available for this article")
    else:
        if len(docs_backup[dID]['.W']) > 20:
            for word in docs_backup[dID]['.W'][:20]:
                print(word, "", end='')
            print("...")
        else:
            for word in docs_backup[dID]['.W']:
                print(word, "", end='')
    print("")


def vectorial_print(docID_cos_sim, duration, docs_backup):
    """Print the results"""
    to_print = [(dID, c) for dID, c in docID_cos_sim if c != 0]
    print("Temps de réponse :", duration, "s.")
    if len(to_print) != 0:
        print("Voici les documents triés par ordre de pertinence (similarités nulles exclues) : ")
        for dID, c in to_print:
            doc_vectorial_print(dID, c, docs_backup)
    else:
        print("Il n'y a aucun document présent dans le corpus correspondant à votre recherche.")
    print("- - - - -")


def print_pertinence(ranks, P, R, e_measures, f_measures, map):
    """Print the results"""

    # Fewer ranks for display
    fewer_ranks = [ranks[k] for k in range(len(ranks)) if k % 2 == 0]

    # Create patches for the legend
    pr_patches = []
    colors = ['black', 'blue', 'cyan']
    for i, r in enumerate(fewer_ranks):
        c = colors[i % len(colors)]
        l = 'Rang ' + str(r)
        pr_patches.append(mpatches.Patch(color=c, label=l))
    ef_patches = [
        mpatches.Patch(color='blue', label='E-mesure'),
        mpatches.Patch(color='green', label='F-mesure')
    ]
    map_patches = [
        mpatches.Patch(color='black', label='tf-idf'),
        mpatches.Patch(color='blue', label='tf-idf normalisé(e)')
    ]

    # Create the precision / recall graph for tf-idf method
    plt.figure(1)
    plt.title('Précision en fonction du rappel pour la méthode tf-idf')
    for i, r in enumerate(fewer_ranks):
        plt.scatter(list(R[r][0].values()), list(P[r][0].values()),
                    marker='o', linestyle='--', color=colors[i % len(colors)])
    plt.legend(handles=pr_patches)

    # Create the precision / recall graph for normalized(e) tf-idf method
    plt.figure(2)
    plt.title('Précision en fonction du rappel pour la méthode tf-idf normalisé(e)')
    for i, r in enumerate(fewer_ranks):
        plt.scatter(list(R[r][1].values()), list(P[r][1].values()),
                    marker='o', linestyle='--', color=colors[i % len(colors)])
    plt.legend(handles=pr_patches)

    # Mean Average Precision / rank graph for tf-idf method
    plt.figure(3)
    plt.title('Mean Average Precision en fonction du rang')
    for m in range(2):
        plt.plot(ranks, list(map[m].values()),
                    marker='o', linestyle='--', color=colors[m % len(colors)])
    plt.legend(handles=map_patches)

    # Create the e-measure and f-measure / rank graph
    plt.figure(4)
    plt.title('E-mesure et F-mesure en fonction du rang')
    moy_e_measures, moy_f_measures = [], []
    for r in ranks:
        e_measures_list = list(e_measures[r][0].values())
        moy_e_measures.append(sum(e_measures_list)/len(e_measures_list))
        f_measures_list = list(f_measures[r][0].values())
        moy_f_measures.append(sum(f_measures_list)/len(f_measures_list))
    plt.plot(ranks, moy_e_measures)
    plt.plot(ranks, moy_f_measures)
    plt.legend(handles=ef_patches)

    print("Graphes affichés.")
    plt.show()
