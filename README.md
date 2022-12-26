#Exportador de textos via Path

## Layout
- Construtor utilizado: Biblioteca TKinter
- TKinter - ttk (Acesso a conjuntos de widgets tematicos)
- 
## Bibliotecas - backend
- requests (Para fazer as requisições http)
- bs4 - BeautifulSoup (Para organizar o código de retorno HTML)
- pandas (Para leitura dos arquivos csv)
- tkinter - filedialog (Para abertura e manipulação dos arquivos no ambiente windows)
- port csv (Para leitura dos arquivos csv)

## Como funciona?
Este script permite a exportação dos textos de uma categoria de qualquer loja por meio das tags HTML.
Grande parte das lojas de ecommerce que possuem páginas otimizadas para SEO e disponibilizam textos acima e abaixo do catalogo de produtos.
Os textos são fornecidos para que os mecanismos de pesquisa do Google os utilize como fator de ranqueamento para termos relacionados a categoria.

Ferramentas de Scraping como o próprio Screaming Frog oferecem esta funcionalidade. Portanto este modelo de raspagem é uma alternativa 
para profissionais que não dispões de tais ferramentas ou que querem entender um pouco mais sobre como é feita a captura de dados da web por meio do python.

Neste exemplo utilizo a biblioteca Tkinter para criar um visual amigável, onde me permite a criação de uma janela para inserir as informações de manipulação 
fora do código.

1. Ao executar o script abrirá esta janela:

![image](https://user-images.githubusercontent.com/59829877/209569399-16e9d699-af69-4bd7-998b-d7aa5e415186.png)

2. Antes de mais nada, precisamos escolher o site que queremos fazer a raspagem de dados.<br>
Pesquisando por Loja de informatica no Google peguei o primeiro resutado e acessei a categoria de Smartphones.<br>
Nesta categoria podemos perceber que existe texto acima do catalogo de produtos. Pressionando a tecla f12 do teclado abrirá o devtools, por aqui é possivel encontrar no código HTML a div (bloco) onde o texto está inserido.<br>

![image](https://user-images.githubusercontent.com/59829877/209568746-8ba439e9-5253-4162-9f0e-8254dc6b167c.png)

3. Vamos copiar a tag e a classe correspondente ao texto acima que inspecionamos no Devtools, neste caso a tag é 'DIV' e a classe correspondente ao texto é 'category-description'
 Obs: Você fará o mesmo processo para raspar o texto abaixo do catalogo. 
![image](https://user-images.githubusercontent.com/59829877/209569851-a3c0974a-e706-4276-8cf0-c5cbf8358f90.png)

4. Como pode notar na imagem abaixo, este site não possui texto abaixo, portanto posso inserir a mesma regra que fiz para o texto acima para não deixar campo vazio afim de evitar erro de execução do script.
![image](https://user-images.githubusercontent.com/59829877/209569796-37cd0cfb-f4ce-4c61-8d1f-3a7c69288496.png)

5. Como nosso objetivo é obter o texto de todas as categorias deste site, neste etapa iremos passar uma lista em formato CSV com o endereço de URL de todas as categorias deste site. 
<br><strong>Clique em "Procurar Arquivos" e selecione a lista de URLs. </strong>
![image](https://user-images.githubusercontent.com/59829877/209571636-2cd57878-179f-46b4-8321-3b9521a2461d.png)

5.1 Pode ser que você ainda não tenha uma lista com todas as categorias do site e não disponha de uma ferramenta capaz de entregar esta lista para você. 
Se este for o caso e não queira fazer isso de forma manual, criei um script que permite mapear toda a arvore de categorias do site [AQUI!](url).
Ao obter a lista de URLs faça o upload (Mantenha apenas os URLs e todos na mesma coluna como o exemplo abaixo:
![image](https://user-images.githubusercontent.com/59829877/209572763-e251bd67-23b4-48b9-a2bd-dbd6dc3ad08e.png)

6. Ao selecionar o arquivo é só cliclar em enviar.
![image](https://user-images.githubusercontent.com/59829877/209584129-af8f9bcd-d400-4517-989a-41748fa85f6f.png)
<br>Sugiro que ao iniciar o programa acompanhe toda a execução pelo terminal

7. Por fim temos aqui o retorno de todos os textos de categoria:
 ![image](https://user-images.githubusercontent.com/59829877/209584094-e82251ac-7dcc-423a-ac8e-97d509d2a3f0.png)
 
8. Ao finalizar o processo de raspagem é gerado automaticamente um arquivo csv com o nome texto_Xpath.csv
![image](https://user-images.githubusercontent.com/59829877/209573636-790aa170-177a-4f70-a6d5-d9927e798da3.png)

