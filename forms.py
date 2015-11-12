from flask.ext.wtf import Form
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, RadioField, BooleanField, \
        SubmitField, IntegerField, FormField, StringField, PasswordField, \
        SelectField
from wtforms import validators, ValidationError
from wtforms.validators import Required, EqualTo, DataRequired
from wtforms.widgets import Input

class StudentFormClassification(Form):
    sex = SelectField('Sex', choices=[('F', 'Female'), ('M', 'Male')])
    age = SelectField('Age', choices=[('15', '15'), ('16', '16'),
                                ('17', '17'), ('18', '18'),
                                ('19', '19'), ('20', '20'),
                                ('21', '21'), ('22', '22')], option_widget=None)
    address = SelectField('Address', choices=[('U', 'Urban'), ('R', 'Rural')])
    famsize = SelectField('Family size', choices=[('LE3', 'Less or equal to 3'), ('R', 'Greater than 3')])
    Pstatus = SelectField('Parent\'s cohabitation status', choices=[('T', 'Living together'), ('A', 'Appart')])
    Medu = SelectField('Mother\'s education', choices=[('0', 'None'),
                                                        ('1', 'Primary education (4th grade)'),
                                                        ('2', 'Primary education (5th to 9th grade)'),
                                                        ('3', 'Secondary education'),
                                                        ('4', 'Higher education')])
    Fedu = SelectField('Father\'s education', choices=[('0', 'None'),
                                                        ('1', 'Primary education (4th grade)'),
                                                        ('2', 'Primary education (5th to 9th grade)'),
                                                        ('3', 'Secondary education'),
                                                        ('4', 'Higher education')])
    Mjob = SelectField('Mother\'s job', choices=[('teacher', 'Teacher'),
                                                ('health', 'Care related'),
                                                ('civil', 'Services (e.g. administrative or police)'),
                                                ('at_home', 'At home'),
                                                ('other', 'Other')])
    Fjob = SelectField('Father\'s job', choices=[('teacher', 'Teacher'),
                                                ('health', 'Care related'),
                                                ('civil', 'Services (e.g. administrative or police)'),
                                                ('at_home', 'At home'),
                                                ('other', 'Other')])
    reason = SelectField('Reason to choose this school', choices=[('home', 'Close to home'),
                                                                    ('reputation', 'Reputation of School'),
                                                                    ('course', 'Course preference'),
                                                                    ('other', 'Other')])
    guardian = SelectField('Guardian', choices=[('mother', 'Mother'),
                                                ('father', 'Father'),
                                                ('other', 'Other')])
    traveltime = SelectField('Home to school travel time', choices=[('1', '<15 min.'),
                                                                    ('2', '15 to 30 min.'),
                                                                    ('3', '30 min. to 1 hour'),
                                                                    ('4', '>1 hour')])
    studytime = SelectField('Weekly study time', choices=[('1', '<2 hours'),
                                                            ('2', '2 to 5 hours'),
                                                            ('3', '5 to 10 hours'),
                                                            ('4', '>10 hours')])
    failures = SelectField('Number of past class failures', choices=[('0', '0'),
                                                                    ('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '>=3')])
    schoolsup = SelectField('Extra educational support', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    famsup = SelectField('Family educational support', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    paid = SelectField('Extra paid classes within the course subject', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    activities = SelectField('Extra-curricular activities', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    nursery = SelectField('Attended nursery school', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    higher = SelectField('Wants to take higher education', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    internet = SelectField('Internet access at home', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    romantic = SelectField('With a romantic relationship', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    famrel = SelectField('Quality of family relationships (1: bad - 5: excellent)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    freetime = SelectField('Free time after school (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    goout = SelectField('Going out with friends (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    Dalc = SelectField('Workday alcohol consumption (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    Walc = SelectField('Weekend alcohol consumption (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    health = SelectField('Current health status (1: very bad - 5: very good)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    absences = IntegerField('Number of school absences', [validators.NumberRange(min=0, max=93)])
    G1 = IntegerField('First period grade', [validators.NumberRange(min=0, max=20)])
    submit = SubmitField('Submit')

class StudentFormRegression(Form):
    sex = SelectField('Sex', choices=[('F', 'Female'), ('M', 'Male')])
    age = SelectField('Age', choices=[('15', '15'), ('16', '16'),
                                ('17', '17'), ('18', '18'),
                                ('19', '19'), ('20', '20'),
                                ('21', '21'), ('22', '22')], option_widget=None)
    address = SelectField('Address', choices=[('U', 'Urban'), ('R', 'Rural')])
    famsize = SelectField('Family size', choices=[('LE3', 'Less or equal to 3'), ('R', 'Greater than 3')])
    Pstatus = SelectField('Parent\'s cohabitation status', choices=[('T', 'Living together'), ('A', 'Appart')])
    Medu = SelectField('Mother\'s education', choices=[('0', 'None'),
                                                        ('1', 'Primary education (4th grade)'),
                                                        ('2', 'Primary education (5th to 9th grade)'),
                                                        ('3', 'Secondary education'),
                                                        ('4', 'Higher education')])
    Fedu = SelectField('Father\'s education', choices=[('0', 'None'),
                                                        ('1', 'Primary education (4th grade)'),
                                                        ('2', 'Primary education (5th to 9th grade)'),
                                                        ('3', 'Secondary education'),
                                                        ('4', 'Higher education')])
    Mjob = SelectField('Mother\'s job', choices=[('teacher', 'Teacher'),
                                                ('health', 'Care related'),
                                                ('civil', 'Services (e.g. administrative or police)'),
                                                ('at_home', 'At home'),
                                                ('other', 'Other')])
    Fjob = SelectField('Father\'s job', choices=[('teacher', 'Teacher'),
                                                ('health', 'Care related'),
                                                ('civil', 'Services (e.g. administrative or police)'),
                                                ('at_home', 'At home'),
                                                ('other', 'Other')])
    reason = SelectField('Reason to choose this school', choices=[('home', 'Close to home'),
                                                                    ('reputation', 'Reputation of School'),
                                                                    ('course', 'Course preference'),
                                                                    ('other', 'Other')])
    guardian = SelectField('Guardian', choices=[('mother', 'Mother'),
                                                ('father', 'Father'),
                                                ('other', 'Other')])
    traveltime = SelectField('Home to school travel time', choices=[('1', '<15 min.'),
                                                                    ('2', '15 to 30 min.'),
                                                                    ('3', '30 min. to 1 hour'),
                                                                    ('4', '>1 hour')])
    studytime = SelectField('Weekly study time', choices=[('1', '<2 hours'),
                                                            ('2', '2 to 5 hours'),
                                                            ('3', '5 to 10 hours'),
                                                            ('4', '>10 hours')])
    failures = SelectField('Number of past class failures', choices=[('0', '0'),
                                                                    ('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '>=3'),])
    schoolsup = SelectField('Extra educational support', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    famsup = SelectField('Family educational support', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    paid = SelectField('Extra paid classes within the course subject', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    activities = SelectField('Extra-curricular activities', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    nursery = SelectField('Attended nursery school', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    higher = SelectField('Wants to take higher education', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    internet = SelectField('Internet access at home', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    romantic = SelectField('With a romantic relationship', choices=[('yes', 'Yes'),
                                                                    ('no', 'No')])
    famrel = SelectField('Quality of family relationships (1: bad - 5: excellent)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    freetime = SelectField('Free time after school (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    goout = SelectField('Going out with friends (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    Dalc = SelectField('Workday alcohol consumption (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    Walc = SelectField('Weekend alcohol consumption (1: low - 5: high)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    health = SelectField('Current health status (1: very bad - 5: very good)', choices=[('1', '1'),
                                                                    ('2', '2'),
                                                                    ('3', '3'),
                                                                    ('4', '4'),
                                                                    ('5', '5')])
    absences = IntegerField('Number of school absences', [validators.NumberRange(min=0, max=93)])
    G1 = IntegerField('First period grade', [validators.NumberRange(min=0, max=20)])
    G2 = IntegerField('Second period grade', [validators.NumberRange(min=0, max=20)])
    submit = SubmitField('Submit')
