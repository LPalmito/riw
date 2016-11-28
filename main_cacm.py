import nltk
import math


def render_documents(tokens):
    markers = ['.I', '.T', '.W', '.B', '.A', '.N', '.X', '.K']
    current_marker = ''

    doc = {}
    for i, token in enumerate(tokens):
        if token in markers:
            current_marker = token
        else:
            doc[current_marker].push(token)
    test = doc

if __name__ == '__main__':

    # Open and read cacm.all
    cacm = open('./Resources/CACM/cacm.all')
    text = cacm.read()

    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    print("100 tokens:", tokens[:99])
    # # Question 1 :
    # T = len(tokens)
    # print("Le nombre T de tokens est : ", T)
    #
    # # Find the vocabulary
    # unique_tokens = list(set(tokens))
    # # Question 2 :
    # M = len(unique_tokens)
    # print("La taille M du vocabulaire est :", M)
    #
    # # Take half of the collection
    # half_tokens = tokens[:int(len(tokens)/2)]
    # unique_half_tokens = list(set(half_tokens))
    # # Question 3 :
    # T2 = len(half_tokens)
    # print("Le nombre T2 de tokens pour la moitié de la collection est : ", T2)
    # M2 = len(unique_half_tokens)
    # print("La taille M2 du vocabulaire pour la moitié de la collection est :", M2)
    # b = math.log(M/M2, 2)
    # print("b = ", b)
    # k = M/T**b
    # print("k = ", k)

    # Close cacm.all
    cacm.close()
