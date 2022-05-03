
![alt text](https://github.com/sebas1017/pokemon-app-challenge/blob/main/fastapi.png?raw=true)
![alt text](https://github.com/sebas1017/pokemon-app-challenge/blob/main/docker.jpeg?raw=true)
![alt text](https://github.com/sebas1017/pokemon-app-challenge/blob/main/react.png?raw=true)
POKEMON APP
#URL  https://github.com/sebas1017/pokemon-app-challenge
en esta app se tiene un dasboard con tarjetas de pokemones 
con nombre del pokemon, descripcion , y un boton VER HABILIDADES.

estos datos son recolectados de la API publica HTTPS://POKEAPI.CO/API/V2/

he construido el frontend en un contenedor usando docker , y  react
para el backend he optado por FastAPI y Python tambien dockerizado


cada servicio tiene un dockerfile que permite crear un container a partir de este archivo

para construir un contenedor del backend ejecutamos lo siguiente:

```
cd backend-pokemon-app/backend
docker build -t backend_pokemon .

```




este comando debe ser ejecutado en la raiz del directorio backend-pokemon-app/backend  ya que el . indica que el dockerfile se encuentra ahi.

una vez echo esto se crea un contenedor a partir de la imagen construida anteriormente


```
docker run -p 8000:8000 backend_pokemon
```

y luego podra ir a la ruta http://localhost:8000 y ver la API funcionando, para
obtener documentacion de la api vaya a la ruta http://localhost:8000/docs


este proceso se debe seguir para desplegar el frontend en un container por separado

este comando debe ser ejecutado en la raiz del directorio frontend-pokemon-app/poke-react   ya que el . indica que el dockerfile se encuentra ahi.

```
docker build -t frontend_pokemon .
```

una vez echo esto se crea un contenedor a partir de la imagen construida anteriormente

```
docker run -p 3000:3000 frontend_pokemon
```

y podra ir a la ruta http://localhost:3000 y podra ver el sitio web
el cual internamente se conecta a la API que previamente ya se desplego en un container aparte y tiene expuesto el puerto 8000

Para el frontend en la ruta frontend-pokemon-app/poke-react
se encuentra el archivo .env el cual contiene 2 variables de entorno que indican
el entorno en que se quiere ejecutar ya que esta forma de crear los containers
por separado fue necesaria para desplegar el proyecto en heroku de forma gratuita el cual no acepta docker-compose

para desplegar en heroku debe tener una cuenta creada y ejecutar los siguientes comandos:
    
    BACKEND:
    ubicarse en la ruta backend-pokemon-app/backend al nivel del Dockerfile y ejecutar:
        heroku login
        heroku container:login
        heroku create backend-app-myapp-poke  #o el nombre que desee
        heroku container:push web -a backend-app-myapp-poke
        heroku container:release web -a backend-app-myapp-poke  #esto despliega

    FRONTEND:
    ubicarse en la ruta frontend-pokemon-app/poke-react al nivel del Dockerfile y ejecutar:
        heroku login
        heroku container:login
        heroku create frontend-app-myapp-poke  #o el nombre que desee
        heroku container:push web -a frontend-app-myapp-poke
        heroku container:release web -a frontend-app-myapp-poke  #esto despliega


y con esto obtendremos en 2 servidores distintos el frontend y el backend
si por otro lado se desea ejecutar localmente en 2 containers pero en la misma maquina entonces hacer uso de la configuracion de docker-compose de la siguiente manera:


en la ruta frontend-pokemon-app/poke-react/components en el archivo PokeCard.js
reemplazar process.env.REACT_APP_URL_PRODUCTION por process.env.REACT_APP_URL_DEVELOPMENT

y en la ruta ruta frontend-pokemon-app/poke-react/src/App.js 
reemplazar process.env.REACT_APP_URL_PRODUCTION 
por process.env.REACT_APP_URL_DEVELOPMENT

esto hara que el frontend se comunique al servicio expuesto en docker-compose y no al desplegado en heroku, ya que desea ejecutarlo localmente

esto solo se requiere para el frontend luego debe ubicarse en la raiz del proyecto al nivel del docker-compose.yml

REQUISITOS:
tener instalado docker y docker-compose

una vez teniendo estas herramientas ejecutar
```
docker-compose up -d
```

y cuando finalice el proceso ir a la ruta http://localhost:3000 y obtendra el sitio web el cual esta comunicandose con el container del puerto  8000 de la api pero esta vez los containers estan siendo gestionados por docker-compose

gracias!!
