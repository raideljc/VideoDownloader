from pythonforandroid.recipes.python3 import Python3Recipe

class Python3CustomRecipe(Python3Recipe):
    version = "3.11.18"
    patches = ["disable-grp.patch"]

recipe = Python3CustomRecipe()
