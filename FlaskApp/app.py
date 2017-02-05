from flask import Flask, render_template, request
from cacm.F_Booleen_Front import *
from cacm.G_Vectorial_Front import *
from ast import literal_eval
from FlaskApp.jsonToHTMLBoolean import *
from FlaskApp.jsonToHTMLVectorial import *
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/boolean_search')
def boolean_search():
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
    result = modele_booleen_front(term_termID, docID_doc, termID_docID, docs_backup, params)
    wrap_result_in_html_boolean(result, params)
    return render_template('result.html')


@app.route('/vect_search')
def vect_search():
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
    with open("../FlaskApp/documents/docID_termID.json", "r") as doc:
        docID_termID_string = doc.read()
        docID_termID = literal_eval(docID_termID_string)
    result = modele_vectoriel_front(term_termID, docID_doc, termID_docID, docID_termID, docs_backup, params)
    wrap_result_in_html_vectorial(result, params)
    return render_template('result.html')


@app.route('/monkey')
def monkey():
    return render_template('monkey.html')

if __name__ == "__main__":
    app.run()
