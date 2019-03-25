# Avaliação Técnica

## Organização de classes/arquivos
* _GeoParser_, contida no arquivo _geoparse.py_ é uma classe que, basicamente, faz o processamento das linhas do arquivo. Ela faz isso possivelmente com qualquer linha de tenha a sintaxe no formato DMS (Degrees Minutes Seconds). Ao ter todos os dados (Latitude, Longitude e Altitude), ela possui um método para retornar um *Point*, formato do GeoPy para pontos geográficos.
* _PointLocator_, contida no arquivo _pointlocator.py_ é uma classe que, dado um ponto no formato Point do GeoPy, pode localizá-lo. Ela utiliza o Geocoder ArcGIS, o qual permite um número de requisições por mês gratuitamente. Todos os outros Geocoders (inclusive o do google maps v3) necessitam de pagamento e, como o enunciado prevê o uso apenas de tecnologias opensourse, isso foi o mais próximo disso que consegui encontrar.
* _Address_, contida no arquivo _address.py_ é uma classe que extrai os dados requisitados de um objeto Location (geopy). Ela também é responsável pela geração dos SQL's para persistir seus objetos.
* _DatabaseService_, contida no arquivo _database.py_ é uma classe que intermedia as interações (inserts e queries) com o BD.
* No arquivo extract_data.py está implementada toda a lógica de negócio para ler os dados dos arquivos, gerar pontos geográficos a partir deles, obter sua localização (informações como rua, CEP, cidade, etc.) e armazená-los no banco de dados.
---

## Extração das Coordenadas dos arquivos - Premissas
* Identificado que o arquivo nem sempre segue o padrão Latitude, Longitude, Altitude. Isso pode ser ou característico do sistema, ou um erro na geração do arquivo. Considerando que pode ser erro na geração do arquivo, identificaram-se poucos casos com esse comportamento (menos de 1 dezena no arquivo 20180101).
* Devido ao ponto citado acima, o leitor do arquivo (extract_data.py) foi desenvolvido como uma máquina de estados (LAT -> LON -> ALT) para evitar erros de consistência. Notar que, com isso, presume-se que todos os dados no formato LAT -> LON -> ALT estão corretos, registros fora dessa ordem são descartados.

---

## Banco de dados
* Tendo em vista que esse é apenas um projeto de demonstração de capacidades, optei por utilizar sqlite como RDBMS.
* Alguns comandos do banco:
    - Em uma linha de comando, execute sqlite3, se houver instalado esse comando inicia um processo do sqlite no console. Para finalizar, ctrl + C.
    - Se precisar instalar, _sudo apt-get install sqlite3_.
    - Para criar o banco, no diretório data deste zip, digite _sqlite3 <database_name>.db < create_database.sql_.
    - Para acessar o banco, basta executar _sqlite3 <database_name>.db_.
* Dependendo da possibilidade de reutilização do banco, talvez o ideal fosse utilizar um framework de mapeamento objeto-relacional (ORM), como o SQLAlchemy.

## Utilizou-se...
* Python 3.7
* Bibliotecas Python
    * [GeoPy](https://geopy.readthedocs.io), para instalar _pip install geopy_
    *
* SQLite
