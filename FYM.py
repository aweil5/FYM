import openai
from flask import Flask, render_template

API_KEY = "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"

openai.organization = "org-RjKf2up3fnL1E2nOJzXhPgRZ"
openai.api_key = API_KEY










def singleRecipe():
    protein = "50"
    carb = "60"
    fat = "20"
    calories = "600"

    otherInfo = "I want vegetables and I want rice in the meal"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Give me a recipe that has around " + protein + " grams of protein, " + carb + " grams of carbohydrate, " + fat + " grams of fat and has " + calories + " calories. Along with that include this information: " + otherInfo}
    ]
    )

    print(completion.choices[0].message)
    return 0

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__== "__main__":
    app.run()




