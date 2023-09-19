import os
from dotenv import load_dotenv
import openai
from flask import Flask, render_template, request


# added in the static_folder to allow for the css to be used
app = Flask(__name__, static_folder='templates/assets')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/recipeGeneration', methods=['POST'])
def recipeGeneration():
    protein = request.form.get('protein')
    carb = request.form.get('carb')
    fat = request.form.get('fat')
    calorie = request.form.get('calorie')
    otherInfo = request.form.get('otherInfo')

    prompt = ". In the response begin with the recipe name, the macro nutrient count in the meal and then the ingredients to make it followed by the steps to make the recipe."

    prompt = prompt + """ Create a RFC8259 compliant JSON response  following this format without deviation:
    [{
        "RecipeName": "The name of the recipe",
        "Macronutrients": "The macronutrients of this recipe",
        "Ingredients":"The ingredients of the recipe",
        "Steps": "The Steps to make the recipe

    }]"""

    if(len(protein) != 0):
        prompt = "I want there to be " + protein  + " grams of protein." + prompt
    if(len(carb) != 0):
        prompt = "I want there to be " + carb  + " grams of carbohydrates." + prompt
    if(len(fat) != 0):
        prompt = "I want there to be " + fat  + " grams of fats." + prompt
    if(len(calorie) != 0):
        prompt = "I want there to be " + calorie  + " calories." + prompt
    if(len(otherInfo) != 0):
        prompt = "Along with this incorporate the following information for the meal plan: " + otherInfo + prompt

    prompt = "Please respond with a recipe satsifies the following information and include  the macro nutrients for the recipe, its required ingredients and the steps to make them. " + prompt
    
    load_dotenv()

    API_KEY = os.getenv("OPENAI_API_KEY")
    ORG_KEY = os.getenv("ORG_KEY")

    openai.organization = ORG_KEY
    openai.api_key = API_KEY
    print("Running AI")
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )
    print("Done with AI call")
    
    recipe = completion.choices[0].message.content
    print(recipe)
    return str(recipe)



@app.route('/recipeGenerationFullDay', methods=['POST'])
def recipeGenerationFullDay():
    protein = request.form.get('protein')
    carb = request.form.get('carb')
    fat = request.form.get('fat')
    calorie = request.form.get('calorie')
    otherInfo = request.form.get('otherInfo')

    prompt = ". In the response begin with how many meals there are, the macro nutrient count in each meal and then list each recipe in order, first being the recipe name, then the macronutrients, then the ingredients, then the steps to make it."

    if(len(protein) != 0):
        prompt = "I want there to be " + protein  + " grams of protein." + prompt
    if(len(carb) != 0):
        prompt = "I want there to be " + carb  + " grams of carbohydrates." + prompt
    if(len(fat) != 0):
        prompt = "I want there to be " + fat  + " grams of fats." + prompt
    if(len(calorie) != 0):
        prompt = "I want there to be " + calorie  + " calories." + prompt
    if(len(otherInfo) != 0):
        prompt = "Along with this incorporate the following information for the meal plan: " + otherInfo + prompt

    prompt = "Please respond with a meal plan for a day of eating that satsifies the following information and include each recipe for the day, the macro nutrients for each recipe, their required ingredients and the steps to make them. " + prompt
    

    load_dotenv()

    API_KEY = os.getenv("OPENAI_API_KEY")
    ORG_KEY = os.getenv("ORG_KEY")

    openai.organization = ORG_KEY
    openai.api_key = API_KEY

    prompt = "For the response I would like a full day of eating that satisfies the given information. In the full day I want there to be " + protein + " grams of protein, " + carb + " grams of carbs, " + fat + " grams of fat. At around a total of " + calorie + " calories for the day. Along with this incorporate the following information for the meal plan: " + otherInfo + ". In the response begin with how many meals there are, the macro nutrient count in each meal and then the keep each recipe organized. "
    print("Running AI")
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt}
        ]
    )
    print("Done with AI call")
    
    recipe = completion.choices[0].message.content
    print(recipe)
    return str(recipe)

if __name__ == "__main__":
    app.run()



