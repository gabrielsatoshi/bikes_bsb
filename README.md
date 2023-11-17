<h1>bikes bsb 🚲 </h1>



<h1>Transferencia .csv para SQLite</h1>
 
  
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





