# Processamento e Otimização de Consultas

```
consulta > Analisador de Consultas -> consulta analisada > Otimizador de Consultas -> plano avaliado > Avaliador de Planos de Consultas
```

1. **O que é um plano de execução da consulta?**

> Sequência de passos executados pelo SGBD para obter a resposta a uma consulta.

2. **Como as consultas SQL são transformadas em álgebra relacional? Como consequência, em qual classe de consultas da álgebra relacional um otimizador de consultas de concentra?**

> As consultas em linguagem de alto nível são otimizadas pela sua decomposição em um conjunto de unidades menores chamadas _blocos_ (contém apenas uma clausula `SELECT-FROM-WHERE`).
> Um otimizador relacional típico se concentra na otimização de um único bloco por vez da classe de planos de profundidade à esquerda (na árvore de expressões).

3. **Qual é o objetivo do processamento de consultas?**

> Transformar uma consulta escrita em uma linguagem declarativa de alto nível em uma estratégia de execução correta e eficiente expressa em uma linguagem de baixo nível. E então executar corretamente a estratégia para recuperar os dados.

4. **Qual a principal tarefa de um otimizador?**

> Escolher a melhor (dentre um subconjunto de todas) estratégia de execução para processar uma consulta [a que minimiza o uso dos recursos].

5. **Como um otimizador calcula o custo de um plano de avaliação de consulta?**

> Para cada plano enumerado, precisa-se estimar seu custo. Esse processo é feito em duas partes:
>
> 1. para cada nó na árvore, devemos _estimar o custo_ da execução da operação correspondente;
> 2. Para cada nó na árvore, devemos _estimar o tamanho do resultado_ e verificar se ele está ordenado.

6. **Como um otimizador gera planos alternativos de avaliação de consulta? Qual é o espaço de planos considerado?**

> As equivalências algébricas formam a base da geração de planos alternativos, em conjunto com a escolha da técnica de implementação dos operadores relacionais presentes na consulta.
> Saber qual é o espaço de planos alternativos considerados para determinada consulta é o problema centro de um otimizador.

7. **Como as consultas SQL aninhadas são otimizadas?**

> As consultas aninhadas são tratadas usando-se alguma forma de avaliação de loops aninhados.

8. **Quais informações são armazenadas no catálogo do sistema de um SGBD e como são usadas na otimização de consultas?**

> Otimizadores recuperam do catálogo informações sobre os tipos e comprimentos dos campos, estatísticas sobre as relações referenciadas e os índices.
> Além do tamanho do arquivo, número de tuplas, número de blocos e o fator de bloco.

9. **O que é um plano de avaliação de consultas?**

> Um plano consiste de uma árvore de álgebra relacional estendida, com anotações adicionais em cada nó indicando os métodos de acesso a usar por cada tabela e o método de implementação por cada operador relacional.

10. **Cite as formas de avaliação de árvores**

> Materialização e Pipelining.
> Na materialização, os resultados das operações são armazenados em disco temporariamente. Avalia-se um operador por vez (bottom-up). É sempre aplicável mas os custos de I/O das relações temporárias pode ser alto.
> No pipelining, várias operações são avaliadas simultaneamente. Os resultados de uma operação são passados para a próxima assim que possível. Tem o custo inferior ao da Materialização mas seu uso nem sempre é possível (eg. hash-join, sort, etc).
> Há duas formas:
>
> - pipelining sob demanda (PULL; "lazy evaluation") -- o sistema requisita repetidamente a próxima tupla da operação de nível superior;
> - pipelining orientada à produção (PUSH; "eager") -- os operadores geram suas tuplas continuamente e passam para os operadores "pai";

## Transações e Locks

1. **O que é uma transação?**

> Uma transação é definida como `qualquer execução única` de um programa de usuário em um SGBD,
> ie., execução de um programa que acessa ou modifica o conteúdo de um BD.
> O conceito de transação é a base da execução concorrente e da recuperação de falhas de sistema em um SGBD.

2. **Quais as propriedades das transações que são garantidas pelo SGBD? Quais são os estados de uma transação?**

> As 4 propriedades ACID são:
>
> - Atomicidade [gerenciador de transação] = ou todas as operações da transação são refletidas corretamente no BD ou nenhuma o será;
> - Consistência [responsabilidade do usuário] = toda transação enxerga uma instância consistente do BD;
> - Isolamento [controle de concorrência] = transações são protegidas dos efeitos do plano de execução concorrente de outras transações;
> - Durabilidade [log/recuperação] = persistência dos efeitos de uma transação comprometida.

