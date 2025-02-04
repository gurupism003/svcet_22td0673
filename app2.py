from flask import Flask, render_template, request
from forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a real secret key

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
