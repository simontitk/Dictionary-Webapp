from flask import Flask, request, session, url_for, redirect, render_template
from queries import Queries


Queries.setup_db()
app = Flask(__name__)
app.config["SECRET_KEY"] = "super_secret_key"


@app.route("/") 
def home():
    return redirect(url_for("manage"))

@app.route("/manage")
def manage():
    words = Queries.get_all_words()
    categories = Queries.get_all_categories()
    if "selected_categories" not in session:
        session["selected_categories"] = []
    if not session["selected_categories"]:
        session["selected_categories"] = Queries.get_all_categories()
    return render_template("manage.html", site_name="Manage", categories=categories, words=words)


@app.route("/add_word", methods=["POST"])
def add_word():
    f = request.form
    word = (f["hungarian"], f["english"], f["danish"], f["category"])
    if all(word):
        Queries.add_word(word)
    return redirect(url_for("manage"))


@app.route("/delete_word", methods=["POST"])
def delete_word():
    id = request.form["id"]
    if id:
        Queries.delete_word(id)
    return redirect(url_for("manage"))


@app.route("/edit_word")
def edit_word():
    return redirect(url_for("manage"))


@app.route("/filter_words", methods=["POST"])
def filter_words():
    selected_categories = request.form.getlist("categories")
    session["selected_categories"] = selected_categories
    return redirect(url_for("manage"))


@app.route("/add_category", methods=["POST"])
def add_category():
    category = request.form["category"].strip().lower()
    if category:
        Queries.add_category(category)
        session["selected_categories"].append(category)
        session.modified = True
    return redirect(url_for("manage"))


@app.route("/delete_category", methods=["POST"])
def delete_category():
    category = request.form["categories"]
    Queries.delete_category(category)
    if category in session["selected_categories"]:
        session["selected_categories"].remove(category)
        session.modified = True
    print("SELECTED CATS", session["selected_categories"])

    return redirect(url_for("manage"))


if __name__ == "__main__":
    app.run(debug=True)