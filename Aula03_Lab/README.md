# Repositório da 3 aula de Processamento de Imagem
Conceito de Realce de imagens, Histograma, Equalização de Histograma, Métodos de Binarização, Transformação de Intensidades
Objetivos:
1. Compreender na prática o conceito de Realce de Imagens.
2. Visualizar Histograma de imagens.
3. Implementar o realce de Imagens utilizando equalização de Histogramas.
4. Implementar a binarização de imagens por diferentes método.

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

## docker file ainda nã funciona
```javascript
docker build -f Dockerfile -t venv .
```

```javascript
docker run 
```
