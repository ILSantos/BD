1. **Considerando um disco magnético típico usado para armazenamento de dados em memória secundária, identifique, descreva e compare brevemente os componentes do tempo de acesso aos dados armazenados.**

O tempo de acesso para leitura ou escrita em disco requer três passos (cada um custa um tempo):

- `seek`: busca da trilha;  posicionamento do braço na trilha correta
- `rotação`: espera para que o setor desejado seja posicionado até a cabeça de leitura/escrita
- `transferência`: transferência dos bits (em bloco) armazenados no setor que está ao alcance da cabeça

O tempo de transferência sempre será necessário, mas os outros dois podem ser ignorados se os blocos a serem lidos/escritos estiverem em setores sequenciais.

2. **Discuta as vantagens e desvantagens em se utilizar (a) um arquivo não ordenado (b) um arquivo ordenado (c) um arquivo estático hash com buckets e encadeamento. Quais operações podem ser realizadas de maneira mais eficiente em cada um destes tipos de organização e quais são dispendiosas.**

      1. Um **arquivo não ordenado** tem seus registros inseridos sempre no final -- último bloco, logo a inserção será ótima. Consequentemente, a busca será sequencial, o que custará no desempenho.
      2. Um **arquivo ordenado** tem melhor desempenho mas as inserções são complexas pois podem usar blocos de overflow (para reduzir o custo da inserção).
      3. Um **arquivo de hashing** tem busca pelo campo de hashing bem rápido; as inserções também podem envolver blocos de overflow e isso prejudica o desempenho na busca. Mas é possível listar os itens ordenados de forma mais rápida que no uso de arquivos não ordenados (apesar da complexidade ser maior).
   
3. **Considere um disco com blocos de B=1 Kbyte. Um apontador de blocos tem P=6 bytes e um apontador de registro tem PR=7 bytes. Um arquivo tem 50.000 registros EMPREGADO de tamanho fixo. Cada registro tem os seguintes campos: NOME (30 bytes), CPF (9 bytes), TELEFONE (9 bytes), DATANASC (8 bytes), SEXO (1 byte). Um byte adicional é usado como marcador de exclusão. Suponha que CPF é um campo-chave. Pede-se:
(a) a ordem de uma árvore-B+ construída sobre CPF para este arquivo; (b) o número de blocos de índice necessários para manter os blocos 50% cheios; (c) o número de níveis da árvore neste caso.**

4. **Descreva a estrutura dos nós internos e dos nós folha de uma árvore-B+. Quais as vantagens deste tipo de estrutura em comparação com as arvores-B comuns?**
