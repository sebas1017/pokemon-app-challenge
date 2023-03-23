#!/usr/bin/python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os 
import uvicorn
import asyncio
import aiohttp
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


app = FastAPI()

app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pokemons = list(map(lambda x: x.lower(),["SPEAROW", "FEAROW", "EKANS", "ARBOK", "PIKACHU",
"RAICHU", "SANDSHREW", "SANDSLASH", "NIDORINA"]))



@app.get("/")
async def root( ):
    return {"message":"Bienvenido a POKE-API construida en FASTAPI"}



async def fetch(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            data_response = response.json()
            return await data_response
    return {}


@app.get("/api/v1/all_pokemons", status_code=200)
async def all_pokemons():
    results = []
    try:
        async with aiohttp.ClientSession() as session:
            for pokemon in pokemons:
                task_pokemon = asyncio.create_task( fetch(session, f"https://pokeapi.co/api/v2/pokemon/{pokemon}"))
                task_description = asyncio.create_task( fetch(session, f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}"))
                response_pokemon, response_description = await asyncio.gather(task_pokemon, task_description)
                
                if response_description:
                    description_pokemon = response_description["flavor_text_entries"][0]["flavor_text"]
                    data_final = {
                        "name": response_pokemon["name"],
                        "sprites": {
                            "front_default": response_pokemon["sprites"]["front_default"],
                            "back_default": response_pokemon["sprites"]["back_default"],
                        },
                        "description": description_pokemon,
                    }
                else:
                    data_final = {}
                results.append(data_final)
            return {"results": results}
    except Exception as e:
        logger.error(f"Exception in function get_all_pokemons -> {e}")
        raise HTTPException(status_code=500, detail="Error interno en el servidor")
       

@app.get("/api/v1/names_abilities/{pokemon}", status_code=200)
async def names_abilities(pokemon: str):
    results=[]
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    try:
        data = requests.get(url)
        if data.status_code==200:
            for result in data.json()["abilities"]:
                results.append(result["ability"]["name"])
            return {"results":results}
        if data.status_code == 404:
            raise HTTPException(status_code=404, detail="el pokemon solicitado no existe")
        else:
            return {"message":"servidor no disponible en este momento"}
    except Exception as e:
        logger.error(f"Exception in function names_abilities -> {e}")
        raise HTTPException(status_code=500, detail="Error interno en el servidor")

if __name__=="__main__":
    port = int(os.getenv("PORT") or 8000)
    uvicorn.run("main:app",host='0.0.0.0',port=port ,reload=True)