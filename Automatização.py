# Nesse projeto eu fiz uma automação de tarefas, uma ferramenta flexivel e util para todos os tipos de trabalho.
# Nesse exemplo vamos utilizar o site da hashtag // https://dlp.hashtagtreinamentos.com/python/intensivao/login //
import pyautogui
import time
import pandas
pyautogui.PAUSE = 0.5

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'


# Abrir o Chrome
pyautogui.press("win")
pyautogui.write("Google")
pyautogui.press("enter")

# Entrar no site
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Fazer o login
pyautogui.click(x=989, y=360)
pyautogui.write("demarcialima@hotmail.com")
pyautogui.press("tab")
pyautogui.write("87712442e")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Ler arquivos e inserir os dados

tabela = pandas.read_csv("PYAUTOGUI/produtos.csv")
for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]

    pyautogui.click(x=939, y=255)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")


    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(50000)
