# Copyright 2023 <Votre nom et code permanent>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import re, random
from flask import Flask, render_template, request, redirect, g, flash, url_for
from .database import Database


app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route('/')
def index():
    db = get_db()
    animaux = db.get_animaux()
    animaux_random = random.sample(animaux, k=5)
    return render_template('index.html', animaux_random=animaux_random)


@app.route('/animal/<int:animal_id>')
def animal(animal_id):
    db = get_db()
    animal = db.get_animal(animal_id)
    return render_template('animal.html', animal=animal)


@app.route('/formulaire')
def form():
    return render_template('form.html')


@app.route('/succes', methods=['POST'])  # TODO a changer par le nom de la page#
def ajout_animal():
    nom = request.form.get('nom')
    espece = request.form.get('espece')
    race = request.form.get('race')
    age = request.form.get('age', type=int)
    description = request.form.get('description')
    courriel = request.form.get('courriel')
    adresse = request.form.get('adresse')
    ville = request.form.get('ville')
    cp = request.form.get('cp')

    if validation_form(nom, espece, race, age, description, courriel, adresse, ville, cp):
        db = get_db()
        new_animal = db.add_animal(nom, espece, race, age, description, courriel, adresse, ville, cp)
        animal = db.get_animal(new_animal)
        return render_template('animal.html', animal=animal)
    else:
        return redirect(url_for('form'))

#TODO
@app.route('/recherche', methods=['GET', 'POST'])
def recherche():
    if request.method == 'POST':
        return render_template('result.html')
    return render_template('recherche.html')


def validation_form(nom, espece, race, age, description, courriel, adresse, ville, cp):
    if not all([nom, espece, race, age, description, courriel, adresse, ville, cp]):
        return redirect(url_for('form'))

    if ',' in nom or ',' in espece or ',' in race or ',' in description or ',' in courriel or ',' in adresse or ',' in ville or ',' in cp:
        return redirect(url_for('form'))

    if not (3 <= len(nom) <= 20):
        return redirect(url_for('form'))

    if not (0 <= age <= 30):
        flash('Age must be between 0 and 30.')
        return redirect(url_for('form'))

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(email_regex, courriel):
        return redirect(url_for('form'))

    cp_regex = r'[A-Z][0-9][A-Z] [0-9][A-Z][0-9]'
    if not re.fullmatch(cp_regex, cp):
        return redirect(url_for('form'))
