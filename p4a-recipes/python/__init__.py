from pythonforandroid.recipe import PythonRecipe


class Python3Recipe(PythonRecipe):
    patches = ['disable-grp.patch']


recipe = Python3Recipe()
