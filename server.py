from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def info():
    print('Got POST Info')
    print(request.form)
    name_form = request.form['name']
    dojo_loc = request.form['dojo']
    lang_form = request.form['language']
    comment = request.form['text']
    return render_template('submit.html', name_temp = name_form, dojo_temp = dojo_loc, lang_temp = lang_form, text_temp = comment)








if __name__=="__main__":
    app.run(debug=True)