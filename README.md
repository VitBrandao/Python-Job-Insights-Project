# Requisitos Obrigatórios

## 1 - Implemente a função `read`
> **Implemente em:** src/jobs.py

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- A função deve receber um _path_ (uma string com o caminho para um arquivo).
- A função deve abrir o arquivo e ler seus conteúdos.
- A função deve tratar o arquivo como CSV.
- A função deve retornar uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.

<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  Se o conteúdo do arquivo for:
  
```
nome,cidade,telefone
Ana,Curitiba,1111111
Bernardo,Santos,999999
```

  O retorno da função deverá ser: 
  
```python
  [
    {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
    {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
  ]
```
</details> 

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando estas funções através do comando <code>python3 -i src/jobs.py</code> e invoque a função utilizando diferentes _paths_.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- A função abre o arquivo passado como parâmetro
- A função retorna uma lista de dicionários
- A função retorna a quantidade correta de itens na lista
- Nos dicionários retornados pela função, as chaves correspondem aos cabeçalhos do arquivo
</details>

## 2 - Implemente a função `get_unique_job_types`
> **Implemente em:** `src/insights.py`

Agora que temos como carregar os dados, podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

- A função deve receber o _path_ do arquivo csv com os dados.
- A função deve invocar a função `jobs.read` com o _path_ recebido para obter os dados.
- A função deve retornar uma lista de valores únicos presentes na coluna `job_type`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função desconsidera valores vazios
</details>

## 3 - Implemente a função `get_unique_industries`
> **Implemente em:** `src/insights.py`

Da mesma forma, agora iremos identificar quais indústrias estão representadas nesse conjunto de dados.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve retornar uma lista de valores únicos presentes na coluna `industry`.
- A função desconsidera valores vazios

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
</details>

## 4 - Implemente a função `get_max_salary`
> **Implemente em:** `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o maior salário presente na coluna `max_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna o valor correto
</details>

## 5 - Implemente a função `get_min_salary`
> **Implemente em:** `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o menor valor de todas as faixas.

- A função deve obter os dados da mesma forma que o requisito 2.
- A função deve ignorar os valores ausentes.
- A função deve retornar *um valor inteiro* com o menor salário presente na coluna `min_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função carrega os dados do arquivo recebido como parâmetro
- A função retorna o valor correto
</details>

## 6 - Implemente a função `filter_by_job_type`

> **Implemente em:** `src/insights.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar esse filtro.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `job_type` como segundo parâmetro.
- A função deve retornar uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função retorna os valores na ordem correta
- A função retorna uma lista vazia para `job_types` ausentes nos `jobs` recebidos
</details>

## 7 - Implemente a função `filter_by_industry`
> **Implemente em:** `src/insights.py`

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Vamos precisar implementar esse filtro também.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber uma string `industry` como segundo parâmetro.
- A função deve retornar uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função retorna os valores na ordem correta
- A função retorna uma lista vazia para `job_types` ausentes nos `jobs` recebidos
</details>

## 8 - Implemente a função `matches_salary_range`
> **Implemente em:** `src/insights.py`

O aplicativo vai precisar filtrar os empregos por salário também. Como uma função auxiliar, implemente `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- A função deve receber um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- A função deve retornar `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função retorna o booleano correto
- A função lança um `ValueError` se o valor de `min_salary` for maior que o valor de `max_salary`
- A função lança um `ValueError` se as chaves `min_salary` ou `max_salary` tiverem valores não numéricos
- A função lança um `ValueError` se o parâmetro `salary` tiver valor não numérico
- A função lança um `ValueError` se as chaves `min_salary` ou `max_salary` estiverem ausentes no dicionário
</details>

## 9 - Implemente a função `filter_by_salary_range`
> **Implemente em:** `src/insights.py`

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- A função deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- A função deve receber um inteiro `salary` como segundo parâmetro.
- A função deve ignorar os empregos com valores inválidos para `min_salary` ou `max_salary`.
- A função deve retornar uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- A função retorna a quantidade correta de valores
- A função retorna os valores corretos
- A função retorna os valores na ordem correta
- Empregos onde as chaves `min_salary` ou `max_salary` tiverem valores não numéricos devem ser ignorados
- Empregos onde o valor de `min_salary` for maior que o valor de `max_salary` devem ser ignorados
</details>

## 10 - Implemente um teste para a função `count_ocurrences`
> **Implemente em:** `tests/counter/test_counter.py`

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra *Python* e *Javascript* nos dados e, para isso, temos uma implementação pronta em `src/counter.py`. Durante o desenvolvimento, sofremos com alguns `bugs`, que já foram resolvidos. Para termos certeza e confiança da nossa entrega, no entanto, e não corrermos riscos, precisaremos de *testes automatizados* que garantam isso!

O nome deste teste **deve** ser `test_counter`, e ele deve garantir que atenda estas especificações:

- **Chamar** a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`src/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada.
- Garantir que a função retorna corretamente a quantidade de ocorrências da palavra solicitada 
  - A contagem de palavras deve ser _case insentitive_, ou seja, não diferenciar letras maiúsculas de minúsculas


<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendido quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code> ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O teste rejeita implementações que não retornam a quantidade de palavras corretamente.
- O teste aprova implementações corretas.
- Se o teste não é um falso positivo, ou seja, teste que passa sem realmente testar o código.

</details>
