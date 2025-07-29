from flask import Flask, render_template, request, session, flash, redirect
from core.core import compute_golden_rule

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        text: str = request.form.get("input_text", "Hello Baba")
        size: float = float(request.form.get("fsize", 60))
        font_name: str = request.form.get("fname", "sans-serif")
    else:
        text = "Hello Baba"
        size = 60
        font_name = "sans-serif"

    sizes_list: list[float] = compute_golden_rule(size)
    
    return render_template("index.html", text=text, sizes_list=sizes_list, font_name=font_name, size=int(size))


if __name__ == '__main__':
    app.run(debug=True)
