
import requests
from bs4 import BeautifulSoup 
from tkinter import *
import pandas as pd 
import tkinter as tk
from tkinter import filedialog 

janela = Tk()
janela.title("Extrair textos de categoria")
janela.geometry("850x500")    

def __init__():
    pass

#importar csv
#Percorrer o diretorio
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
    title = "Select a File", 
    filetypes = (("csv files", 
        "*.csv*"), 
        ("all files", 
        "*.*"))) 
    label_file_explorer.configure(text="Arquivo escolhido: "+filename) 
    
    #abre o arquivo e armazena em data
    with open(filename, 'r', encoding='utf-8') as f:
       text_URLs.insert("1.0", f.readlines())
       print(f.readlines())
    
def create_list_urls():
    tag5 = (text_URLs.get("1.0",'end-1c'))
    valor_tag5 = tag5
    list1 = []
    print(list1)
    list1.append(valor_tag5)
    return list1

def road_path():
    tag1 = str(first_tag_up.get())
    tag2 = str(Second_tag_up.get())
    tag3 = str(first_tag_down.get())
    tag4 = str(Second_tag_down.get())
    valor_tag1 = tag1
    valor_tag2 = tag2
    valor_tag3 = tag3
    valor_tag4 = tag4
    list2 = []
    list2.append(valor_tag1)
    list2.append(valor_tag2)
    list2.append(valor_tag3)
    list2.append(valor_tag4)
    return list2
def get_text_category(list1, list2):
    # print("teste")
    # print(list1)
    URL = list1[0]
    tag_pai_cima = list2[0]
    tag_filha_cima = list2[1]
    tag_pai_baixo = list2[2]
    tag_filha_baixo = list2[3]
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    for URLs in URL:
        site = requests.get(URLs, headers=headers) #buscar e guardar minhas informações
        try:
            soup = BeautifulSoup(site.content, 'html.parser') #guardar todo o meu html da página
            texto_acima = soup.find(tag_pai_cima, class_ = tag_filha_cima).get_text()#utiliza claas com _ para palavra reservada.
            #print(texto_acima)
            texto_abaixo = soup.find(tag_pai_baixo, class_ = tag_filha_baixo).get_text()#utiliza claas com _ para palavra reservada.
            #print(texto_abaixo)

            #criando dicionario para receber os valores.
            dic_URLs = {'URL':[], 'texto acima':[], 'texto abaixo':[]}
            dic_URLs['URL'].append(URL)
            dic_URLs['texto acima'].append(texto_acima)
            dic_URLs['texto abaixo'].append(texto_abaixo)
        except:
            print('erro')
            pass    

    #gerando planilha csv
    df = pd.DataFrame(dic_URLs)
    df.to_csv(r'C:\Users\liveSEO\Desktop\LiveSEO\Scripts_python\interface\Texto_Xpath.csv', encoding='utf-8')

def send_data():
    list1 = create_list_urls()
    list2 = road_path()
    # print(list1)
    get_text_category(list1, list2)

#campos para preenchimento
first_tag_up_text = Label(janela, text='Informe a tag do texto acima: ')
first_tag_up_text.grid(column=0, row=0, padx=10, pady=10)
first_tag_up = Entry(janela, width=100)
first_tag_up.grid(column=1, row=0, padx=10, pady=10)

Second_tag_up_text = Label(janela, text='Informe a classe do texto acima: ')
Second_tag_up_text.grid(column=0, row=1, padx=10, pady=10)
Second_tag_up = Entry(janela, width=100)
Second_tag_up.grid(column=1, row=1, padx=5, pady=10)

first_tag_down_text = Label(janela, text='Informe a tag do texto abaixo: ')
first_tag_down_text.grid(column=0, row=2, padx=10, pady=10)
first_tag_down = Entry(janela, width=100)
first_tag_down.grid(column=1, row=2, padx=10, pady=10)

Second_tag_down_text = Label(janela, text='Informe a classe do texto abaixo: ')
Second_tag_down_text.grid(column=0, row=3, padx=10, pady=10)
Second_tag_down = Entry(janela, width=100)
Second_tag_down.grid(column=1, row=3, padx=10, pady=10)

# Text editor
text_URLs = tk.Text(janela, height=12)
text_URLs.grid(column=1, row=8, sticky='nsew')
#botões do browserFile
label_file_explorer = Label(janela,  
    text = "Faça o upload de um arquivo", 
    width = 100, height = 4,  
    fg = "blue") 
button_explore = Button(janela,  
    text = "Procurando Arquivos", 
    command = browseFiles)    
#Fim botõesbrowsefile

#Mensagem de validação dos campos (Não esta sendo utilizado no momento..)
erro = Label(bg='#191970', fg='white', font=('Arial', '11'), text='preencha todos os campos!')
erro.place(x=10, y=400)

# Botão de confirmação 
btn_enviar = Button(janela, text="Enviar",command=send_data)
btn_enviar.place(x=15, y=450)
button_exit = Button(janela,  
    text = "Exit", 
    command = exit)  
label_file_explorer.grid(column = 1, row = 6) 
button_explore.grid(column = 1, row = 7) 
button_exit.grid(column = 1,row = 7)
button_exit.place(x=80, y= 450)

janela.mainloop()