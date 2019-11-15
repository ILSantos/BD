# Questões de Revisão P3

1. **Quais as principais propriedades que toda transação deve ter?**

- **Atomicidade:** uma transação é uma unidade atômica de processamento; ou ela será executada em sua totalidade ou não será de modo nenhum.
- **Consistência:** uma transação será preservadora de consistência se sua execução completa fizer o banco de dados passar de um estado consistente para outro.
- **Isolamento:** uma transição deve ser executada como se estivesse isolada das demais. Isto é, a execução de uma transição não deve sofrer interferência de quaisquer outras transações concorrentes.
- **Durabilidade:** As mudanças aplicadas ao banco de dados por uma transação efetivada devem persistir no banco de dados. Essas mudanças não devem ser perdidas em razão de uma falha.
  
2.  **Discuta como ocorre, durante a operação de um SGBD, o chamado `Checkpoint`. Quais vantagens e desvantagens de se fazerem checkpoints frequentes?**

`Checkpoint` consiste em suspender temporariamente a execução de transações para realizar todas as operações de escrita no banco de dados. O checkpoint é então registrado no log e a execução das transações é liberada novamente.

**Vantagem de se fazer checkpoint frequente:** a recuperação de falhas é mais rápida, pois o checkpoint reduz e limita a quantidade de REDOs

**Desvantagem:** a efetivação de um única transação exige que diversos blocos sejam movimentados, prejudicando o desempenho so SGBD.

3.  **Considerando a transação abaixo, use primitivas de bloqueio para construir uma transação que segue o 2PL estrito.**

``` 
T: read_item(Z); read_item(Y); write_item(Y); read_item(X); write_item(X);
```
> | T |
> |---|
> | read_lock(Z) |
> | read_item(Z) |
> | read_lock(Y) |
> | read_item(Y) |
> | write_lock(Y) |
> | write_item(Y) |
> | read_lock(X) |
> | read_item(X) |
> | write_lock(X) |
> | write_item(X) |
> | unlock(Z) |
> | unlock(Y) |
> | unlock(X) |

4.  **Descreva os protocolos de bloqueio 2PL e 2PL estrito. Analise comparativamente as vantagens e desvantagens destes protocolos.**

**2PL:**  two-phase locking ou bloqueio em 2 fases, uma transação segue o 2PL se todos os locks (read_lock, write_lock) precedem o primeiro unlock. Uma transação que segue o 2PL pode ser dividida em 2 fases: expansão - onde os locks são obtidos mas nenhum é liberado, e contração - onde os locks são liberados mas nenhum novo lock é obtido.

**Vantagem:** garante escalonamento serializável.

**Desvantagens:** limita a concorrência, pode gerar deadlocks e starvations.

**2PL Estrito:** nenhum write-lock é liberado até que a transação execute um commit ou abort. Portanto, nenhuma outra transação pode acessar um item até que T comprometa ou aborte.

**Vantagem:** garante escalonamento serializável e estrito, sem necessidade de rollback em cascata.

**Desvantagens:** por ser estrito, limita ainda mais que o 2PL básico a concorrência. Pode gerar deadlocks e starvations.

5.  **O que é `starvation` (inanição) e em que situações esta anomalia pode ocorrer? Apresente um exemplo descrevendo uma destas situações.**

`Starvation` é um problema que ocorre quando uma transação é impedida de progredir por outras transações durante um longo período de tempo. Pode ocorrer em esquemas de bloqueio/desbloqueio injustos que priorizam determinadas transações sobre outras ou esquemas de prevenção de deadlock que vitimam a mesma transação repetidas vezes.

6.  **O que é um escalonamento recuperável? Apresente um exemplo de um escalonamento não recuperável.**

Escalonamento recuperável é o escalonamento que garante que, uma vez comprometida uma transação, ela nunca será desfeita. Um escalonamento é recuperável se nenhuma transação T for comprometida até que todas as transações T', que tiverem gravado um item lido por T, tenham sido comprometidas.

Exemplo de um escalonamento não recuperável:

```
S: r1(X); w1(X); r2(X); r1(Y); w2(X); c2; a1;
 ```

7.  **Considere um transação que utiliza `REPEATABLE READ`. Dê um exemplo de uma operação de escrita executada por uma transação T2 que causa a ocorrência de tuplas fantasmas em uma operação de escrita de uma transação T1.**

**Exemplo:** uma transação T1 acessa todos os registros dos alunos matriculados numa determinada turma para calcular média da turma. E existe uma transação T2 que está atualizando a nota de um aluno. Se a ordem serial for T1 seguida de T2, o registro atualizado por T2 será um registro fantasma, pois apareceu subitamente.
