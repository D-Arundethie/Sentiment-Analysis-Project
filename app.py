from flask import Flask, render_template, request,redirect
from prediction_pipeline import preprocessing,vectorizer,get_prediction

app = Flask(__name__)

data = dict()
reviews = []
positive_r = 0
negative_r = 0
@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive_r
    data['negative'] = negative_r
    return render_template('index.html',data=data)

@app.route("/", methods=['POST'])
def my_post():
    text = request.form['text']
    preprocessed_text = preprocessing(text)
    vectorized_text = vectorizer(preprocessed_text)
    prediction = get_prediction(vectorized_text)

    if prediction == 'negative_r':
        global negative_r
        negative_r += 1
    else:
        global positive_r
        positive_r += 1

    reviews.insert(0,text)
    return redirect(request.url)


if __name__ == "__main__":
    app.run()