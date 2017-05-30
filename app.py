from collections import Counter
from flask import Flask, request
from build_model_py3 import TextClassifier
app = Flask(__name__)


def dict_to_html(d):
    return '<br>'.join('{0}: {1}'.format(k, d[k]) for k in sorted(d))

@app.route('/')
def home_page():
    return '''
        <head>
        	<meta charset="UTF-8">
            <title>My classifier app</title>
        </head>
        <body>
            <h1 style="color:fuscia;font-size:30px;">An app to predict topics of a text file</h1>
            <hr style="border-color:black;">
        	<a href='/submit'>
                <form action='/submit' method="POST">
                    <input type="button" value="Make Dat Model!">
                </form>
            </a
        </body>
        '''

# Form page to submit text
@app.route('/submit', methods=['GET', 'POST'])
def submission_page():
    return '''
        <form action="/fit" method='POST' >
            <input type="text" name="user_input" />
            <input type="submit" value='Enter data as text '/>
        </form>
        <form action="/predict" method='POST' >
            <input type="text" name="user_input" />
            <input type="submit" value='Enter data to predict '>
        '''

@app.route('/fit', methods=['GET', 'POST'])
def make_classifier():
    text = str(request.form['user_input'])
    tc = TextClassifier
    tc.fit(X, y)
    # formatted output string
    page = 'You made a model! Go predict on it!'

    # make html that gives us a button to go back to the home page
    go_to_home_html = '''
        <form action="/" >
            <input type="submit" value = "Predict on data"/>
        </form>
    '''

    return go_to_home_html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
