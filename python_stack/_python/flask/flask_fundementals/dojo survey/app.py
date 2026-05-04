from  flask import Flask , render_template , redirect ,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def show():
    name_from_temp = request.form['name']
    location_from_temp = request.form['location']
    language_from_temp = request.form['language']
    comment_from_temp = request.form['comment']
    gender_from_temp = request.form.get('gender', 'Not specified')
    fav_sports_from_temp = request.form.getlist('fav_sport')
    return render_template("show.html",
                           name_on_template=name_from_temp,
                           language_on_template=language_from_temp,
                           location_on_template=location_from_temp,
                           comment_on_template=comment_from_temp,
                           gender_on_template=gender_from_temp,
                           fav_sport_on_template = fav_sports_from_temp
                           )

if __name__ == '__main__' :
    app.run(debug=True)
