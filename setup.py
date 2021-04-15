from cx_Freeze import setup, Executable

options = {
  "include_files" : ["icon/"]
}

setup(
  name = "HVoca",
  version = "Beta1.1-1",
  description = "Logiciel d'apprentissage du vocabulaire à partir de liste créées par l'utilisateur.",
  author = "Adrien Herman",
  options = {"bdist_exe" : options},
  executables = [Executable("main.py", build="Win32GUI")]
)
