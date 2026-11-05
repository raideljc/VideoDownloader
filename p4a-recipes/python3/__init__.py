from pythonforandroid.recipes.python3 import Python3Recipe as BasePython3Recipe


class Python3Recipe(BasePython3Recipe):
    # Hereda url, version, patches, depends, etc. de la receta oficial
    patches = BasePython3Recipe.patches + ['disable-grp.patch']


recipe = Python3Recipe()
