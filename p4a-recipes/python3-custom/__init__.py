from pythonforandroid.recipe import PythonRecipe

class Python3CustomRecipe(PythonRecipe):
    version = "3.11.18"
    name = "python3-custom"
    patches = ["disable-grp.patch"]
    # ... otras propiedades necesarias ...

recipe = Python3CustomRecipe()


