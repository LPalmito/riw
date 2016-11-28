import nltk
import math
import matplotlib.pyplot as plt


def render_documents(tokens):
    # Initialisations
    markers = ['.I', '.T', '.W', '.B', '.A', '.N', '.X', '.K']
    current_marker = '.I'
    current_doc = {}
    result = []
    # Prepare the result
    for token in tokens:
        # For each new .I, prepare a new doc and fill it
        if token == '.I':
            if current_doc != {}:
                result.append(current_doc)
            current_doc = {}
            for marker in markers:
                current_doc[marker] = []
        # For each other marker, update the current marker
        elif token in markers:
            current_marker = token
        # Else, fill the corresponding attribute
        else:
            current_doc[current_marker].append(token)
    result.append(current_doc)
    return result

if __name__ == '__main__':

    # Open and read cacm.all
    cacm = open('./Resources/CACM/cacm.all')
    text = cacm.read()

    # Tokenize the text and render in docs
    tokens = nltk.word_tokenize(text)
    docs = render_documents(tokens)

    # Keep only the tokens in useful attributes
    useful_tokens = []
    for doc in docs:
        useful_tokens.extend(doc['.T'])
        useful_tokens.extend(doc['.W'])
        useful_tokens.extend(doc['.K'])

    # Question 1 :
    T = len(useful_tokens)
    print("Le nombre T de tokens dans .T, .W, .K est : ", T)

    # Find the vocabulary
    unique_useful_tokens = list(set(useful_tokens))
    # Question 2 :
    M = len(unique_useful_tokens)
    print("La taille M du vocabulaire est :", M)

    # Take half of the collection
    half_useful_tokens = useful_tokens[:int(len(useful_tokens)/2)]
    unique_half_useful_tokens = list(set(half_useful_tokens))
    # Question 3 :
    T2 = len(half_useful_tokens)
    print("Le nombre T2 de tokens dans .T, .W, .K pour la moitié de la collection est : ", T2)
    M2 = len(unique_half_useful_tokens)
    print("La taille M2 du vocabulaire pour la moitié de la collection est :", M2)
    b = math.log(M/M2, 2)
    print("b = ", b)
    k = M/T**b
    print("k = ", k)

    # Question 4 :
    M_1M = math.floor(k*1000000**b)
    print("La taille M_1M du vocabulaire pour 1 million de tokens est : ", M_1M)

    # Close cacm.all
    cacm.close()
