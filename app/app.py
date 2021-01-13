from flask import Flask


app = Flask(__name__)



from app import app
from flask import jsonify
from flask import render_template
from flask import Flask, request
from iperf import triggerIperf

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="homepage")

#trigger in background iperf test
@app.route('/backgroundIperf')
def backgroundIperf():
    iperf_result = triggerIperf()
    return jsonify(iperf_result)



if __name__ == 'main':
    app.run()