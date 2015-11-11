# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask
from flask import render_template, redirect, url_for, session
from forms import StudentFormClassification, StudentFormRegression
from flask_material import Material
import numpy as np

import sklearn
from sklearn.externals import joblib


log_reg = None
rf_regressor = None
vectorizer = None
try:
    rf_regressor = joblib.load("serialized/regressor/rfr.pkl")
    vectorizer = joblib.load("serialized/extras/vect.pkl")
    log_reg = joblib.load("serialized/classifier/lr.pkl")
    print "using trained classifier"
except Exception as e:
    print repr(e)

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Material(app)

def clean_data(info_student, second_period=False):
    """ Receives a dictionary containing all of the features with the values.
    Returns a vector ready to classify.
    """
    categorical_columns = ['address', 'schoolsup', 'guardian', 'famsize',
                           'Fjob', 'Pstatus', 'sex', 'reason', 'internet',
                           'paid', 'higher', 'famsup', 'Mjob', 'romantic',
                           'nursery', 'activities']
    categorical_dict = {k : info_student[k] for k in categorical_columns} # ready for vectorizer
    if second_period:
        numerical_columns = [k for k in info_student.keys() if k not in categorical_columns]
    else:
        numerical_columns = [k for k in info_student.keys() if k not in categorical_columns and k != "G2"]
    numerical_columns.sort()
    numerical_features = np.array([info_student[k] for k in numerical_columns]).astype('float64') # ready for scaler

    categorical_vector = vectorizer.transform(categorical_dict)
    numerical_vector = numerical_features.reshape((1, len(numerical_features)))
    return np.hstack((numerical_vector, categorical_vector))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student_classification', methods=['GET', 'POST'])
def student_classification():
    form = StudentFormClassification()
    if form.validate_on_submit():
        student_profile = {}
        for field in form:
            if field.type == 'SelectField' or field.type == 'IntegerField':
                k = field.name
                val = None
                try:
                    val = int(field.data)
                except ValueError:
                    val = field.data
                student_profile[k] = val
        vector_student = clean_data(student_profile)
        result = log_reg.predict(vector_student)
        probability = log_reg.predict_proba(vector_student)
        session['result'] = result[0]
        session['probability'] = probability[0][result[0]]
        return redirect(url_for('result_classification'))
    return render_template('form.html', form=form)

@app.route('/student_regression', methods=['GET', 'POST'])
def student_regression():
    form = StudentFormRegression()
    if form.validate_on_submit():
        student_profile = {}
        for field in form:
            if field.type == 'SelectField' or field.type == 'IntegerField':
                k = field.name
                val = None
                try:
                    val = int(field.data)
                except ValueError:
                    val = field.data
                student_profile[k] = val
        vector_student = clean_data(student_profile, True)
        result = rf_regressor.predict(vector_student)
        session['result'] = result[0]
        return redirect(url_for('result_regression'))
    return render_template('form.html', form=form)

@app.route('/result_classification')
def result_classification():
    result = session['result']
    probability = "%.2f" % (session['probability'] * 100)
    return render_template('result_classification.html', result=result, probability=probability)

@app.route('/result_regression')
def result_regression():
    result = "%.2f" % session['result']
    return render_template('result_regression.html', result=result)

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix! Si No'

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
