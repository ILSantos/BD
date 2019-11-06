# Parte I

Verificar alguns parâmetros do hardware e do software que vamos utilizar

## Tarefa I.1

Identificar o sistema que será usado para os experimentos incluindo informações sobre o hardware e o SO utilizado. Sobre o hardware, incluir informações como marca, modelo, número de série, tipo de processador, quantidade de memória RAM, tamanho do disco. Devem também ser apresentadas informações sobre as caches existentes. Sobre o SO, que deve ser Linux, incluir informações sobre qual a distribuição usada, versão do sistema, versão do Kernel, etc.

### Resposta

Sobre o hardware:

- **Marca**:
- **Modelo**:
- **Número de Série**:
- **Tipo de Processador**:
- **Quantidade de Memória RAM:**
- **Tamanho do Disco**:
- **Caches existentes**:

Sobre o SO Linux:

- **Distribuição**:
- **Versão do sistema**:
- **Versão do Kernel**:

****CheatSheet****

- Para obter informações sobre o processador:
  - `lscpu`
  - `hwinfo --short`
- Para listar o hardware:
  - `lshw -short`
- Dispositivos PCI podem ser listados com:
  - `lscpu`
- Para obter lista de dispositivos SATA e SCSI:
  - `lsscsi`
- Dispositivos USB:
  - `lscpu`
- Para obter de forma organizada e colorida várias informações:
  - `inxi -Fxxx`
  - `inxi -F`

## Tarefa I.2

1. Verifique no disco que será usado para os experimentos no laboratório os seguintes parâmetros: Nr de superfícies, cilindros, setores por trilha, velocidade de rotação, latência rotacional; tempos de seek médio, máximo e mínimo; tempo para a próxima trilha; e taxa de transferência.
2. Utilizando o comando `hdparm` do Linux, verifique os parâmetros dos parâmetros de SO que serão utilizados para o disco.
3. Verifique o tamanho do bloco utilizado

### Resposta

- Informações detalhadas do disco: `hdparm -I /dev/sda`
- Mede velocidade de leitura do disco: `sudo hdparm -t /dev/sda`
- Mede velocidade de leitura do cache: `sudo hdparm -T /dev/sda`
- Ativa leitura antecipada: `sudo hdparm -A1 /dev/sda`
- 

## Tarefa I.3

Analisar e descrever os detalhes dos seguintes sistemas de arquivos disponíveis no Linux: Ext2, Ext3, ReiserFS e XFS. Construir uma tabela comparativa das principais características de cada um dos dois sistemas.

### Resposta

- Ext2: primeiro sistema de arquivos a suportar atributos de arquivo estendidos e 2 unidades de terabyte. Não possui suporte ao journaling.
- Ext3: é um Ext2 com suporte journaling
- ReiserFS: criado recentemente, sua performance é muito boa, principalmente para um número muito grande de arquivos pequenos. Possui suporte a journaling
- XFS: possui suporte a journaling. É considerado um dos melhores sistemas de arquivos para banco de dados, pois é muito rápido na gravação. XFS utiliza muitos recursos de cache com memória RAM, e para utilizar XFS é recomendado utilizar sistemas que possuem redundância de energia.