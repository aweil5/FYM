import os
from dotenv import load_dotenv
import openai
from flask import Flask, render_template

load_dotenv()

API_KEY = os.getenv("API_KEY")
ORG_KEY = os.getenv("ORG_KEY")


openai.organization = ORG_KEY
openai.api_key = API_KEY

# DOING FULL BACKEND LATER, CREATE MORE INTRICATE PROMPT
def singleRecipe():
    protein = "50"
    carb = "60"
    fat = "20"
    calories = "600"

    otherInfo = "I want vegetables and I want rice in the meal"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Give me a recipe that has around " + protein + " grams of protein, " + carb + " grams of carbohydrate, " +
                fat + " grams of fat and has " + calories + " calories. Along with that include this information: " + otherInfo}
        ]
    )

    print(completion.choices[0].message)
    return 0

# added in the static_folder to allow for the css to be used
app = Flask(__name__, static_folder='templates/assets')

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
