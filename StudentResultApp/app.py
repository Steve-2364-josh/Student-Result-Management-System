from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():

    student_name = request.form['student_name']

    english = int(request.form['english'])
    tamil = int(request.form['tamil'])
    maths = int(request.form['maths'])
    science = int(request.form['science'])
    social = int(request.form['social'])

    marks = [english, tamil, maths, science, social]

    total = sum(marks)
    maximum = max(marks)
    minimum = min(marks)

    percentage = round(total / 5, 2)

    # Grade Rules
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Subject-wise Pass Check
    if min(marks) < 35:
        result = "FAIL"
    else:
        result = "PASS"

    return render_template(
        'result.html',
        student_name=student_name,
        total=total,
        maximum=maximum,
        minimum=minimum,
        percentage=percentage,
        grade=grade,
        result=result
    )


if __name__ == '__main__':
    app.run(debug=False)