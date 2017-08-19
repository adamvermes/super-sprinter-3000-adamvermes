from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('list.html')


@app.route('/story', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/story/edit', methods=['POST'])
def save():
    if request.method == 'POST':
        print("POST request completed")
        form = request.form
        with open('form.csv', 'a') as file:
            writer = csv.writer(file)
            for key, value in form.items():
                writer.writerow([key, value])
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
