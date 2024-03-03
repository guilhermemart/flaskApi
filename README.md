# flaskApi
Api Flask MySql para cadastro e manipulação de produtos.

Setup:
1. Clone o repositório  
2. Abra o terminal na pasta raiz do projeto clonado
3. Instale os requirements listados no requirements.txt ou todos de uma vez  
  ex: pip install -r requirements.txt
4. Na pasta raiz do repositorio, build a imagem do banco de dados MYSQL  
  ex(Windows): docker build -t flask_api_db .  
5. Rode o container com o comando abaixo, 3 produtos serão criados como exemplo  
  ex(Windows): docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=**RootPassword** -e MYSQL_DATABASE=FlaskApiDb -e MYSQL_USER=**MyUser** -e MYSQL_PASSWORD=**MainPassword** flask_api_db  
  substitua:  
    **RootPassword** pelo password root desejado  
    **MyUser** pelo usuario principal desejado   
    **MainPassword** pelo password desejado  
  Anote esses valores.  
6. No arquivo .env da raiz do projeto use os valores anotados para preencher os valores 
7. Rode o app  
  ex(Windows): python -m main  
8. O framework irá servir o app na url:  
  http://127.0.0.1:5000/  
OBS:: No Linux rode o container docker com sudo  
  
Utilização:  
1. O site apresenta 4 campos.  
-- Uma lista com todos os produtos do bd  
-- Um campo que permite criar um novo produto  
-- Um campo que permite editar um produto existente  
-- Um campo que permite deletar um produto existente
  
2. Para criar um produto  
-- Edite os campos nome, descrição e preço do novo produto  
-- Pressione o botão criar  
-- Atualize a pagina para ver o novo produto na lista  
  
3. Para editar um produto  
-- Edite o campo Id do produto a ser editado com um dos existentes na lista  
-- Edite os campos nome, descrição e preço que serão alterados  
-- Pressione o botão editar  
-- Atualize a pagina para ver as novas caracteristicas do produto  
  
4. Para deletar um produto  
-- Edite o campo Id do produto a ser deletado com o Id de um dos produtos da lista  
-- Pressione o botão excluir  
-- Atualize a pagina e o produto nao aparecerá mais na lista  