# Avaliação Técnica

## Extração das Coordenadas dos arquivos - Premissas
* Identificado que o arquivo nem sempre segue o padrão Latitude, Longitude, Altitude. Isso pode ser ou característico do sistema, ou um erro na geração do arquivo. Considerando que pode ser erro na geração do arquivo, identificaram-se poucos casos com esse comportamento (menos de 1 dezena no arquivo 20180101).
* Devido ao ponto citado acima, o leitor do arquivo (extract_data.py) foi desenvolvido como uma máquina de estados (LAT -> LON -> ALT) para evitar erros de consistência. Notar que, com isso, presume-se que todos os dados no formato LAT -> LON -> ALT estão corretos, registros fora dessa ordem são descartados.

---

## Organização de classes/arquivos
* PointLocator é um singleton para não haver a possibilidade de gerar múltiplas conexões com um serviço de coordenadas.

---

## Banco de dados
* Tendo em vista que esse é apenas um projeto de demonstração de capacidades, optei por utilizar sqlite como RDBMS.
* Alguns comandos do banco:
    - Em uma linha de comando, execute sqlite3, se houver instalado esse comando inicia um processo do sqlite no console. Para finalizar, ctrl + C.
    - Se precisar instalar, _sudo apt-get install sqlite3_.
    - Para criar o banco, no diretório data deste zip, digite _sqlite3 <database_name>.db < create_database.sql_.
    - Para acessar o banco, basta executar _sqlite3 <database_name>.db_.

## Utilizou-se...
* Python 3.7
* Bibliotecas Python
    * [GeoPy](https://geopy.readthedocs.io), para instalar _pip install geopy_
    *
* SQLite
