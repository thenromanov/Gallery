import os
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class PhotoForm(FlaskForm):
    file = FileField('Фото')
    submit = SubmitField('Отправить')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = 'static/img'


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    form = PhotoForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/success')
    return render_template('carousel.html', form=form, filenames=list(map(lambda x: '/static/img/' + x, os.listdir(os.getcwd() + '/static/img'))))


@app.route('/success')
def success():
    return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
