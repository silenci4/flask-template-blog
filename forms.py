from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class CreateNewUser(FlaskForm):
    email = StringField("Your E-mail address", validators=[DataRequired()])
    password = PasswordField("Your Password", validators=[DataRequired()])
    name = StringField("Your Name", validators=[DataRequired(), URL()])
    submit = SubmitField("Register")

class LoginUserForm(FlaskForm):
    email = StringField("Your E-mail address", validators=[DataRequired()])
    password = PasswordField("Your Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    comment = CKEditorField('Your Comment', validators=[DataRequired()])
    submit = SubmitField('Send')