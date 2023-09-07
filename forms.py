from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, InputRequired

class JournalForm(FlaskForm):
    """
    Form for creating a new journal entry.
    """
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=100)])
    body = StringField("Body", validators=[DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField("Submit")

class MoodForm(FlaskForm):
    """
    Form for assessing mood level and emotions to determine best treatments
    """
    mood = RadioField("How are you feeling?", choices=[("Awful", "Awful"), ("Not Good", "Not Good"), ("Okay", "Okay"), ("Good", "Good"), ("Amazing", "Amazing"),], validators=[InputRequired()])
    submit = SubmitField("Submit")

class NegativeEmotions(FlaskForm):
    negative_emotions = RadioField("What exactly are you feeling?", choices=[("Angry", "Angry"), ("Sad", "Sad"), ("Anxious", "Anxious"), ("Depressed", "Depressed"), ("Worried", "Worried"), ("Stress", "Stressed")], validators=[InputRequired()])
    submit = SubmitField("Submit")

class PositiveEmotions(FlaskForm):
    positive_emotions = RadioField("Positive Emotions", choices=[("Happy"), ("Content"), ("Relaxed"), ("Energetic"), ("Excited")])
    submit = SubmitField("Submit")

    
    
    
   
    negative_manifestations = RadioField("Manifestations", choices=[("Irritation"), ("Rumination"), ("Restlessness"), ("Tension"), ("Agitation"), ("Shortness of Breath"), ("Nausea")])
    rumination_exercises = RadioField("Rumination Exercises", choices=[("Leaves on a Stream Meditation"), ("Body Scan Meditation"), ("Journaling"), ("Walk")])
    submit = SubmitField("Submit")
    
    