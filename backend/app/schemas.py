from datetime import date, datetime, time
from decimal import Decimal
from typing import Any
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, EmailStr, Field


class UsuarioBase(BaseModel):
    nome: str = Field(..., max_length=100, validation_alias=AliasChoices("nome", "nome"), serialization_alias="nome")
    email: str = Field(..., max_length=150, validation_alias=AliasChoices("email", "email"), serialization_alias="email")
    senhaHash: str = Field(..., max_length=255, validation_alias=AliasChoices("senhaHash", "senha_hash"), serialization_alias="senhaHash")


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(BaseModel):
    nome: str | None = None
    email: str | None = None
    senhaHash: str | None = None


class UsuarioRead(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    nome: str = Field(..., max_length=100, validation_alias=AliasChoices("nome", "nome"), serialization_alias="nome")
    email: str = Field(..., max_length=150, validation_alias=AliasChoices("email", "email"), serialization_alias="email")
    senhaHash: str = Field(..., max_length=255, validation_alias=AliasChoices("senhaHash", "senha_hash"), serialization_alias="senhaHash")
    criadoEm: datetime | None = Field(None, validation_alias=AliasChoices("criadoEm", "criado_em"), serialization_alias="criadoEm")


class ListaBase(BaseModel):
    titulo: str = Field(..., max_length=120, validation_alias=AliasChoices("titulo", "titulo"), serialization_alias="titulo")
    descricao: str | None = Field(None, validation_alias=AliasChoices("descricao", "descricao"), serialization_alias="descricao")
    usuarioId: int = Field(..., validation_alias=AliasChoices("usuarioId", "usuario_id"), serialization_alias="usuarioId")


class ListaCreate(ListaBase):
    pass


class ListaUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    usuarioId: int | None = None


class ListaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    titulo: str = Field(..., max_length=120, validation_alias=AliasChoices("titulo", "titulo"), serialization_alias="titulo")
    descricao: str | None = Field(None, validation_alias=AliasChoices("descricao", "descricao"), serialization_alias="descricao")
    criadoEm: datetime | None = Field(None, validation_alias=AliasChoices("criadoEm", "criado_em"), serialization_alias="criadoEm")
    usuarioId: int = Field(..., validation_alias=AliasChoices("usuarioId", "usuario_id"), serialization_alias="usuarioId")


class CategoriaBase(BaseModel):
    nome: str = Field(..., max_length=80, validation_alias=AliasChoices("nome", "nome"), serialization_alias="nome")
    cor: str | None = Field(None, max_length=7, validation_alias=AliasChoices("cor", "cor"), serialization_alias="cor")
    usuarioId: int = Field(..., validation_alias=AliasChoices("usuarioId", "usuario_id"), serialization_alias="usuarioId")


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nome: str | None = None
    cor: str | None = None
    usuarioId: int | None = None


class CategoriaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    nome: str = Field(..., max_length=80, validation_alias=AliasChoices("nome", "nome"), serialization_alias="nome")
    cor: str | None = Field(None, max_length=7, validation_alias=AliasChoices("cor", "cor"), serialization_alias="cor")
    criadoEm: datetime | None = Field(None, validation_alias=AliasChoices("criadoEm", "criado_em"), serialization_alias="criadoEm")
    usuarioId: int = Field(..., validation_alias=AliasChoices("usuarioId", "usuario_id"), serialization_alias="usuarioId")


class TarefaBase(BaseModel):
    titulo: str = Field(..., max_length=150, validation_alias=AliasChoices("titulo", "titulo"), serialization_alias="titulo")
    descricao: str | None = Field(None, validation_alias=AliasChoices("descricao", "descricao"), serialization_alias="descricao")
    status: str | None = Field(None, max_length=20, validation_alias=AliasChoices("status", "status"), serialization_alias="status")
    prioridade: str | None = Field(None, max_length=20, validation_alias=AliasChoices("prioridade", "prioridade"), serialization_alias="prioridade")
    dataLimite: datetime | None = Field(None, validation_alias=AliasChoices("dataLimite", "data_limite"), serialization_alias="dataLimite")
    concluidaEm: datetime | None = Field(None, validation_alias=AliasChoices("concluidaEm", "concluida_em"), serialization_alias="concluidaEm")
    listaId: int = Field(..., validation_alias=AliasChoices("listaId", "lista_id"), serialization_alias="listaId")
    categoriaId: int | None = Field(None, validation_alias=AliasChoices("categoriaId", "categoria_id"), serialization_alias="categoriaId")


class TarefaCreate(TarefaBase):
    pass


class TarefaUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    status: str | None = None
    prioridade: str | None = None
    dataLimite: datetime | None = None
    concluidaEm: datetime | None = None
    listaId: int | None = None
    categoriaId: int | None = None


class TarefaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    id: int
    titulo: str = Field(..., max_length=150, validation_alias=AliasChoices("titulo", "titulo"), serialization_alias="titulo")
    descricao: str | None = Field(None, validation_alias=AliasChoices("descricao", "descricao"), serialization_alias="descricao")
    status: str | None = Field(None, max_length=20, validation_alias=AliasChoices("status", "status"), serialization_alias="status")
    prioridade: str | None = Field(None, max_length=20, validation_alias=AliasChoices("prioridade", "prioridade"), serialization_alias="prioridade")
    dataLimite: datetime | None = Field(None, validation_alias=AliasChoices("dataLimite", "data_limite"), serialization_alias="dataLimite")
    concluidaEm: datetime | None = Field(None, validation_alias=AliasChoices("concluidaEm", "concluida_em"), serialization_alias="concluidaEm")
    criadoEm: datetime | None = Field(None, validation_alias=AliasChoices("criadoEm", "criado_em"), serialization_alias="criadoEm")
    atualizadoEm: datetime | None = Field(None, validation_alias=AliasChoices("atualizadoEm", "atualizado_em"), serialization_alias="atualizadoEm")
    listaId: int = Field(..., validation_alias=AliasChoices("listaId", "lista_id"), serialization_alias="listaId")
    categoriaId: int | None = Field(None, validation_alias=AliasChoices("categoriaId", "categoria_id"), serialization_alias="categoriaId")
