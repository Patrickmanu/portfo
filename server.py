from flask import Flask, render_template, abort, request, Response
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


# def write_to_file(data):
#     with open('web-server-project/database.txt', mode='a') as database:
#         name = data['name']
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{name},{email},{subject},{message}')


def write_to_csv(data):
    with open('web-server-project/database.csv', newline='', mode='a') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return Response('Data written to file!', status=200, mimetype='text/plain')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong try again!'


if __name__ == '__main__':
    app.run(debug=True)
