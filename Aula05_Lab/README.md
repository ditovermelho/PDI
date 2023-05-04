# Repositório da 5 aula de Processamento de Imagem
__Filtragem no domínio da Frequência__

__Objetivos:__
1. Compreender na prática o comportamento da DFT, por meio do algoritmo FFT.
2. Compreender na prática o conceito de Filtragem de Imagens.
3. Compreender que a convolução no tempo equivale a um produto na frequência.
4. Implementar filtros no domínio da frequência.

Questões estão comentadas em cada código do projeto.

## Comandos de inicio de projeto 
* Criando maquina virtual:
```javascript
python -m venv venv
```

* Atualização do pip da venv:
```javascript
python -m pip install --upgrade pip
```

## Comandos de geração de requerimentos do projeto
* Pipreqs:
```javascript
pip install pipreqs
```
Essa biblioteca permite criar o arquivo de requerimento do projeto, puxando apenas as dependências do projeto. A única dependência 
desse pacote e, que todos os arquivos estejam dentro de uma pasta. 

No nosso caso:
```javascript
pipreqs ./pythonfile
```
ou para forçar a criação:
```javascript
pipreqs --force ./pythonfile
```
O pipreqs ira ler todos os arquivos da pasta e identificara todos 
os pacotes necessários para o projeto. Assim, é preciso prestar atenção aos pacotes que não são invocados mas são necessários para o projeto, como o lxml para quem usa BeutifulSoup. fonte: https://medium.com/pyladiesbh/requirements-em-python-ec88b42058a6.

* Freeze:
```javascript
pip freeze > requirements.txt
```
O pacote freeze ira criar os requerimentos do projeto com base nas bibliotecas instaladas no ambiente.

* Instalação dos requerimentos:
```javascript
pip install -r requirements.txt
```
basta digitar o comando acima no CMD.

