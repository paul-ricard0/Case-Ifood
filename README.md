
<h1 align="center">Case Engenharia de Dados People Analytics - Ifood :motor_scooter::hamburger:</h1>

## :memo: Descrição
O time de Recrutamento e Seleção recebeu uma informação que os seguidores de uma determinada pessoa candidata no github podem ser potenciais para a vaga de engenharia de dados. Por isso, Recrutamento solicitou que fosse feito o web scraping usando a api do github para criar uma lista dessas pessoas candidatas e essa é a descrição da tarefa.

Você precisa construir uma tabela que contenha as seguintes colunas:
name, company, blog, email, bio, public_repos, followers, following, created_at

Conversando com uma outra pessoa engenheira você recebeu a dica que a melhor maneira de fazer essa tarefa seria usar esse endpoint: [https://api.github.com/users/{user}/followers](https://api.github.com/users/{user}/followers) para conseguir a lista de followers e em seguida iterar em cada follower usando esse endpoint: [https://api.github.com/users/{user}](https://api.github.com/users/{user}).

Depois de conseguir a tabela alguns campos precisam ser limpos, tirar o @ do campo company, transformar o campo created_at para ele estar no formato dia/mês/ano. Carregue os dados em um csv. (não precisa enviar o csv, apenas o código utilizado.)

**Recomendações:**
- Crie uma chave de api para se autenticar a api tem um rate limit pequeno.
- Seria interessante criar o código em pyspark.
- Escolha uma pessoa no github que tenha entre 31 e 100 followers no github.

**Alguns exemplos aleatórios de users:**
- [elonmuskceo](https://github.com/elonmuskceo)
- [cvscarlos](https://github.com/cvscarlos)
- [marciocl](https://github.com/marciocl)


## :wrench:  Tecnologias utilizadas
* Python;
* Pyspark;
* Pandas;

## :rocket: Rodando o projeto
Para rodar o repositório é necessário clonar o mesmo,
1. Criar um arquivo `.env` com de acordo com `example.env` [Doc para o token](https://docs.github.com/pt/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28)
2. Executar os seguintes comandos para rodar o pipeline:
```
pip install -r requirements.txt
```
```
python api_github_pandas.py    
```
## :handshake: Colaboradores
<table>
  <tr>
    <td align="center" >
      <a href="https://github.com/paul-ricard0">
        <img src="https://avatars.githubusercontent.com/u/63252822?v=4" width="100px;" /><br>
        <sub>
          <b>Paulo Ricardo Lima</b>
        </sub>
      </a>
  </tr>
</table>
