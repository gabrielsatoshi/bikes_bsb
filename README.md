[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=3000&color=14F709&random=false&width=435&lines=Arquitetura+de+Software)](https://git.io/typing-svg)
<h1>API bikes bsb 🚲 </h1>
<div class="line">
<img src='https://img.shields.io/badge/python-green'> <img src='https://img.shields.io/badge/Markdown-yellow'> <img src='https://img.shields.io/badge/SqLite-red'> 
<img src='https://img.shields.io/badge/Flask-pink'>
</div>

<h1>Transferencia .csv para SQLite 📄</h1>

Esse projeto tem como finalidade alimentar uma API Python com dados fornecidos em uma base de dados .csv que será posteriormente convertida
em SQLite , onde será contruido endpoints GET e POST.
 
  
<h3>1° Primeiro passo</h3>

Primeiramente é necessário que os arquivos .csv sejam baixados em seu computador , para isso faça o download dos arquivos
no link abaixo.
<a href="https://salaonline.ceub.br/pluginfile.php/290814/mod_assign/introattachment/0/basebikes.zip?forcedownload=1">Clique aqui para baixar os Arquivos .csv</a>
 
<h3>2° Segundo passo</h3>

Após baixar os arquivos .csv é necessário que você realize uma transferência dos dados para um banco SQLite, a forma mais simples
é utilizar nosso script para a transferência dos dados contidos no repositório. Para baixar o script do repositório , você deve ter 
o git instalado em seu computador e caso não tenha <a href="https://git-scm.com/downloads">Clique aqui</a> para realizar a instalação.

<h3>3° Terceiro passo</h3>

Agora que você possui o Git instalado em seu computador , abra o programa Git Bash e digite o seguinte comando :<br>
`git clone https://github.com/gabrielsatoshi/bikes_bsb.git`<br>
Se você executou o código corretamente, agora você poderá visualizar uma pasta chamada bikes_bsb em seu computador e
essa pasta contém o script para realizar a transferência dos dados .csv para o banco de dados SQLite.

<h3>4° Quarto passo</h3>

Já temos o necessário para realizar a transferência , porém antes precisamos mover os arquivos .csv para dentro da pasta bikes_bsb,
assim que a movimentação for realizada, você já pode abrir o seu programa editor de código e começar a instalar as bibliotecas utilizadas
no projeto. <br><br>
`pip install csv`<br>
`pip install sqlite3`<br><br>
**OBS**:*Normalmente é utilizado um requirements.txt , mas estamos utilizando apenas duas bibliotecas*.<br>

<h3>5° Quinto passo</h3>

Agora que você possui todos os requisitos necessários para executar o código, basta clicar em run em seu editor de códigos,
se não ocorrer nenhuma exceção meus parabéns! você seguiu todos os passos corretamente. Você deve ter percebido que na pasta
bikes_bsb foi criado um arquivo chamado `banco_bikes`  esse é nosso banco de dados , acredite ou não todos os dados contidos nos
arquivos .csv estão agora dentro do banco de dados SQLite.


<h3>6° Sexto passo (Opcional)</h3>

Esse último passo é opcional , você pode seguir esse último passo para verificar se os dados realmente foram inseridos no banco de dados,
para isso você deve instalar a ferramenta Db Browser for SQLite , <a href="https://sqlitebrowser.org/dl/">Clique aqui</a> para baixar a ferramenta diretamente.
Esta ferramenta serve para você conseguir visualizar o seu banco de forma gráfica ou seja, será possível você visualizar suas tabelas e os dados contidos nela.
Se você já realizou o download da ferramenta, basta abrir o programa e arrastar o arquivo banco_bikes para dentro do programa.

<h1>Flask e SQLite 🤖</h1>
<h1>GET🎯</h1>

Se você clonou o repositório e realizou todos os passos acima , a pasta bikes_bsb deve permanecer dentro do seu computador , desta forma a utilidade real
da base de dados SQLite vem a tona, a base de dados banco_bikes tem a finalidade de fornecer dados para uma API Python , Nesta seção será ensinado passo a passo de 
como utilizar a rota GET nesta API desenvolvida em Flask.

<h3>1° Primeiro passo</h3>

Antes de tudo você deve abrir o arquivo onde contém a configuração dos endpoints e baixar as bibliotecas utilizadas no projeto.<br><br>
`pip install flask`<br><br>
**OBS**:*Lembre de instalar as bibliotecas .csv e sqlite3 mostradas na primeira seção*.<br>

<h3>2° Segundo passo</h3>

Você deve agora clicar no botão Run , se tudo der certo irá exibir algo como `http://127.0.0.1:5000`<br>
se isso aparecer deu tudo certo e você está conseguindo rodar a API em seu localhost corretamente.<br>
Você deve copiar o link que aparecer e colar em seu navegador , fazendo isto você deve ver uma espécie de<br>
painel semelhante a este:<br>

<img src="https://user-images.githubusercontent.com/112598996/283928219-642f54dd-1b0b-4701-9329-61b5e14669a7.png">

<h3>3° Terceiro passo</h3>

Agora temos acesso a um painel com links que criam as requisições na API, basta escolher um dos links que estão <br>
sendo exibidos no painel. Perceba que a rota está sendo exibida na primeira coluna da tabela , observando bem podemos ver<br>
que é possível consultar as tabelas do banco de dados , assim como os itens da tabela. Se você clicar no primeiro link, poderá<br>
presenciar algo semelhante a isto:<br>

<img src="https://user-images.githubusercontent.com/112598996/283929758-cc0722a0-0b97-4a66-9658-92fd3b7d23af.png">
<br>
Na imagem acima podemos ver que o retorno é toda a tabela df_stations , isso ocorre pois clicamos no primeiro link exibido<br>
Porém também é possível sermos mais especificos e consultar um id dentro da tabela df_stations, basta clicar no segundo link.<br><br>

<img src="https://user-images.githubusercontent.com/112598996/283931232-6b15b4d7-4b4d-49ce-ba16-0f42cc435b1a.png">
<br>
É possível notar que o ID da estação está sendo passado pela URL, se você olhar bem para a imagem vai perceber que o ID 4 <br>
está sendo retornado, mas se você alterar o número do ID na URL você irá receber a respectiva estação que está cadastrada com o número.<br>
Assim podemos concluir a rota GET , lembrando que esse método é válido tanto para a tabela df_stations quanto para a tabela df_rides.<br>
<br>
<h1>POST📬</h1>

O método POST é um pouco diferente do método GET, com esse novo método podemos inserir novos registros na tabela e depois utilizar o GET para
conferir se o novo registro realmente foi inserido na tabela, mas para isso precisamos da ajuda de um programa.

<h3>1° Primeiro passo</h3>

A rota POST está definida na tabela como "NECESSITA POSTMAN ", a razão para isso é que a requisição POST não pode ser passada pela URL como a
requisição GET, desta forma iremos utilizar o programa POSTMAN para nos auxiliar com a requisição POST. O programa em questão pode ser baixado
<a href="https://www.postman.com/downloads/">Clicando aqui.</a>

<h3>2° Segundo passo</h3>

<h1>Erros ou dúvidas❗</h1>

Caso ocorra algum erro você pode verificar:

1- Se os módulos que estão sendo utilizados no código foram instalados no seu computador.<br>
2- Se os arquivos df_stations.csv e df_rides.csv estão presentes na pasta do bikes_bsb.<br>
3- Se o seu computador possui versões Python 3.0.<br>
4- Se o seu visual studio possui uma extensão para interpretador Python.<br>
5- Se existe algum erro de sintaxe no código ou estão faltando partes.

Caso você tenha alguma dúvida você pode consultar:

1- Documentação do SQLITE : https://docs.python.org/pt-br/3.9/library/sqlite3.html<br>
2- Documentação do PYTHON : https://docs.python.org/pt-br/3/<br>
3- O criador do código : gabrieltechr@gmail.com <br>
4- ChatGPT: https://chat.openai.com/ <br>


<h1>Tutoriais💻</h1>

Vídeo mostrando todo o processo : https://youtu.be/XJCTpFG2WTg





