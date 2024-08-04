from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from typing import List


class UsersRepositoryMock(UsersRepositoryInterface):

    def __init__(self) -> None:
        self.insert_user_attribute = {}
        self.select_user_attribute = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attribute["first_name"] = first_name
        self.insert_user_attribute["last_name"] = last_name
        self.insert_user_attribute["age"] = age
        return

    def get_user(self, first_name=str) -> List[Users]:
        self.select_user_attribute["first_name"] = first_name
        return [
            Users(1, first_name, 'Testes', 56),
            Users(2, first_name, 'Testei', 56)
        ]
