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
    print("Text: ", end='')
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
