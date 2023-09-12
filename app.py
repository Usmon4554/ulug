from flask import Flask, render_template, request

app = Flask(__name__)


data =[ {'name' : 'byd 2022',
     'description': "Lorem ipsum dolor sit amet"
     },
     {'name' : "matiz 2022", "description": "Eng zor car"},
     {'name' : 'spark 1922', "description": "1922"}

]


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/search')
def search():
    s = request.args['s']
    # for k in data:
    #     if s.lower() in k['name']:
    #         return render_template('search.html', s=k['name'], d=k['description'])
    #     else:
    #         return "Fuck you"

    for k in data:
        if s.lower() in k['name']:
            return render_template('search.html', s=s.lower(), data=data)
    
    



if __name__ == "__main__":
    app.run(debug=True)

