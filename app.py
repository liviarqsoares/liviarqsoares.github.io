from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    principal = float(request.form['principal'])
    rate = float(request.form['rate'])
    time = float(request.form['time'])
    result = principal + (principal * rate * time)
    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)