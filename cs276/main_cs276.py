from cs276.tokenization import *

from cs276.A_traitements_linguistiques import *

if __name__ == '__main__':

    # Prepare cs276 corpus
    useful_tokens = get_cs276_tokens()

    print("\n------------------------------------------------------------")
    print("| 2.1 / A Traitements linguistiques                         |")
    print("------------------------------------------------------------")
    traitements_linguistiques(useful_tokens)
