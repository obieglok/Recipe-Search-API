import requests

def search(ingredient):
    app_key = '2d18de37fa056f6c5a6e311033d2aacc'
    app_id = '058ce9ff'
    ingredient
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def start():
    ingredient = input('Please enter an ingredient: ')
    res = search(ingredient)
    count=1
    for result in res:
        recipe = result['recipe']
        print("Recipe :{}".format(count))
        count=count+1
        print(recipe['label'])
        print(recipe['url'])

    wantToSaveRecipe=input("Would you like to save a recipe to a file? y/n")
    if(wantToSaveRecipe=='y'):
        saveRecipe(res)
    # while(wantToSaveRecipe=='y'):
    #     saveRecipe(res)
    #     wantToSaveRecipe = input("Would you like to save another recipe to a file? y/n")




def  saveRecipe(res):
    with open("Recipe.txt", "r") as text_file:
        recipeFile = text_file.read()
    recipeToSave=int(input("Which recipe would you like to save? (Number please)"))
    with open("Recipe.txt", "w+") as text_file:
        recipeSaved=res[recipeToSave-1]
        recipe=recipeSaved['recipe']
        text_file.write(recipe["label"] + "\n")
        text_file.write(recipe["url"]+ "\n")
        # text_file.write(recipe["image"])
        ingredients=recipe["ingredientLines"]
        text_file.write("Ingrediants: " + "\n")
        for ing in ingredients:
             text_file.write(ing + "\n")
    print("Your recipe has been saved")

start()