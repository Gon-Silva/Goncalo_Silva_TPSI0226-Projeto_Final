# 🎬 Random Play

**Random Play** é um sistema de gestão de locadoras de filmes desenvolvido em Python, com interface em linha de comandos (CLI). Permite gerir clientes, funcionários, filmes, alugueres e planos de subscrição, assim como visualizar estatísticas da locadura.

---

## 📋 Funcionalidades

### Primeiro Arranque
- Configuração inicial da locadura (nome, email, localização, telefone)
- Criação automática do administrador (owner)

### Autenticação
- Login com email e password
- Distinção automática entre clientes e funcionários pelo domínio do email
- Registo de novas contas de cliente

### Gestão (Owner)
- Gerir clientes — listar, pesquisar, editar, remover (soft delete)
- Gerir funcionários — listar, pesquisar, editar, remover (soft delete)
- Gerir filmes — adicionar, editar, remover
- Gerir planos de subscrição
- Ver estatísticas — filmes mais alugados, clientes ativos, receita
- Editar dados da locadura

### Gestão (Employee)
- Gerir filmes — adicionar, editar
- Ver lista de clientes
- Registar devoluções de filmes
- Editar conta própria

### Área do Cliente
- Ver catálogo de filmes com disponibilidade em tempo real
- Filtrar filmes por nome, género, diretor, ano
- Alugar filmes
- Avaliar filmes (1-5 estrelas) e comentar
- Votar em comentários de outros utilizadores
- Editar conta ou solicitar eliminação (soft delete)

### Algoritmos Implementados
**Pesquisa:**
- Pesquisa linear — por nome, email
- Pesquisa binária — por ID (em dados ordenados)

**Ordenação** (com escolha de campo e ordem crescente/decrescente):
- Bubble Sort
- Quick Sort

**Estatísticas:**
- Total de clientes ativos/inativos
- Distribuição por plano de subscrição
- Filmes mais alugados
- Cópias disponíveis por filme (calculado dinamicamente)

---

## 🗂️ Estrutura do Projeto

```
Random_Play/
│
├── main.py                  # Ponto de entrada do programa
├── config.py                # Caminhos e regex centralizados
│
├── DataBase/                # Dados persistentes (JSON)
│   ├── statement.json
│   ├── subscription_plans.json
│   ├── Client/
│   ├── Employees/
│   ├── Movies/
│   ├── Rentals/
│   └── Comment/
│
└── Code/                    # Lógica do programa
    ├── Headers/             # Cabeçalhos de apresentação
    ├── Setup/               # Configuração inicial da locadura
    ├── NewAccount/          # Criação de contas
    ├── Login/               # Autenticação
    ├── Home/
    │   ├── Client/          # Página inicial do cliente
    │   └── Employee/        # Página inicial do funcionário
    ├── Management/
    │   ├── Movies/          # Gestão de filmes
    │   ├── Employees/       # Gestão de funcionários
    │   ├── Client/          # Gestão de clientes
    │   └── Plans/           # Gestão de planos
    └── GenericUtils/        # Utilitários partilhados
        ├── files.py         # Leitura/escrita de JSON
        ├── algorithms.py    # Ordenação e pesquisa
        ├── inputs.py        # Inputs com validação
        ├── terminal.py      # cls, press_to_continue
        └── errors.py        # Tratamento de erros
```

---

## ⚙️ Requisitos

- Python 3.14.5 ou superior
- Sem dependências externas — apenas bibliotecas standard do Python:
  - `json`
  - `os`
  - `re`
  - `datetime`

---

## 🚀 Instalação e Execução

**1. Clonar o repositório:**
```bash
git clone https://github.com/Gon-Silva/Goncalo_Silva_TPSI0226-Projeto_Final.git
cd Goncalo_Silva_TPSI0226-Projeto_Final
```

**2. Executar o programa:**
```bash
python main.py
```

> ⚠️ Corre sempre o `main.py` a partir da raiz do projeto (`Random_Play/`), caso contrário os caminhos dos ficheiros JSON não serão encontrados.

**3. Primeiro arranque:**

Na primeira execução, o programa irá guiar-te pela configuração inicial da locadura e criação do administrador. Os dados ficam guardados automaticamente em `DataBase/statement.json`.

---

## 💾 Persistência de Dados

Os dados são guardados em ficheiros JSON organizados por entidade. Cada entidade tem o seu próprio ficheiro, com um campo `next_id` para garantir IDs únicos mesmo após remoções.

```json
{
  "next_id": 4,
  "clients": [...]
}
```

Os comentários dos filmes ficam em ficheiros individuais por filme:
```
DataBase/Comment/1.json   ← comentários do filme com id 1
DataBase/Comment/2.json   ← comentários do filme com id 2
```

---

## 👤 Autor

**Gonçalo Silva** — TPSI0226  
Projeto Final — Python
