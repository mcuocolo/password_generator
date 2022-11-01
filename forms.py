from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, NumberRange


# class FieldsRequiredForm(FlaskForm):
#     """Require radio fields to have content. This works around the bug that WTForms radio fields
#     don't honor the `DataRequired` or `InputRequired` validators."""
#     class Meta:
#         def render_field(self, field, render_kw):
#             if field.type == "_Option":
#                 render_kw.setdefault("required", True)
#             return super().render_field(field, render_kw)


## Create Form Here
class PswOptionsForm(FlaskForm):
    length = IntegerField("Password length", validators=[DataRequired(),
                                                         NumberRange(min=0, max=36)], default=12)

    allow_numbers = BooleanField("Allow numbers", default=True)
    allow_uppercase = BooleanField("Allow uppercase", default=True)
    allow_lowercase = BooleanField("Allow lowercase", default=True)
    allow_symbols = BooleanField("Allow symbols", default=True)
    allow_similar = BooleanField("Allow similar", default=True)
    allow_duplicates = BooleanField("Allow duplicates", default=True)
    submit = SubmitField("Generate password")
