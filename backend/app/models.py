from sqlalchemy import Boolean, Date, DateTime, Float, ForeignKey, Integer, JSON, LargeBinary, Numeric, String, Text, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column("nome", String(255), nullable=False)
    email: Mapped[str] = mapped_column("email", String(255), nullable=False)
    senha_hash: Mapped[str] = mapped_column("senha_hash", String(255), nullable=False)
    criado_em: Mapped[datetime] = mapped_column("criado_em", DateTime, nullable=True)
    listas = relationship("Lista")
    categorias = relationship("Categoria")


class Lista(Base):
    __tablename__ = "listas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column("titulo", String(255), nullable=False)
    descricao: Mapped[str] = mapped_column("descricao", Text, nullable=True)
    criado_em: Mapped[datetime] = mapped_column("criado_em", DateTime, nullable=True)
    usuario_id: Mapped[int] = mapped_column("usuario_id", Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario")
    tarefas = relationship("Tarefa")


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column("nome", String(255), nullable=False)
    cor: Mapped[str] = mapped_column("cor", String(255), nullable=True)
    criado_em: Mapped[datetime] = mapped_column("criado_em", DateTime, nullable=True)
    usuario_id: Mapped[int] = mapped_column("usuario_id", Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario")
    tarefas = relationship("Tarefa")


class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column("titulo", String(255), nullable=False)
    descricao: Mapped[str] = mapped_column("descricao", Text, nullable=True)
    status: Mapped[str] = mapped_column("status", String(255), nullable=True)
    prioridade: Mapped[str] = mapped_column("prioridade", String(255), nullable=True)
    data_limite: Mapped[datetime] = mapped_column("data_limite", DateTime, nullable=True)
    concluida_em: Mapped[datetime] = mapped_column("concluida_em", DateTime, nullable=True)
    criado_em: Mapped[datetime] = mapped_column("criado_em", DateTime, nullable=True)
    atualizado_em: Mapped[datetime] = mapped_column("atualizado_em", DateTime, nullable=True)
    lista_id: Mapped[int] = mapped_column("lista_id", Integer, ForeignKey("listas.id"), nullable=False)
    categoria_id: Mapped[int] = mapped_column("categoria_id", Integer, ForeignKey("categorias.id"), nullable=True)
    lista = relationship("Lista")
    categoria = relationship("Categoria")
