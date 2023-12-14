import google.generativeai as palm
from flask import Flask, render_template, request

app = Flask(__name__)

palm.configure(api_key="AIzaSyChiF9rWXIZ4lLd8kzcuWOdQpx52MTjsu0")
models = [model for model in palm.list_models()]

model_id = models[1]


@app.route("/")
def home():
    return render_template("AI.html")


@app.route("/submit", methods=["POST"])
def submit():
    prompt = request.form["text"]

    if prompt == "":
        return render_template("AI.html", output="Please give some input    ")

    completion = palm.generate_text(
        model=model_id,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )

    result = completion.result

    return render_template("AI.html", output=result)


if __name__ == "__main__":
    app.run(debug=True)
