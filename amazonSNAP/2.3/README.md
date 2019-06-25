# Notas sobre a Dashboard

A dashboard depende do Python 3.7 e de algumas bibliotecas. 
Caso elas não estejam instaladas, use o script `./prepare_env.sh` para configurar
seu ambiente.


A dashboard depende de uma ordem específica para os argumentos de inicialização. Um
comando funcional é:

`python3.7 start.py 127.0.0.1 alecrim alecrim alecrim`
 
 POSTGRES_HOST -> DB_NAME -> USER_NAME -> PASSWORD