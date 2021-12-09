from flask import Flask, render_template, request
from flask.views import MethodView
from calories import Calories
from wtforms import Form, StringField, SubmitField

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPages(MethodView):
    def get(self):
        calories = CaloriesForm()
        return render_template('calories_form_page.html', calories=calories)

    def post(self):
        calories = CaloriesForm()
        return render_template('calories_form_page.html', calories=calories)


class CaloriesForm(Form):
    weight = StringField("weight:", default="70")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/caloriesForm',
                 view_func=CaloriesFormPages.as_view('calories_form'))

app.run(debug=True)
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
