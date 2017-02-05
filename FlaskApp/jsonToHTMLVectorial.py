def wrap_result_in_html_vectorial(json, params):
    filename = "../FlaskApp/templates/" + params + "_vectorial.html"
    with open(filename, 'w') as result_html:
        result_html.truncate()
        wrapper = wrapper_header
        wrapper += params
        wrapper += wrapper_title + params + """</h3>"""
        i = 0
        for key, document in json.items():
            if i < 10:
                wrapper += """<div><h4>""" + document[0] + " – " + "ID du doc : " + str(key) + " – " + "Similarité : " + \
                           str(document[3]) + """</h4>""" \
                           + """<div>""" + "<i>Date : " + document[1] + "</i></div>" + \
                           "<div>" + document[2][:140] + "..." + "</div></div>"
                i += 1
            else:
                break
        if i == 10:
            wrapper += wrapper_if_more_results
        wrapper += wrapper_footer
        result_html.write(wrapper)
        result_html.close()

wrapper_header = """<!DOCTYPE html>
                     <html lang="en">
                     <head>
                        <meta charset="UTF-8">
                        <title>"""

wrapper_title = """</title>
                      </head>
                      <body>
                      <h3>Voici les résultats de votre requête """

wrapper_if_more_results = """<h3>Il existe d'autres résultats. :)</h3>"""

wrapper_footer = """</body>
                      </html>"""
