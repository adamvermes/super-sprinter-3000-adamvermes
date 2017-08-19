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
        fieldnames = ['Story line', 'User Story', 'Acceptance Criteria', 'BV', 'Est']
        with open('form.csv', 'w') as file:
            csvfile = csv.writer(file)
            csvfile.writerow(fieldnames)
    return redirect('/')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
