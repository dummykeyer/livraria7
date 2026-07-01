from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas


def list_usuario(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()


def get_usuario(db: Session, item_id: int):
    item = db.get(models.Usuario, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return item


def create_usuario(db: Session, payload: schemas.UsuarioCreate):
    data = {
        "nome": payload.nome,
        "email": payload.email,
        "senha_hash": payload.senhaHash,
    }
    item = models.Usuario(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_usuario(db: Session, item_id: int, payload: schemas.UsuarioUpdate):
    item = get_usuario(db, item_id)
    data = payload.model_dump(exclude_unset=True)
    if "nome" in data:
        item.nome = data["nome"]
    if "email" in data:
        item.email = data["email"]
    if "senhaHash" in data:
        item.senha_hash = data["senhaHash"]
    db.commit()
    db.refresh(item)
    return item


def delete_usuario(db: Session, item_id: int):
    item = get_usuario(db, item_id)
    db.delete(item)
    db.commit()
    return None


def list_lista(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lista).offset(skip).limit(limit).all()


def get_lista(db: Session, item_id: int):
    item = db.get(models.Lista, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Lista not found")
    return item


def create_lista(db: Session, payload: schemas.ListaCreate):
    data = {
        "titulo": payload.titulo,
        "descricao": payload.descricao,
        "usuario_id": payload.usuarioId,
    }
    item = models.Lista(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_lista(db: Session, item_id: int, payload: schemas.ListaUpdate):
    item = get_lista(db, item_id)
    data = payload.model_dump(exclude_unset=True)
    if "titulo" in data:
        item.titulo = data["titulo"]
    if "descricao" in data:
        item.descricao = data["descricao"]
    if "usuarioId" in data:
        item.usuario_id = data["usuarioId"]
    db.commit()
    db.refresh(item)
    return item


def delete_lista(db: Session, item_id: int):
    item = get_lista(db, item_id)
    db.delete(item)
    db.commit()
    return None


def list_categoria(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Categoria).offset(skip).limit(limit).all()


def get_categoria(db: Session, item_id: int):
    item = db.get(models.Categoria, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return item


def create_categoria(db: Session, payload: schemas.CategoriaCreate):
    data = {
        "nome": payload.nome,
        "cor": payload.cor,
        "usuario_id": payload.usuarioId,
    }
    item = models.Categoria(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_categoria(db: Session, item_id: int, payload: schemas.CategoriaUpdate):
    item = get_categoria(db, item_id)
    data = payload.model_dump(exclude_unset=True)
    if "nome" in data:
        item.nome = data["nome"]
    if "cor" in data:
        item.cor = data["cor"]
    if "usuarioId" in data:
        item.usuario_id = data["usuarioId"]
    db.commit()
    db.refresh(item)
    return item


def delete_categoria(db: Session, item_id: int):
    item = get_categoria(db, item_id)
    db.delete(item)
    db.commit()
    return None


def list_tarefa(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarefa).offset(skip).limit(limit).all()


def get_tarefa(db: Session, item_id: int):
    item = db.get(models.Tarefa, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Tarefa not found")
    return item


def create_tarefa(db: Session, payload: schemas.TarefaCreate):
    data = {
        "titulo": payload.titulo,
        "descricao": payload.descricao,
        "status": payload.status,
        "prioridade": payload.prioridade,
        "data_limite": payload.dataLimite,
        "concluida_em": payload.concluidaEm,
        "lista_id": payload.listaId,
        "categoria_id": payload.categoriaId,
    }
    item = models.Tarefa(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_tarefa(db: Session, item_id: int, payload: schemas.TarefaUpdate):
    item = get_tarefa(db, item_id)
    data = payload.model_dump(exclude_unset=True)
    if "titulo" in data:
        item.titulo = data["titulo"]
    if "descricao" in data:
        item.descricao = data["descricao"]
    if "status" in data:
        item.status = data["status"]
    if "prioridade" in data:
        item.prioridade = data["prioridade"]
    if "dataLimite" in data:
        item.data_limite = data["dataLimite"]
    if "concluidaEm" in data:
        item.concluida_em = data["concluidaEm"]
    if "listaId" in data:
        item.lista_id = data["listaId"]
    if "categoriaId" in data:
        item.categoria_id = data["categoriaId"]
    db.commit()
    db.refresh(item)
    return item


def delete_tarefa(db: Session, item_id: int):
    item = get_tarefa(db, item_id)
    db.delete(item)
    db.commit()
    return None
