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
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Frontend

```
cd frontend
npm run build  # para gerar o build
npm run serve  # para rodar o servidor
```

## Comandos pra criar o projeto do zero

```
# Criando o projeto Django
python -m venv .venv
source .venv/bin/activate
pip install -U pip; pip install django python-decouple
django-admin startproject myproject .
cd myproject
python ../manage.py startapp core
cd ..
# Criando uma pasta chamada contrib com um env_gen.py
git clone https://gist.github.com/22626de522f5c045bc63acdb8fe67b24.git /tmp/contrib; if [ ! -d contrib ]; then mkdir contrib; fi; cp /tmp/contrib/env_gen.py contrib/
python contrib/env_gen.py
```

Em `settings.py` insira `'myproject.core',` em `INSTALLED_APPS`.

Se você mudar a pasta default dos estáticos, então faça:

```
# opcional
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'myproject/core/templates/static/',
]
```

Depois entre na pasta

```
cd myproject/core/
```

e faça:

```
cat << EOF > views.py
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
EOF
```

```
cd ..
cat << EOF > core/urls.py
from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
]
EOF
```

```
cat << EOF > urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myproject.core.urls')),
    path('admin/', admin.site.urls),
]
EOF
```

### Frontend

```
cd ..
nvm use 11
vue create frontend
cd frontend
```

Arquivo de configuração

```
cat << EOF > vue.config.js
module.exports = {
  outputDir: '../myproject/core/templates',
  assetsDir: '../static'
}
EOF
```

```
npm run build  # para gerar o build
npm run serve  # para rodar o servidor
```

Rodando o servidor Django

```
cd ..
python manage.py runserver
```
