from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired

status_list=[('Open','Open'),('Withdraw', 'Withdraw'),('Closed', 'Closed')]
devops_owner_list=[('Iron.Man','Iron.Man'),('Captain.American', 'Captain.American'),('Black.Widow', 'Black.Widow')]

class BlogPostForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    title = StringField('Request Title', validators=[DataRequired()])
    text = TextAreaField('Request Content', validators=[DataRequired()])
    status = SelectField('Status', choices=status_list, validators=[DataRequired()] )
    submit = SubmitField('Submit')

class BlogPostFormAdmin(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    title = StringField('Request Title', validators=[DataRequired()])
    text = TextAreaField('Request Content', validators=[DataRequired()])
    status = SelectField('Status', choices=status_list, validators=[DataRequired()] )
    devops_owner = SelectField('DevOps Owner', choices=devops_owner_list, validators=[DataRequired()] )
    effort_hour = IntegerField('DevOps Hour')
    submit = SubmitField('Submit')
