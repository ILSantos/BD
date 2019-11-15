# Questões de Revisão P2

1. **O que são e como estão relacionados os conceitos de `Esquema`e `Instância` de Banco de Dados. Defina de forma precisa o que significa `consistência` de dados.**

- O esquema é uma descrição (textual ou gráfica) da estrutura de um BD de acordo com um determinado modelo de dados (descrição das tabelas, domínios e restrições).
- A instância é um conjunto de dados armazenados em um banco de dados em um determinado instante de tempo. E deve seguir o esquema definido.
- Consistência é a propriedade que garante que todas as tuplas de uma relação obedecem o esquema da relação.

2. **Qual a diferença entre um esquema de banco de dados e um estado ou instância de um banco de dados?**

- Um BD relacional é uma coleção de esquemas das relações presentes no banco de dados.
- O esquema especifica o nome da relação, o nome de cada atributo e o seu domínio.
- Uma instância de uma relação é um conjunto de tuplas, no qual cada uma tem o mesmo número de atributos que o esquema da relação. Naturalmente, cada instância deve satisfazer as restrições de domínio nesse esquema, a fim de mater a consistência.

3. **Defina os seguintes termos: domínio, atributo, tupla, esquema de relação, instância/estado de relação, grau de uma relação, esquema de um banco de dados relacional, instância/estado de um banco de dados relacional, chave**

`relação` é o principal construtor para representar dados no modelo relacional. Consiste em um `esquema de relação` e em uma `instância de relação`. O `modelo de dados` é um conjunto de conceitos que podem ser usados para descrever  a estrutura de um banco de dados.

| termo | definição|
|------|---------:|
| instância/estado de relação | tabela
| esquema de relação | descreve os cabeçalhos de coluna da tabela
| atributo | campo ou coluna de uma relação
| tupla | linha de uma relação (em um dado instante)
| domínio (de atributo) | conjunto de valores que um atributo pode assumir
| grau/aridade de uma relação | número de atributos da relação
| cardinalidade de uma instância | número de tuplas que a instância contém
| instância/estado de um BD relacional | conjunto de instâncias de relação, uma por esquema de relação no esquema de BD (snapshot)
| chave | conjunto de atributos de uma relação que devem ter valor único dentre todas as tuplas

4. **Defina chave estrangeira. Para que esse conceito é usado?**

Chave estrangeira é um tipo de restrição para relacionar relações distintas. A chave estrangeira na relação de referência deve corresponder à chave primária da relação referenciada.

5. **Liste as operações da álgebra relacional e a semântica de cada uma.**

- União, Intersecção e Diferença
- Seleção **`σ c (R)`**: selecionar linhas de `R` que satisfazem um critério `c`
- Projeção **`π L (R)`**: selecionar colunas de `R` que estão listados em `L` separados por vírgula
- Produto Cartesiano **`A ⨯ B`**: emparelha cada tupla de `A` com cada tupla de `B`
- Junção Theta (e Natural) **`A ⨝ c B`**: toma o produto cartesiano das relações `A` e `B` e aplica a seleção com a condição `c`
- Renomeação **`ρ R`**: modifica o esquema da relação
- Divisão **`A ÷ B`**

6. **O que é compatibilidade de união? Por que as operações UNIÃO, INTERSEÇÃO e DIFERENÇA exigem que as relações nas quais elas forem aplicadas sejam união compatíveis?**

A compatibilidade de união/tipo é a condição de que as duas relações sobre as quais uma as operações de conjuntos são aplicadas precisam ter o mesmo **tipo de tuplas**.
Duas relações são consideradas _compatíveis na união_ se tiverem o mesmo grau e cada par correspondente de atributos têm o mesmo domínio (i.e., mesmos esquemas).

7. **Discuta os vários tipos de operações de junção interna. Por que a junção theta é necessária?**

Os tipos de junção interna são:

- junção natural
- equijunção
- junção theta

8. **Relacione os tipos de dados que são permitidos como atributos SQL.**

9. **Como a SQL viabiliza a implementação das restrições de integridade de entidade e referencial?**

10. **Discuta como os NULLs são tratados em operadores de comparação na SQL. Como são tratados os NULLs quando funções agregadas são aplicadas em uma consulta em SQL? Como os NULLs são tratados se existirem em atributos agrupados?**

A lógica das condições SQL aceita 3 valores: TRUE, FALSE e UNKNOWN. Comparando qualquer valor com NULL, retorna-se UNKNOWN

11. **Como a SQL implementa as restrições de integridade genéricas?**

12. **O que são triggers? Dê dois exemplos de sua utilização.**

Gatilhos (triggers) são procedimentos de verificação executados quando ocorre uma condição específica. Por exemplo, inserção de tupla, atualização de valores. São mais fáceis de implementar do que restrições complexas.

13. **O que é uma visão em SQL e como é definida? Discuta os problemas que podem surgir quando se tenta atualizar uma visão**

Uma visão (view) é uma tabela virtual; uma relação definida em termos do conteúdo de outras tabelas ou visões. Modificações em uma view são possíveis mas são limitadas a atualizações que podem ser refletidas nas tabelas base. Ainda é possível _materializar_ a view para criar uma tabela real a partir dela.
