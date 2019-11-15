1. **Um banco de dados é:**

Um conjunto de dados logicamente estruturados e que são usados para uma determinada aplicação

2. **Comparando a abordagem de banco de dados com a abordagem tradicional de processamento de arquivos, NÃO podemos afirmar que:**

As aplicações que utilizam a abordagem BD apresentam, em geral, melhor tempo de execução
<!--
http://ehgomes.com.br/disciplinas/bdd/sgbd.php
-->

3. **Um modelo de dados é:**
Um conjunto de conceitos que é utilizado para gerar descrições da estrutura de um banco de dados

4. **Escolha uma alternativa que contém apenas componentes da arquitetura de um SGBD típico:**

Otimizador de consultas, subsistema de backups e recuperação de falhas e compilador LDD

5. **Quais as principais categorias de modelos de dados? Dê exemplos destes modelos e suas aplicações.**

Um modelo de BD é uma descrição dos tipos de informações que estão armazenadas nele (informa qual o tipo das informações que ele armazena).
O esquema de banco de dados é uma descrição do modelo.

Uma para cada nível de abstração:

- modelo conceitual:
  - registra QUE dados podem aparecer no BD.
  - representação de alto nível de abstração.
  - modela de forma mais natural os fatos do mundo real, suas características e relações.
  - preocupação semântica da aplicação.
  - independe de BD.
  - eg. modelo entidade-relacionamento.
- modelo lógico (ou modelos de BD):
  - registra O QUE guardam os dados do BD.
  - representação dos dados alguma em estrutura (lógica) de armazenamento de dados.
  - depende de BD (mostra as ligações entre as tabelas, os atributos, etc).
  - eg. modelo relacional, modelo OO.
- modelo físico:
  - registra COMO os dados estão armazenados.
  - organização dos arquivos de dados em disco (organização sequencial, uso de índices ou B-Trees).
  - não são manipulados por usuários ou aplicações que acessam o BD.
  - implementação depende do SGBD.

7. **usando o <https://dbis-uibk.github.io/relax/calc.htm>**

**(a)** obter nome das clínicas que tem médicos que atuam na especialidade denominada 'Geriatria'

```
EspeciGeriatria :=  σ Nome = 'Geriatria' (Especialidade)
Geriatras := Medico ⨝ EspeciGeriatria
Ambos  := Geriatras ⨝ ClinicaMedico

π NomeCli (Ambos ⨝ Clinica)
```

**(b)** obter os códigos dos médicos que atuam em todas as clínicas cadastradas no banco de dados
```
Medicos := γ CodMed, n←COUNT(CodMed) (ClinicaMedico)
TotalClinicas := γ n←COUNT(CodCli) (Clinica)

π CodMed( Medicos ÷ TotalClinicas )
```

**(c)** obter os nomes dos médicos que estão livres no dia 28/04/2016
```
CodMedicosLivres := π CodMed (
    σ Data ≠ '28/04/2016' (AgendaConsulta)
)

π NomeMed (Medico ⨝ CodMedicosLivres)
```

**(d)** obter uma tabela contendo as seguintes colunas: Código e nome da cada clínica, Nome de cada médico da clínica que atua na especialidade 'Obstetrícia'. Caso a clínica não tiver médicos ou, caso ela não tiver nenhum médico atuando nesta especialidade, o código e nome da clínica devem aparecer seguidos de _NULL_

```
Obstetras := σ nome = 'Obstetrícia' (Medico ⟕ Especialidade)
Clinicas := ClinicaMedico ⨝ Obstetras

π CodCli, NomeCli, NomeMed (Clinicas ⟕ Clinica) 
```

**(e)** Para cada médico que atua em duas clínicas diferentes, obter nome do médico seguido do nome das clínicas
```
Medicos := σ qtdCli = 2 (
	γ CodMed; qtdCli←COUNT(CodCli) (ClinicaMedico)
)

MedicosClinicas := ClinicaMedico ⨝ Medicos
Nomes := Medico ⨝ MedicosClinicas 

π NomeMed, NomeCli (Nomes ⨝ Clinica)
```
