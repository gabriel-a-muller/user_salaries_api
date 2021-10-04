# USER_SALARIES_API

Este projeto é uma API feita em Django-rest-framework e lida com operações CRUD (e mais algumas outras) para dois modelos.

O modelo de usuário é composto por cpf, nome e datade nascimento. Já o modelo dedados de salário armazena a data, o salárioe os descontos. As seguintes informações de usuário (global e individual) estão disponibilizadas via API, além das contidas na base de dados:

- A média dos salários
- A média dos descontos
- O maior salário
- O menor salário

## Installation

Crie um venv para o projeto

```
path/to/project/python virtualenv venv
```

Instale as dependencias
Use o [pip](https://pip.pypa.io/en/stable/) para instala-las.

```bash
pip install -r requirements.txt
```

Não esqueça de rodar as migrações para o banco de dados!

### Settings e DatabaseConfig

Com o objetivo de não publicar dados pessoais de banco de dados e ao mesmo tempo
obrigar o desenvolvedor a configurar o banco para uso da aplicação, é necessária a criação de
uma classe chamada DatabaseConfig com os seguintes parâmetros para setar na settings.py:

```
from .database_config import DatabaseConfig
DATABASES = {
    'default': {
        'ENGINE': DatabaseConfig.ENGINE,
        'NAME': DatabaseConfig.NAME,
        'HOST': DatabaseConfig.HOST,
        'PORT': DatabaseConfig.PORT,
        'USER': DatabaseConfig.USER,
        'PASSWORD': DatabaseConfig.PASSWORD,
    }
}
```

Sinta-se livre para utilizar outros backends. Desde que as migrações sejam compatíveis.
Neste projeto foi utilizado MySQL.

### Exemplo de DatabaseConfig:
```
class DatabaseConfig(object):
    ENGINE = 'django.db.backends.mysql'
    NAME = 'salary_manager'
    USER = 'root'
    PASSWORD = 'password'
    HOST = '127.0.0.1'
    PORT = '3306'
```



## Usage


### **api/v1/users/**
```
<id>/ -> Enviando o ID do usuário como parâmetro, retorna o usuário
create/ -> Cria um novo usuário
update/<id> -> Trabalha tanto com PUT e com PATCH.
delete/<id> -> Deleta a instância no backend
```
Campos necessários para o modelo:
```
{
    "cpf": [
        "String - CPF VÁLIDO!"
    ],
    "name": [
        "String"
    ],
    "born_date": 
        "YYYY-MM-DD"
}
```
### **api/v1/salary/**
```
<id>/ -> Enviando o ID do salário como parâmetro, retorna o salário
create/ -> Cria um novo salário
update/<id> -> Trabalha tanto com PUT e com PATCH.
delete/<id> -> Deleta a instância no backend
average_salary/ -> Retorna a média dos salários totais
average_discounts/ -> Retorna a média dos descontos totais
min/ -> Retorna o menor salário (instância)
max/ -> Retorna o maior salário (instância)
```
Campos necessários para o modelo:
```
{
    "user": [
        "Int"
    ],
    "salary": [
        "Float (MAIOR QUE O DESCONTO)"
    ],
    "discounts": [
        "Float (MENOR QUE O SALÁRIO)"
    ],
    "date": [
        "YYYY-MM-DD"
    ]
}
```

