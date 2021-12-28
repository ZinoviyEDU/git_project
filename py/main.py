from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.numeric import FloatField
from wtforms.validators import InputRequired
from wtforms.validators import NoneOf
from wtforms import TextAreaField
from wtforms import SelectField
from wtforms.validators import Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'


@app.route('/about.html')
def about():
   output = render_template('about.html')
   return output

class sign(FlaskForm):
   condition = TextAreaField('condition', validators=[InputRequired('Field must be required!')])
   signA = StringField('фенотип A_', validators=[InputRequired('Field must be required!')])
   signa = StringField('фенотип aа', validators=[InputRequired('Field must be required!')])
   signB = StringField('фенотип B_', validators=[InputRequired('Field must be required!')])
   signb = StringField('фенотип bb', validators=[InputRequired('Field must be required!')])

   signAB_data = FloatField('фенотип AB', validators=[InputRequired('Field must be required!'), NoneOf(values=[0])])
   signAb_data = FloatField('фенотип Ab', validators=[InputRequired('Field must be required!'), NoneOf(values=[0])])
   signaB_data = FloatField('фенотип aB', validators=[InputRequired('Field must be required!'), NoneOf(values=[0])])
   signab_data = FloatField('фенотип ab', validators=[InputRequired('Field must be required!'), NoneOf(values=[0])])
   genotype = SelectField('genotype', choices=[('cys', 'AB//ab'), ('trans', 'Ab//aB')])

@app.route('/main.html')
def main():
   output = render_template('main.html')
   return output

@app.route('/solution_of_exercise.html', methods = ['GET', 'POST'])
def solution_of_exercise():
   form = sign()
   output = render_template('solution_of_exercise.html', form=form)
   return output

@app.route('/solution.html', methods = ['GET', 'POST'])
def solution():

   form = sign()
   if form.validate_on_submit():
      return render_template('solution_of_exercise.html')
   return render_template('solution.html', form=form)


