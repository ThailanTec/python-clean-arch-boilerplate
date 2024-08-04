from typing import Dict

from src.domain.services.users_finder import UsersFinder as UsersFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserFinder(UsersFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:

        if not first_name.isalpha():
            raise Exception('Nome invalido para busca')

        if len(first_name) > 18:
            raise Exception('Nome maior que o esperado para buscar')

        users = self.__users_repository.get_user(first_name)

        if users == []:
            raise Exception('Usuário não encontrado')

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }
        return response
