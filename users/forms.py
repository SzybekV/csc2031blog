from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email, DataRequired, ValidationError, Regexp, Length, NoneOf
import re


def password_characters_regex():
    #Regex for at least one Lowercase, Uppercase, Digit, and none of <&%, in any order
    regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]|[\da-zA-Z]^[<&%]")
    return regex


class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Email(), Regexp(regex=r"^[<&%]")])
    password = PasswordField(validators=[DataRequired(), Regexp(regex=password_characters_regex()), Length(8, 15),
                                         NoneOf(['<', '&', '%'])])

    submit = SubmitField()
