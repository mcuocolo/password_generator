from flask import Flask, render_template, redirect, url_for
from forms import PswOptionsForm
from password import Password
from utils.export_psw import make_qr_code

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'SECRET_PROJECT'

# instantiate password object
psw = Password()


@app.route("/", methods=["GET", "POST"])
def index():
    psw_form = PswOptionsForm(csrf_enabled=True)
    if psw_form.validate_on_submit():
        generated_psw = "empty"
        psw.length = psw_form.length.data
        psw.allow_numbers = psw_form.allow_numbers.data
        psw.allow_lowercase = psw_form.allow_lowercase.data
        psw.allow_uppercase = psw_form.allow_uppercase.data
        psw.allow_symbols = psw_form.allow_symbols.data
        psw.allow_similar = psw_form.allow_similar.data
        psw.allow_duplicates = psw_form.allow_duplicates.data
        _, _, generated_psw = psw.generate_psw()
        make_qr_code(generated_psw)
        return redirect(url_for("result", generated_psw=generated_psw, _external=True))
    return render_template("index.html", psw_form=psw_form)

@app.route("/<generated_psw>")
def result(generated_psw):
    return render_template("result.html", generated_psw=generated_psw)

if __name__ == "__main__":
    app.run(debug=False)