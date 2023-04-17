# Repositório da 4 aula de Processamento de Imagem
__Filtragem no domínio espacial__

__Objetivos:__
1. Compreender na prática o conceito de Filtragem de Imagens.
2. Compreender a convolução como operação fundamental em PI.
3. Implementar filtros no domínio espacial por meio da convolução com máscaras e pelo uso de bibliotecas.
4. Implementar filtros com o objetivo de detectar bordas.
5. Implementar filtros com o objetivo de reduzir ruídos.

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

## docker file ainda não funciona
```javascript
docker build -f Dockerfile -t venv .
```

```javascript
docker run 
```
