from typing import Dict

from src.domain.services.users_finder import UsersFinder as UsersFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserFinder(UsersFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        pass
