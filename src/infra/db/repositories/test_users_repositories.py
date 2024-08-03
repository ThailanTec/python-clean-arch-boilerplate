import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repositories import UsersRepository

db_connection = DBConnectionHandler()
connection = db_connection.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    mocked_first_name = 'Nome'
    mocked_last_name = 'Sobrenome'
    mocked_age = 24

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql = '''
            SELECT * FROM users
            WHERE first_name='{}' AND
            last_name='{}' AND 
            age={}
        '''.format(mocked_first_name, mocked_last_name, mocked_age)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f'DELETE FROM users where id = {registry.id}'))
    connection.commit()
    print(registry)


@pytest.mark.skip(reason="Sensive test")
def test_get_user():
    mocked_first_name = 'Thailan'
    users_repository = UsersRepository()

    user = users_repository.get_user(mocked_first_name)

    assert user[0].first_name == mocked_first_name

    print(user)
