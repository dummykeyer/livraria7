from fastapi import Depends, FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="livraria7", description="Backend FastAPI gerado para livraria7")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/usuarios", response_model=list[schemas.UsuarioRead], tags=["Usuario"])
def list_usuario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_usuario(db, skip=skip, limit=limit)


@app.post("/api/usuarios", response_model=schemas.UsuarioRead, status_code=status.HTTP_201_CREATED, tags=["Usuario"])
def create_usuario(payload: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db, payload)


@app.get("/api/usuarios/{item_id}", response_model=schemas.UsuarioRead, tags=["Usuario"])
def get_usuario(item_id: int, db: Session = Depends(get_db)):
    return crud.get_usuario(db, item_id)


@app.put("/api/usuarios/{item_id}", response_model=schemas.UsuarioRead, tags=["Usuario"])
def update_usuario(item_id: int, payload: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    return crud.update_usuario(db, item_id, payload)


@app.delete("/api/usuarios/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Usuario"])
def delete_usuario(item_id: int, db: Session = Depends(get_db)):
    crud.delete_usuario(db, item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/api/listas", response_model=list[schemas.ListaRead], tags=["Lista"])
def list_lista(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_lista(db, skip=skip, limit=limit)


@app.post("/api/listas", response_model=schemas.ListaRead, status_code=status.HTTP_201_CREATED, tags=["Lista"])
def create_lista(payload: schemas.ListaCreate, db: Session = Depends(get_db)):
    return crud.create_lista(db, payload)


@app.get("/api/listas/{item_id}", response_model=schemas.ListaRead, tags=["Lista"])
def get_lista(item_id: int, db: Session = Depends(get_db)):
    return crud.get_lista(db, item_id)


@app.put("/api/listas/{item_id}", response_model=schemas.ListaRead, tags=["Lista"])
def update_lista(item_id: int, payload: schemas.ListaUpdate, db: Session = Depends(get_db)):
    return crud.update_lista(db, item_id, payload)


@app.delete("/api/listas/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Lista"])
def delete_lista(item_id: int, db: Session = Depends(get_db)):
    crud.delete_lista(db, item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/api/categorias", response_model=list[schemas.CategoriaRead], tags=["Categoria"])
def list_categoria(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_categoria(db, skip=skip, limit=limit)


@app.post("/api/categorias", response_model=schemas.CategoriaRead, status_code=status.HTTP_201_CREATED, tags=["Categoria"])
def create_categoria(payload: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.create_categoria(db, payload)


@app.get("/api/categorias/{item_id}", response_model=schemas.CategoriaRead, tags=["Categoria"])
def get_categoria(item_id: int, db: Session = Depends(get_db)):
    return crud.get_categoria(db, item_id)


@app.put("/api/categorias/{item_id}", response_model=schemas.CategoriaRead, tags=["Categoria"])
def update_categoria(item_id: int, payload: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    return crud.update_categoria(db, item_id, payload)


@app.delete("/api/categorias/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Categoria"])
def delete_categoria(item_id: int, db: Session = Depends(get_db)):
    crud.delete_categoria(db, item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/api/tarefas", response_model=list[schemas.TarefaRead], tags=["Tarefa"])
def list_tarefa(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_tarefa(db, skip=skip, limit=limit)


@app.post("/api/tarefas", response_model=schemas.TarefaRead, status_code=status.HTTP_201_CREATED, tags=["Tarefa"])
def create_tarefa(payload: schemas.TarefaCreate, db: Session = Depends(get_db)):
    return crud.create_tarefa(db, payload)


@app.get("/api/tarefas/{item_id}", response_model=schemas.TarefaRead, tags=["Tarefa"])
def get_tarefa(item_id: int, db: Session = Depends(get_db)):
    return crud.get_tarefa(db, item_id)


@app.put("/api/tarefas/{item_id}", response_model=schemas.TarefaRead, tags=["Tarefa"])
def update_tarefa(item_id: int, payload: schemas.TarefaUpdate, db: Session = Depends(get_db)):
    return crud.update_tarefa(db, item_id, payload)


@app.delete("/api/tarefas/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tarefa"])
def delete_tarefa(item_id: int, db: Session = Depends(get_db)):
    crud.delete_tarefa(db, item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
