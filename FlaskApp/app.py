from flask import Flask, render_template, request
from riw.cacm.F_Booleen_Front import *
from ast import literal_eval
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/search')
def search():
    # Define parameter of the search
    params = request.args.get("search")
    params = params.upper()
    with open("../FlaskApp/documents/docID_doc.json", "r") as doc:
        docID_doc_string = doc.read()
        docID_doc = literal_eval(docID_doc_string)
    with open("../FlaskApp/documents/docs_backup.json", "r") as doc:
        docs_backup_string = doc.read()
        docs_backup = literal_eval(docs_backup_string)
    with open("../FlaskApp/documents/term_termID.json", "r") as doc:
        term_termID_string = doc.read()
        term_termID = literal_eval(term_termID_string)
    with open("../FlaskApp/documents/termID_docID.json", "r") as doc:
        termID_docID_string = doc.read()
        termID_docID = literal_eval(termID_docID_string)
    return modele_booleen_front(term_termID, docID_doc, termID_docID, docs_backup, params)

if __name__ == "__main__":
    app.run()
