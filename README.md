## Desafio técnico - SRE

Para a conclusão deste desafio foram utilizados python+flask, docker e shellScript.

### Iniciando a aplicação

Para executar a aplicação, é necessário ter instalado o Docker. Para ambientes Linux, a aplicação pode ser iniciada utilizando o script start.sh:

    ./mao_na_massa/start.sh

Em ambientes Windows, os comandos devem ser executados diretamente no console Docker Desktop. Navegue até a pasta mao_na_massa e execute:

    docker build -t challengesre2023 --pull --force-rm .

    docker run --name challengeApp -p 5001:5000 -d challengesre2023:latest


### Consumindo a aplicação
Após iniciar a aplicação você poderá consumir as rotas conforme o filtro:

##### Realizar o filtro por nome de cliente
Utilizar a rota /filter-clients/clientName

Ex.: http://localhost:5001/filter-clients/cliente2

##### Realizar o filtro por tipo de arquivo 

Utilizar a rota /filter-typeFile/typeFile

http://localhost:5001/filter-typeFile/metrics

##### Realizar o filtro por data solicitada

Utilizar a rota /filter-date/2022_11_01

http://localhost:5001/filter-date/dateFile

##### Ao informar o nome de um cliente, excluir todos os arquivos dele

Utilizar a rota /remove-client/clientName

http://localhost:5001/remove-client/cliente8

##### Trazer todos os arquivos que possuam mais de X dias filtrando por nomedocliente

Utilizar a rota  /filter-ageFiles/client_forFilter/qtdDays

http://localhost:5001/filter-ageFiles/cliente8/45