![estados-transacao](https://image.slidesharecdn.com/techtudpptformat7-170428082921/95/state-of-transaction-in-database-2-638.jpg?cb=1493368256)

3. **Explique o "checkpoint" realizado por um SGBD**

> A intervalos regulares, o SGBD executa um _checkpoint_ que consiste em:
>
> 1. suspender temporariamente a execução de transações;
> 2. atualizar todas as operações de escrita realizadas no banco de dados;
> 3. registrar no log uma entrada do tipo `[CHECKPOINT]`
> 4. liberar as execuções de transação.

4. **Quais os principais problemas no controle de concorrência?**

> Atualização perdida, atualização temporária (dirty read: leituras de dirty data: dados escritos por transações não commitadas), sumarização incorreta e leitura dupla.

5. **Por que um SGBD intercala transações**

> Por motivos de desempenho, assim pode realizar a concorrência das operações das transações (além de um melhor uso da CPU).
> Podendo aumentar o número médio de transações completadas em um determinado tempo (throughput do sistema).
> Além disso, a execução intercalada de uma transação curta com uma longa normalmente permite que a curta termine rapidamente (evita o _starvation_/inanição).

6. **Quais tipos de anomalias as transações intercaladas podem causar?**

> As 3 situações anômalas podem ser descritas em termos de quando as operações de duas transações entram em conlito entre si: gravação-leitura (WR), leitura-gravação (RW) e gravação-gravação (WW).

7. **Como um SGBD usa bloqueios para garantir intercalações corretas?**

> Através do uso de um protocolo de bloqueio, um conjunto de regras a ser seguidas por transação (e impostas pelo SGBD) para garantir que, mesmo intercalando as operações de várias transações, o resultado seja idêntico à execução de todas as transações em alguma ordem serial.

8. **Qual o impacto do bloqueio no desempenho?**

> Bloqueio e cancelamento são os dois mecanismos básicos usados quando se usa locks para resolver conflitos entre transações.
> Esses mecanismos envolvem uma penalidade no desempenho:
> transações bloqueadas podem manter bloqueios que obriguem outras transações a esperar, e o cancelamento e o reinício de uma transação desperdiçam o trabalho feito até o momento por ela.
> O _deadlock_ representa um caso extremo de bloqueio no qual um conjunto de transações fica bloqueado para sempre (a não ser que uma delas seja cancelada pelo SGBD).

9. **Quais comandos SQL permitem que os programadores selecionem características da transação e reduzam a sobrecarga (overhead) do bloqueio?**

> O nível de isolamento e o modo de acesso podem ser configurados com o comando ```SET TRANSACTION ISOLATION LEVEL```.

10. **Como um SGBD garante a atomicidade da transação e a recuperação de falhas de sistema?**

> O gerenciador de recuperação (_recovery manager_) de um SGBD é responsável por garantir a atomicidade e a durabilidade das transações.
> Ele garante a atomicidade desfazendo as ações das transações que não são efetivadas (canceladas ou abortadas).
> Quando um SGBD é reiniciado após falhas, o gerenciador de recuperação recebe o controle deve levar o BD para um estado consistente.

11. **Diferenças entre _deadlock_ e _concorrência_**

> A concorrência ocorrer quando processos disputam um recurso compartilhado (causando _race condition_).
> Já o deadlock ocorre quando um conjunto de transações querem acessar um item/objeto de dados _x_ que está bloqueado por uma outra transação que está nesse conjunto (causando uma fila circular de espera).

12. **Em que situações duas operações em um schedule (plano de execução) são ditas "conflitantes"?**

> Quando pertencem a transações diferentes, acessam o mesmo item de dados _X_ e pelo menos uma das duas é escrita _X_.

13. **Quando um schedule é dito "completo"?**

> Um schedule _S_ de _n_ transações é dito ser completo se as seguintes condições ocorrem:
>
> 1. As operações de _S_ são exatamente aquelas das suas _n_ transações, inclusive as operações `commit` e `abort` como sendo as últimas operações de cada transação;
> 2. Para cada par de operações da mesma transação Ti em _S_, temos que a ordem em que estas operações aparecem na transação é preservada no schedule;
> 3. Para quaisquer duas operações conflitantes, uma das duas deve necessariamente ocorrer antes da outra no schedule.

14. **Quando um schedule é dito "recuperável"?**

> Quando nenhuma transação _T_ é comprometida até que todas as demais transações, que tenham escrito um item que _T_ deve ler, estejam comprometidas [realizar `commit` em escritas antes que alguém  precise ler].

15. **O que é um Schedule/Escalonamento Estrito?**

> Nenhuma transação pode ler/escrever um item _X_ até que a última transação que escreveu _X_ seja comprometida ou abortada.

16. **O que é um Schedule Serial?**

> É um schedule onde as operações das transações são executadas sem intercalação (ausência de concorrência); está de acordo com as propriedades ACID.

17. **Diferencie o lock binário do lock multi-modo**

> O lock binário possui 2 estados: `unlock` e `lock`, enquanto o multi-modo possui 3 estados: `read-lock`, `write-lock` e `unlock`.
> 
> O lock binário é muito simples e restritivo, por isso não é utilizado na prática.
> 
> Garante a exclusão mútua em um item de dados.

18. **O que é o Two-Phase Lock (2PL)?**

> É um protocolo para controle de concorrência baseado em bloqueios (locks).
>
> Uma transação segue o 2PL se todos os locks (`read_lock` e `write_lock`) precedem o primeiro `unlock`.
> Na primeira fase ocorre a expansão, locks são obtidos mas nenhum é liberado.
> Na segunda fase ocorre a contração, locks são liberados mas nenhum novo lock é obtido.

1. **Cite as variações do 2PL**
>
> - 2PL Conservativo: a transação deve bloquear todos os itens antes de iniciar, garantindo a ausência de deadlocks.
>
> - 2PL Estrito*: nenhum `write_lock` é liberado até que a transação se efetive (execute _abort_ ou _commit_); garante escalonamentos estritos.
>
> - 2PL Rigoroso: nenhum `write_lock` ou `read_lock` é liberado até que a transação se efetive; mais restrito que anterior e mais simples de implementar.

1. **Quais os quatro níveis de isolamento da SQL e quais os fenômenos (tipos de violação) que podem ocorrer em cada um?**

> O nível de isolamento define o comportamento da transação em relação ao controle de concorrência. Controla até que ponto uma transação é exposta às ações das outras que estão sendo executadas concorrentemente.

| nível                | leitura suja | leitura dupla | tupla fantasma |
|:---------------------|:------------:|:-------------:|:--------------:|
|`READ UNCOMMITED`     | talvez       | talvez        | talvez         |
|`READ COMMITED`       | não          | talvez        | tavez          |
|`REPEATABLE READ`     | não          | não           | talvez         |
|`SERIALIZABLE`        | não          | não           | não            |

21. **O que é um grafo de precedência no contexto de BDs? Dê um exemplo de uso.**

> Um plano de execução é **serializável por conflito** se ele for equivalente quanto ao conflito a algum plano serial.
> O grafo de precedência ajuda a visualizar todos os conflitos em potencial entre as transações de um PEC. Assim podemos saber se ela é serializável em relação às operações.
> Tendo duas transições A e B, o grafo é definido da seguinte forma: os vértices são as transações efetivadas e as arestas são criadas se o PEC tem uma das seguintes condições como verdadeira (o rótulo da aresta é o ítem de dados que está sendo compartilhado):
>
> - A executa w(X) antes de B executar r(X)
> - A executa r(X) antes de B executar w(X)
> - A executa w(X) antes de B executar w(X)
>
> Se ocorrer ciclo no grafo, então o escalonamento é dito não serializável por conflito.
> EXEMPLO de um serializável por conflito:
>
> - R2(x); W3(x); C3; W1(x); C1; W2(y); R2(z); C2; R4(x); R4(y); C4;
[![eg-](https://image.prntscr.com/image/-_c2FMMkQRuWyc1xyE14JA.png)]
<!-- (c) https://www.youtube.com/watch?v=A5t1aOfTweE -->

### TL;DR

- __Transações Atômicas__: unidades lógicas de processamento sobre um BD.

- __Controle de Concorrência__: garantia de que múltiplas transações ativadas por vários usuários produzirão resultados corretos quando manipulam o BD.

- __Recuperação de Falhas__: garantia de que os efeitos das transações são mantidos no BD mesmo com a ocorrência de falhas.

- __Schedules de Transações__: ordem para a execução de operações de transações; lista de ações/operações de um conjunto de transações.

- __Log__: permite a recuperação de falhas de uma transação pois registra todas as operações que afetam os valores dos itens de dados.

- __Schedule Serializável__: schedule não serial que equivale à um serial, ie., produzem o mesmo estado no BD.

- __Projeção Comprometida__: schedule que contém somente as operações que pertencem a transações comprometidas.

- Um schedule __evita roolback em cascata__ se cada transação nele só lê itens que foram escritos por transações comprometidas.

- Um __lock__/bloqueio é uma variável associada a um item de dados em um BD (geralmente 1 pra cada item). Técnica para controlar a execução concorrente de transações.

- Se todas as transações de um plano seguem o 2PL, então, esse plano é __garantidamente serializável__ (não é necessário aplicar o teste de serializabilidade).

- A __serialidade__ é o critério de correção geralmente aceito a para execução intercalada de determinado conjunto de transções.
