# NewsScraping 

Esse é um projeto de raspagem das últimas noticias, de 2021, do portal da universidade Ucsal http://noosfero.ucsal.br/institucional


## Dados Extraidos 

O projeto conta um um único spider que extrai titulo, data e o link da respectiva noticia raspada e disponiza os dados em formato json.

Exemplo de dado extraido:

    {
    
    "title": "INSCRIÇÕES ABERTAS PARA O PROGRAMA DE MONITORIA SOLIDÁRIA DA GRADUAÇÃO 2021.2",
    "date": "18 de Agosto de 2021, 18:34",
    "link": "http://noosfero.ucsal.br/institucional/noticias/inscricoes-abertas-para-o-programa-de-monitoria-solidaria-da-graduacao-2021.2"
    
    }


 ## Rodar o spider:

Entre no diretorio do arquivo: 

      cd crawler/crawler/spiders

Execute o comando: 

      scrapy crawl noticias
