import os
from typing import Optional, List

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

from bson import ObjectId
import asyncio
from pymongo import AsyncMongoClient
from pymongo import ReturnDocument

# ------------------------------------------------------------------------ #
#                         Inicialització de l'aplicació                    #
# ------------------------------------------------------------------------ #
app = FastAPI(
    title="Gestor de Pel·lícules API",
    summary="API REST amb FastAPI i MongoDB per gestionar informació de pel·lícules (Sprint 4)",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que cualquier web se conecte
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, PUT, DELETE
    allow_headers=["*"],
)
# ------------------------------------------------------------------------ #
#                   Configuració de la connexió amb MongoDB               #
# ------------------------------------------------------------------------ #
# Creem el client de MongoDB utilitzant la URL de connexió emmagatzemada
client = AsyncMongoClient(os.environ["MONGODB_URL"])

# Selecció de la base de dades i de la col·lecció
db = client.cinema
movie_collection = db.get_collection("movies")

# Definició de PyObjectId per als models Pydantic
PyObjectId = Annotated[str, BeforeValidator(str)]

# ------------------------------------------------------------------------ #
#                            Definició dels models                        #
# ------------------------------------------------------------------------ #
class MovieModel(BaseModel):
    """
    Model que representa una pel·lícula.
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    titol: str = Field(...)
    descripcio: str = Field(...)
    estat: str = Field(..., description="Estat de la pel·lícula: 'pendent de veure' o 'vista'")
    puntuacio: int = Field(..., ge=1, le=5)
    genere: str = Field(...)
    usuari: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "eixemple": {
                "titol": "El Padrino",
                "descripcio": "Història de la família criminal Corleone.",
                "estat": "vista",
                "puntuacio": 5,
                "genere": "Drama",
                "usuari": "jan06"
            }
        },
    )

class UpdateMovieModel(BaseModel):
    """
    Model per actualitzar una pel·lícula (tots els camps opcionals).
    """
    titol: Optional[str] = None
    descripcio: Optional[str] = None
    estat: Optional[str] = None
    puntuacio: Optional[int] = Field(None, ge=1, le=5)
    genere: Optional[str] = None
    usuari: Optional[str] = None

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

# ------------------------------------------------------------------------ #
#                                 Endpoints CRUD                          #
# ------------------------------------------------------------------------ #

# --- CREATE (Crear una pel·lícula) ---
@app.post("/movies/", response_description="Afegir nova pel·lícula", status_code=status.HTTP_201_CREATED, response_model=MovieModel)
async def create_movie(movie: MovieModel = Body(...)):
    new_movie = await movie_collection.insert_one(
        movie.model_dump(by_alias=True, exclude={"id"})
    )
    created_movie = await movie_collection.find_one({"_id": new_movie.inserted_id})
    return created_movie

# --- READ (Llistar totes les pel·lícules) ---
@app.get("/movies/", response_description="Llistar totes les pel·lícules", response_model=List[MovieModel])
async def list_movies(genere: Optional[str] = None):
    # Si l'usuari passa un gènere, filtrem. Si no, busquem tot.
    query = {}
    if genere:
        query["genere"] = genere
        
    movies = await movie_collection.find(query).to_list(1000)
    return movies

@app.get("/movies/{id}", response_description="Obtenir una pel·lícula per ID")
async def get_movie(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="El format de l'ID no és vàlid")
    movie = await db["movies"].find_one({"_id": ObjectId(id)})
    if movie is not None:
        movie["_id"] = str(movie["_id"])
        return movie
    raise HTTPException(status_code=404, detail="Pel·lícula no trobada")

# --- UPDATE (Actualitzar una pel·lícula) ---
@app.put("/movies/{id}", response_description="Actualitzar una pel·lícula", response_model=MovieModel)
async def update_movie(id: str, movie: UpdateMovieModel = Body(...)):
    movie_dict = {k: v for k, v in movie.model_dump().items() if v is not None}
    
    if len(movie_dict) >= 1:
        update_result = await movie_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": movie_dict},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Pel·lícula {id} no trobada")
            
    # Si no hi ha camps per actualitzar, retornem l'original
    existing_movie = await movie_collection.find_one({"_id": ObjectId(id)})
    if existing_movie is not None:
        return existing_movie
    raise HTTPException(status_code=404, detail=f"Pel·lícula {id} no trobada")

# --- DELETE (Eliminar una pel·lícula) ---
@app.delete("/movies/{id}", response_description="Eliminar una pel·lícula")
async def delete_movie(id: str):
    delete_result = await movie_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Pel·lícula {id} no trobada")
