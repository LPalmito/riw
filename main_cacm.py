import nltk
import math

if __name__ == '__main__':

    # Open and read cacm.all
    cacm = open('./Ressources/CACM/cacm.all')
    text = cacm.read()

    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Question 1 :
    T = len(tokens)
    print("Le nombre T de tokens est : ", T)

    # Find the vocabulary
    unique_tokens = list(set(tokens))
    # Question 2 :
    M = len(unique_tokens)
    print("La taille M du vocabulaire est :", M)

    # Take half of the collection
    half_tokens = tokens[:int(len(tokens)/2)]
    unique_half_tokens = list(set(half_tokens))
    # Question 3 :
    T2 = len(half_tokens)
    print("Le nombre T2 de tokens pour la moitié de la collection est : ", T2)
    M2 = len(unique_half_tokens)
    print("La taille M2 du vocabulaire pour la moitié de la collection est :", M2)
    b = math.log(M/M2, 2)
    print("b = ", b)
    k = M/T**b
    print("k = ", k)

    # Close cacm.all
    cacm.close()
