# Lista de Exercícios - Álgebra Relacional

## Enunciados

- **(1)** Quais os modelos de PC têm uma velocidade de pelos menos 3.00?

```
π model (
  σ speed ≥ 3.00 (PC)
)
```

```sql
SELECT DISTINCT model
FROM PC
WHERE speed >= 3
```

![r1](https://user-images.githubusercontent.com/13461315/30888614-70d99ab8-a2ef-11e7-8d33-487bf5aaa3f5.png)

-**(2)** Quais os fabricantes fazem laptops com um disco rígido de pelo menos 100GB?

```
A := σ hd ≥ 100 (Laptop)
π maker (Product ⨝ A)
```
```sql
SELECT DISTINCT maker
FROM Product
INNER JOIN
 ( SELECT * FROM Laptop WHERE hd >= 100 ) AS A
NATURAL
```
![r2](https://user-images.githubusercontent.com/13461315/30880266-ffbc921e-a2cf-11e7-8a0f-4a47931625fd.png)

- **(3)** Encontre o número do modelo e preço de todos os produtos (de qualquer tipo) que são produzidos pelo fabricante `B`

```
ProduzidosPorB := σ maker = 'B' (Product)
π model, price (ProduzidosPorB ⨝ PC)
∪ 
π model, price (ProduzidosPorB ⨝ Laptop)
∪
π model, price (ProduzidosPorB ⨝ Printer)
```
```sql
( SELECT DISTINCT model, price
FROM PC
INNER JOIN Product AS P NATURAL
WHERE maker = 'B' )
UNION
( SELECT DISTINCT model, price
FROM Laptop
INNER JOIN Product AS P NATURAL
WHERE maker = 'B' )
UNION
( SELECT DISTINCT model, price
FROM Printer
INNER JOIN Product AS P NATURAL
WHERE maker = 'B' )
```

![r3](https://user-images.githubusercontent.com/13461315/30778330-28e50026-a0a1-11e7-8327-2ad9bfa67ad0.png)

- **(4)** Encontre os números dos modelos de todas as impressoras a laser coloridas

π model (
  σ color = true ∧ type = 'laser' (Printer)
)
```
```sql
SELECT DISTINCT model
FROM Printer
WHERE color = true AND type = 'laser'
```
![r4](https://user-images.githubusercontent.com/13461315/30778380-9f7821a4-a0a2-11e7-8b2b-88c9f06c9f08.png)

- **(5)** Encontre os fabricantes que vendem laptops, mas não PCs

```
MakerFazPC := π maker ( σ type = 'pc' (Product) )
FazPC := Product ⨝ MakerFazPC
NaoFazPC := Product - FazPC

FazLaptop := σ type = 'laptop' (NaoFazPC)

π maker (FazLaptop)
```
![r5](https://user-images.githubusercontent.com/13461315/30946468-40e9a2d8-a3d2-11e7-8c43-c485d88bd304.png)

- **(6)** Encontrar os tamanhos de discos rígidos que ocorrem em dois ou mais PCs

```
π hd (
  σ oc ≥ 2 (
    γ hd, oc←count(hd) (PC)
  )
)
```
```sql
SELECT DISTINCT Hds.hd
FROM (
	SELECT hd, COUNT(hd) AS ocorrencia
	FROM PC
	GROUP BY hd
) AS Hds
WHERE Hds.ocorrencia >= 2
```
![r6](https://user-images.githubusercontent.com/13461315/30834736-82ced35a-a222-11e7-8e72-bbee7c5a42ca.png)

- **(7)** Encontre os pares de modelos de computadores que possuem a mesma velocidade e memória RAM. Cada par deve aparecer apenas uma vez; listar, por exemplo, (i, j), mas não (j, i)

```
A1 := π m1←model, s1←speed, r1←ram (PC)
A2 := ρ m2←m1, s2←s1, r2←r1 (A1)

B := (A1) ⨝ m1 ≠ m2 ∧ s1 = s2 ∧ r1 = r2 (A2)

Pares := π m1, m2 (B)
σ m1 < m2 (Pares)
```
![r7](https://user-images.githubusercontent.com/13461315/30833799-8263ff20-a21e-11e7-9c6c-4830a5cd5f2a.png)

- **(8)** Encontre os fabricantes de pelo menos dois diferentes tipos de computadores (PCs ou laptops) com velocidade de pelos menos 2.80

```
A := ( π maker, speed (Product ⨝ PC) ) ∪ ( π maker, speed (Product ⨝ Laptop) ) 

π maker ( σ speed ≥ 2.8 (A) )
```
![r8](https://user-images.githubusercontent.com/13461315/30786034-b79fa360-a13d-11e7-8568-a50824794376.png)


- **(9)** Encontre o(s) fabricante(s) do computador (PC ou laptop) com a maior velocidade disponível

```
Computador := (π speed, model (PC)) ∪ (π speed, model (Laptop))

-- mapear todos os fabricantes com os computadores
A := π maker, speed (Product ⨝ Computador)

-- cópia de A com os atributos 'maker' e 'speed' renomeados
B := ρ maker2←maker, speed2←speed (A)

-- deixar os maiores valores em 'speed2'
C := (A) ⨝ speed < speed2 (B)

-- deixar somente o maior valor de 'speed'
R := (π speed (A)) - (π speed (C))

-- deixar somente os fabricantes que possuem o maior valor em 'speed'
A ÷ R
```
![r9](https://user-images.githubusercontent.com/13461315/30835737-cee2c2ec-a227-11e7-95d3-79a5f40091fa.png)

- **(10)** Encontre os fabricantes de PCs com pelo menos três velocidades diferentes

```
A := π maker, speed (Product ⨝ PC)
B := γ maker, qtd_speed←count(speed) (A)

π maker ( σ qtd_speed ≥ 3 (B) )
```
![r10](https://user-images.githubusercontent.com/13461315/30836531-d449d73e-a22c-11e7-934f-5c78e8d79180.png)

- **(11)** Encontre os fabricantes que vendem exatamente três diferentes modelos de PC

```
A := γ maker, qtd_modelos←count(model) (Product)

σ qtd_modelos = 3 (A)
```
![r11](https://user-images.githubusercontent.com/13461315/30836747-26470466-a22e-11e7-8a25-5c69bdee16c3.png)