# ANALISE
### O que é o software?
Um sistema de pedagio!

### Qual seu dominio?
Veiculos, operadores, placas, legalidade de veiculos, pista de pedagio, localização da pista

#### Requisitos funcionais
- Admin gerencia operadores, pistas, veiculos e transações
- Operador gerencia transações, sem poder edita-las ou remove-las
- O programa deve utilizar o fuso horario de Brasilia GMT -3

#### Requisitos não funcionais
- O programa deve ter uma interface simples e intuitiva

#### Entidades
- Admin
- Veiculo
- Pista de Pedagio
- Operador
- Transação

# PROJETO
## Quais tecnologias serão utilizadas?
- Linguagem: Python
- Bibliotecas: 
    - tkinter, para interface grafica
    - json, para comunicação com a persistencia de dados
    - mathplotlib
    - numpy

## Qual padrão de arquitetura?
- Arquitetura: MVC modificado (model, view, control e data)

## Praticas de programação
- O software é totalmente orientado a objeto.

#### Quais os padrões utilizados?
- Observer
- Singleton
- Strategy
- DAO (Data Acess Object)

# INSTRUÇÕES DE EXECUÇÃO
Para executar o programa, o usuário deve rodar o arquivo `main.py`. Certifique-se de que todas as dependências estão instaladas e configuradas corretamente.

```bash
python main.py

# BUGS CONHECIDOS