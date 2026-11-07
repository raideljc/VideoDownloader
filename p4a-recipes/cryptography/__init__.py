from pythonforandroid.recipes.cryptography import CryptographyRecipe

class CryptographyNoIsolationRecipe(CryptographyRecipe):
    # Forzar la versión que quieres usar
    version = "3.4.8"
    
    # Desactivar el aislamiento de build para que use el cffi de p4a
    def get_recipe_env(self, arch, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        env["PIP_NO_BUILD_ISOLATION"] = "1"
        return env

recipe = CryptographyNoIsolationRecipe()
