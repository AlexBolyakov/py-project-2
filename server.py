from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary
app = Flask(__name__)

cupcake = find_cupcake("cupcakes.csv", "Oreo")

# Decorator
@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("sample.csv"))

@app.route("/individual-cupcake/<name>")
def view_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    # print(cupcake)
    if cupcake:
        
        # print("Found Oreo cupcake", cupcake)
        return render_template("individual-cupcake.html", cupcake=cupcake)
    else:
        return "Cupcake is not in the list!"


@app.route("/all_cupcakes")
def all_cupcake():
    return render_template("all-cupcakes.html")


@app.route("/active_order")
def order_cupcake():
    return render_template("active-order.html")

if __name__ == "__main__":
    app.debug = "development"
    app.run(debug = True, port = 8000, host = "localhost")


