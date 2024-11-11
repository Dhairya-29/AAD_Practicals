from flask import Flask, request, render_template

app = Flask(__name__)

def find_min_sum_pair(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    min_sum = float('inf')
    min_pair = (None, None)

    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            min_pair = (arr[left], arr[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return min_pair

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_numbers = request.form['numbers']
        numbers = list(map(int, input_numbers.split(',')))
        result = find_min_sum_pair(numbers)
    return render_template('index1.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


