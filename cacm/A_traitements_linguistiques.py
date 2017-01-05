import math
import nltk
import matplotlib.pyplot as plt


def traitements_linguistiques(useful_tokens):

    # Question 1 :
    print("----- ----- -----")
    print("Question 1 :")
    T = len(useful_tokens)
    print("Le nombre T de tokens dans .T, .W, .K est : ", T)

    # Question 2 :
    print("----- ----- -----")
    print("Question 2 :")
    unique_useful_tokens = list(set(useful_tokens))
    M = len(unique_useful_tokens)
    print("La taille M du vocabulaire est :", M)

    # Question 3 :
    print("----- ----- -----")
    print("Question 3 :")
    half_useful_tokens = useful_tokens[:int(len(useful_tokens) / 2)]
    unique_half_useful_tokens = list(set(half_useful_tokens))
    T2 = len(half_useful_tokens)
    print("Le nombre T2 de tokens dans .T, .W, .K pour la moitié de la collection est : ", T2)
    M2 = len(unique_half_useful_tokens)
    print("La taille M2 du vocabulaire pour la moitié de la collection est :", M2)
    b = math.log(M / M2, 2)
    print("b = ", b)
    k = M / T ** b
    print("k = ", k)

    # Question 4 :
    print("----- ----- -----")
    print("Question 4 :")
    M_1M = math.floor(k * 1000000 ** b)
    print("La taille M_1M du vocabulaire pour 1 million de tokens est : ", M_1M)

    # Find the frequencies of the words
    frequencies_list = nltk.FreqDist(useful_tokens).most_common()
    frequencies_list.sort(key=lambda t: t[1], reverse=True)

    # Fill the ranks and the frequencies lists
    ranks = []
    frequencies = []
    for rank, frequency in enumerate(frequencies_list):
        ranks.append(rank)
        frequencies.append(frequency[1])

    # # Question 5 :
    # print("----- ----- -----")
    # print("Question 5 :")
    # plt.figure(1)
    # plt.subplot(211)
    # plt.title('f en fonction de r')
    # plt.plot(ranks, frequencies)
    # log_ranks = [math.log(rank + 1) for rank in ranks]
    # log_frequencies = [math.log(frequency) for frequency in frequencies]
    # plt.subplot(212)
    # plt.title('log(f) en fonction de log(r)')
    # plt.plot(log_ranks, log_frequencies)
    # print("Graphes affichés.")
    # plt.show()

    return unique_useful_tokens