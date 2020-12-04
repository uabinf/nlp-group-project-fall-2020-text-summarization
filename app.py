import flask
from flask import Flask, request, render_template, Response
import json
from T5 import T5_summarization
from read import read_article
from Text_Rank import summary

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    print(request.files)
    input_file = request.files['file']
    # print(input_file.stream)  
    # fileRead = open(input_file,"r")
    read_article = input_file.read()
    # print(str(read_article))
    read_json = {}
    read_json['fileData'] = str(read_article)
    return flask.jsonify(read_json)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("in try")
        original_data = request.json['input_text']
        sum_words = request.json['num_words']
        num_beams = request.json['num_beams']
        model = request.json['model']
        if model.lower() == 'sum':
            # print("here")
            output = summary(original_data)
            # print("error")
        else:
            output = T5_summarization(original_data, num_beams, sum_words)
        response = {}
        response['response'] = {
            'summary': str(output),
            'model': model.lower()
        }
        return flask.jsonify(response)
    except Exception as ex:
        res = dict({'message': str(ex)})
        print(res)
        return app.response_class(response=json.dumps(res), status=500, mimetype='application/json')

@app.route('/download', methods=['POST'])
def download():
    sum_out = request.form['summary_given']
    print(sum_out)
    return Response(sum_out, mimetype="text/plain", headers={"Content-Disposition":"attachment;filename=output.txt"})
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8000, use_reloader=False)
