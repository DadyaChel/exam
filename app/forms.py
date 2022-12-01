from flask_wtf import FlaskForm
import wtforms as ws


class EmployeeForm(FlaskForm):
    fullname = ws.StringField('FIO', validators=[ws.validators.DataRequired()])
    phone = ws.StringField('Телефон')
    short_info = ws.TextAreaField('Краткая информация')
    experience = ws.IntegerField('Опыт работы в годах')
    preferred_position = ws.StringField('Желаемая должность')
    # user_id = ws.SelectField('User')

    def validate_fullname(self, field):
        names_split = field.data.split(' ')
        if len(names_split) == 1:
            raise ws.ValidationError('FIO не может состоять из одного слова')
        for name in names_split:
            if not name.isalpha():
                raise ws.ValidationError('в FIO не должно быть спец символов и чисел')


class UserForm(FlaskForm):
    username = ws.StringField('Имя пользователя', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=4, max=20)
    ])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=8, max=69)
    ])

