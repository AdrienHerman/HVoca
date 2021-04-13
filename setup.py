from cx_Freeze import setup, Executable

platform = "Win32GUI"

options = {
  "include_files" : ["icon/"]
}

setup(
  base = platform,
  name = "HVoca",
  version = "Beta 1.1",
  description = "Logiciel d'apprentissage du vocabulaire à partir de liste créées par l'utilisateur.",
  author = "Adrien Herman",
  options = {"build_exe" : options},
  executables = [Executable("main.py")]
)