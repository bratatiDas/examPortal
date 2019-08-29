from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ExamPortal.html')

if __name__ =='__main__':
    app.run(debug=True,port=6530)
