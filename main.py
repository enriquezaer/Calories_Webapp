from flask import Flask, render_template, request
from flask.views import MethodView
from calories import Calories
from wtforms import Form, StringField, SubmitField
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    # Clase que crea la pagina inicia HTML inicial
    def get(self):
        return render_template('index.html')


class CaloriesFormPages(MethodView):
    # Pagina que captura los datos, calcula y muestra los resultados

    def get(self):
        # Metodo Get
        calories = CaloriesForm()
        return render_template('calories_form_page.html',
                               calories=calories)

    def post(self):
        # Metodo POST
        calories = CaloriesForm(request.form)
        temperature_ = Temperature(country=str(calories.country.data),
                                   location=str(calories.city.data))

        calories_ = Calories(weight=float(calories.weight.data),
                             height=float(calories.height.data),
                             age=float(calories.age.data),
                             temperature=temperature_)

        val_result = calories_.calculate()

        result = True

        return render_template('calories_form_page.html',
                               calories=calories,
                               result=result,
                               val=str(val_result))


class CaloriesForm(Form):
    weight = StringField("weight:", default="70")
    height = StringField("Height:", default="17")
    age = StringField("age:", default="32")

    city = StringField("City:", default="tegucigalpa")
    country = StringField("Country", default="honduras")

    button_calc = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/caloriesForm',
                 view_func=CaloriesFormPages.as_view('calories_form'))

app.run(debug=True)
