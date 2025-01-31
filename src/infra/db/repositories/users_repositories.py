from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UserEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from typing import List
import random


class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:  # Melhorar geração de ID
                new_registry = UserEntity(id=random.randint(1, 1000), first_name=first_name,
                                          last_name=last_name,
                                          age=age)
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def get_user(cls, first_name=str) -> List[Users]:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session
                    .query(UserEntity)
                    .filter(UserEntity.first_name == first_name)
                    .all()
                    )
                print("TIPOOOOO", type(users))
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception
