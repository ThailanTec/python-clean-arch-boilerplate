from src.infra.db.tests.mock_users_repository import UsersRepositoryMock
from .user_finder import UserFinder


def test_user_finder_success():
    repo = UsersRepositoryMock()
    user_finder = UserFinder(repo)
    mock_firt_name = 'Tuliao'

    result = user_finder.find(mock_firt_name)

    assert repo.select_user_attribute['first_name'] == mock_firt_name
    assert result['type'] == 'Users'
    assert result['count'] == len(result['attributes'])
    assert result['attributes'] != []



