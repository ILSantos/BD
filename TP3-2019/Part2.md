# Parte II

Verificar as características de organização física dos dados, registros, blocos e arquivos no PostgreSQL.

## Tarefa II.1

Analisar e descrever os detalhes de armazenamento físico de dados no PostgreSQL. Descrever a estrutura lógica e física de um "database cluster", descrever um layout interno dos arquivos que armazenam os dados e índices, descrever os métodos de leitura e escrita de dados das tabelas.

#### Resposta

A estrutura física do PostgreSQL é bem simples, consistindo de memória compartilhada e alguns processos em background e arquivos de dados.
![Estrutura do PostegrSQL](https://severalnines.com/sites/default/files/blog/node_5122/image17.jpg)

Memória Compartilhada: refere-se a memória reservada para o armazenamento em cache do banco de dados e o log de transações. Os elementos mais importantes na memória compartilhada são os buffers de buffer compartilhado e WAL.

- Buffer Compartilhado: o objetivo é minimizar as E/S do disco. Para isso, os seguintes princípios devem ser atendidos:

  - precisa acessar buffers muito grandes (dezenas, centenas de gigabytes) rapidamente.

  - deve minimizar a disputa quando muitos usuários acessarem ao mesmo tempo.

  - os blocos usados com frequência devem estar no buffer o maior tempo possível.

- Buffer WAL: é um buffer que armazena temporariamente as alterações no banco de dados. O conteúdo armazenado no buffer WAL é gravado no arquivo WAL em um momento predeterminado. Do ponto de vista de backup e recuperação, os buffers WAL e os arquivos WAL são muito importantes.

O PostgreSQL tem quatro tipos de processos:

1. Processo do Postmaster: é o primeiro processo iniciado quando iniciamos o PostgreSQL. Na inicialização, executa a recuperação, inicializa a memória compartilhada e executa processos em background. Ele também cria um processo de backend quando há uma solicitação de conexão do processo do cliente.

    ![Diagrama de relacionamento do processo](https://severalnines.com/sites/default/files/blog/node_5122/image2.jpg)

    Verificando os relacionamentos entre processos com o comando `pstree` é possível verificar que o Postmaster é o pai de todos os processos.

2. Processo do Background: segue a lista de processos background requerida para operações PostgreSQL

   - logger: escreve a mensagem de erro no arquivo de log.
   - check pointer: quando um checkpoint ocorre o buffer sujo é gravado no arquivo.
   - writer: periodicamente escreve o buffer sujo em um arquivo.
   - wal wr iter: escreve o buffer WAL no arquivo WAL.
   - autovacuum launcher: bifurca quando o autovacuum está ativado. É de responsabilidade do daemon de autovacuum executar operações de vácuo em tabelas inchadas sob demanda.
   - archive: quando em modo Archive.log, copia o arquivo WAL para um diretório especifico.
   - stats collector: estatísticas de uso do DBMS, como informações de execução da sessão (`pg_stat_activity`) e informações estatísticas de uso da tabela (`pg_stat_all_tables`), são coletadas.

3. Processo do Backend: O número máximo de processos de backend é definido pelo parâmetro `max_connections` e o valor padrão é 100. O processo de backend executa a solicitação de consulta do processo do usuário e depois transmite o resultado. Algumas estruturas de memória são necessárias para a execução da consulta, denominada memória local. Os principais parâmetros associados à memória local são:

    - `work_mem`: espaço usado para classificação, operações de bitmap, junções de hash e junções de mesclagem. A configuração padrão é 4 MB.
    - `Maintenance_work_mem`: espaço usado para Vácuo e `CREATE INDEX`. A configuração padrão é 64 MB.
    - `Temp_buffers`: espaço usado para tabelas temporárias. A configuração padrão é 8 MB.

4. Processo do Cliente: refere-se ao processo em segundo plano atribuído a cada conexão de usuário backend. Geralmente, o processo do postmaster bifurca um processo filho dedicado a servir uma conexão do usuário.

## Tarefa II.2

Utilizar _docker_ para criar um container com PostgreSQL instalado. A seguinte imagem deve ser utilizada `http://hub.docker.com/_/postgres`

**Entregar:** o resultado dos comandos `sudo docker ps` executado no shell e `select version()` executado no psql.
