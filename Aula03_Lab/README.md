# Repositório da 3 aula de Processamento de Imagem

## Comandos de inicio de projeto 
* Criando maquina virtual:
```javascript
python -m venv venv
```

* python -m pip install --upgrade pip

## Comandos de geração de requerimentos do projeto
pip install pipreqs
pip freeze > requirements.txt
pip install -r requirements.txt

pip install scikit-image
pip install matplotlib 

## docker file ainda nã funciona

docker build -f Dockerfile -t venv .
docker run 