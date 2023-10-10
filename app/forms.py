from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectMultipleField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email



class NegativeForm(FlaskForm):
    """
    Follow up form for MoodForm to assess whether user would like relief or not
    """
    choices=[("Yes", "Yes"), ("No", "No")]
    neg_selection = RadioField("Would you like to find some relief?", choices=choices, validators=[DataRequired()])
    submit = SubmitField("Submit")

class PositiveForm(FlaskForm):
    """
    Follow up form for MoodForm to assess whether user would like to post in the gratitude journal or not
    """
    choices=[("Yes", "Yes"), ("No", "No")]
    pos_selection = RadioField("Would you like to post in the gratitude journal?", choices=choices, validators=[DataRequired()])
    submit = SubmitField("Submit")

class Relief(FlaskForm):
    
    """
    Form for selecting symptoms
    """

    choices=[("Irritation", "Irritation"), ("Rumination", "Rumination"), ("Restlessness", "Restlessness"), ("Tension", "Tension"), ("Agitation", "Agitation"), ("Shortness of Breath", "Shortness of Breath"), ("Worry", "Worry"), ("Sadness", "Sadness")]
    relief = SelectMultipleField("Take a moment to observe what is going on inside your body and mind. What are you feeling right now?", choices=choices, validators=[DataRequired()])
    submit = SubmitField("Submit")

class GratitudeForm(FlaskForm):
    """
    Form for posting in the Gratitude Journal
    """
    gratitude = StringField("What are you grateful for?", validators=[DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField("Send")

    
class LoginForm(FlaskForm):
    """
    Form for logging in
    """
    username = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class ForgotPasswordForm(FlaskForm):
    """
    Form for resetting password
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    """
    Form for resetting password
    """
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class RegistrationForm(FlaskForm):
    """
    Form for user registration
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
   
    
    