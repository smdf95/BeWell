from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectMultipleField
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
    choices=[("Awful", "Awful"), ("Not Good", "Not Good"), ("Okay", "Okay"), ("Good", "Good"), ("Amazing", "Amazing"),]
    mood = RadioField("How are you feeling?", choices=choices, validators=[DataRequired()])
    submit = SubmitField("Submit")

class Relief(FlaskForm):
    choices=[("Irritation", "Irritation"), ("Rumination", "Rumination"), ("Restlessness", "Restlessness"), ("Tension", "Tension"), ("Agitation", "Agitation"), ("Shortness of Breath", "Shortness of Breath"), ("Worry", "Worry"), ("Sadness", "Sadness")]
    relief = SelectMultipleField("Take a moment to observe what is going on inside your body and mind. What are you feeling right now?", choices=choices, validators=[DataRequired()])
    submit = SubmitField("Submit")

class GratitudeForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired(), Length(min=1, max=100)])
    gratitude = StringField("What are you grateful for?", validators=[DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField("Send")

    
    
    
   
rumination_exercises = RadioField("Rumination Exercises", choices=[("Leaves on a Stream Meditation"), ("Body Scan Meditation"), ("Journaling"), ("Walk")])
submit = SubmitField("Submit")
choices=[("Angry", "Angry"), ("Sad", "Sad"), ("Anxious", "Anxious"), ("Depressed", "Depressed"), ("Worried", "Worried"), ("Stressed", "Stressed")] 
    
    