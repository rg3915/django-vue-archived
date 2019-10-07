# django-vue

Este projeto usa o VueJS apenas como arquivos estáticos do Django.

## Como rodar o projeto?

Em Dev rodar dois servidores, back e front.
Depois fazer `npm run build` para gerar os arquivos pra rodar somente com Django.

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-vue.git
cd django-vue
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Frontend

```
cd frontend
npm run build
npm run serve
```

## Comandos

```
nvm use 11
vue create frontend
cd frontend

cat << EOF > vue.config.js
module.exports = {
  outputDir: '../myproject/core/templates',
  assetsDir: 'static'
}
EOF

npm run serve
npm run build
```