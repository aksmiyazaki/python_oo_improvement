# Avaliação Técnica

## Extração das Coordenadas dos arquivos - Premissas
* Identificado que o arquivo nem sempre segue o padrão Latitude, Longitude, Altitude. Isso pode ser ou característico do sistema, ou um erro na geração do arquivo. Considerando que pode ser erro na geração do arquivo, identificaram-se poucos casos com esse comportamento (menos de 1 dezena no arquivo 20180101). Portanto, o Parser será desenvolvido como uma máquina de estados (LAT -> LON -> ALT) para evitar erros de consistência. Notar que, com isso, presume-se que todos os dados no formato LAT -> LON -> ALT estão corretos, registros fora dessa ordem são descartados.
