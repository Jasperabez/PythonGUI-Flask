from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    allowed_audio = tuple('mp3'.split())
    recTitle = StringField('Title', validators=[DataRequired()])
    recLocation = StringField('Location', validators=[DataRequired()])
    recDate = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    recAudio = FileField('Recording', validators=[FileRequired(),FileAllowed(allowed_audio, 'MP3 only!')])
    submit = SubmitField('Create')