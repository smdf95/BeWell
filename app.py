from flask import Flask, render_template, request, redirect, url_for, session
from forms import JournalForm, MoodForm, NegativeEmotions, PositiveEmotions
from datetime import date

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"



journal_entry = [
    {
        "id": 1,
        "title": "First Journal Entry",
        "body": "This is my first journal entry."
    },
    {
        "id": 2,
        "title": "Second Journal Entry",
        "body": "This is my second journal entry."
    },
    {
        "id": 3,
        "title": "Third Journal Entry",
        "body": "This is my third journal entry."
    }
]

mood_entries = [
    {

    }
]

@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    form = JournalForm()
    if form.validate_on_submit():
        journal_entry.append({"id": len(journal_entry) + 1, "title": form.title.data, "body": form.body.data})
        return redirect(url_for("index"))
    return render_template('index.html', journal_entry=journal_entry, form=form)


current_mood = {}

@app.route("/mood", methods=['GET', 'POST'])
def mood():

    form = MoodForm()




    if form.validate_on_submit():
        mood = form.mood.data
        current_mood = {"date": date.today(), "mood": mood}
        if mood == "Amazing" or mood == "Good":
            return redirect(url_for('positive_emotions'))
        else:
            return redirect(url_for('negative_emotions'))

        
    return render_template('mood.html', form=form)
        
# mood_entries.append({"date": date.today(), "mood": form.mood.data, "negative_emotions": form.negative_emotions.data, "positive_emotions": form.positive_emotions.data, "negative_manifestations": form.negative_manifestations.data})

@app.route("/negative_emotions", methods=['GET', 'POST'])
def negative_emotions():
    form = NegativeEmotions()

    negative_emotions = form.negative_emotions.data

    return render_template('negative_emotions.html', form=form)

@app.route("/positive_emotions", methods=['GET', 'POST'])
def positive_emotions():
    form = PositiveEmotions()

    positive_emotions = form.positive_emotions.data

    return render_template('positive_emotions.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

