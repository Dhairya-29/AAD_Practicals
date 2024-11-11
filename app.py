from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/xyz', methods=['POST'])
def home():
    a = [int(request.form.get(f'a{i}')) for i in range(3)]
    b = [int(request.form.get(f'b{i}')) for i in range(3)]
    
    count1 = sum(1 for i in range(3) if a[i] > b[i])
    count2 = sum(1 for i in range(3) if a[i] < b[i])
    
    c = [count1, count2]
    return render_template('index.html', result=c)

if __name__ == '__main__':
    app.run(debug=True)
