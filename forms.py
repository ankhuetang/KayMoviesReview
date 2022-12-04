from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email=StringField("Email", validators=[Email(message="Please enter a valid email")] )
    password= PasswordField("Password",validators=[DataRequired()])
    name=StringField("Name", validators=[DataRequired()])
    submit=SubmitField("Sign Me Up!")

class LoiginForm(FlaskForm):
    email=StringField("Email", validators=[Email(message="Please enter a valid email")] )
    password= PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Let Me In!")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")