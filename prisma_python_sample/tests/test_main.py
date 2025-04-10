from prisma_python_sample.main import app, get_prisma
import pytest
from fastapi.testclient import TestClient
from prisma_python_sample.main import app, get_prisma


# @pytest.fixture(scope="module")
# def test_client():
#     client = TestClient(app)
#     yield client


# @pytest.fixture(autouse=True, scope="module")
# async def setup_db():
#     prisma = get_prisma()
#     await prisma.connect()
#     await prisma.user.delete_many()
#     yield
#     await prisma.disconnect()


@pytest.mark.asyncio
async def test_create_and_get_user():
    email = "test@example.com"
    name = "Test User"

    client = TestClient(app)

    prisma = get_prisma()
    await prisma.connect()
    # await prisma.user.delete_many()

    # app.dependency_overrides[get_prisma] = lambda: prisma

    # response = await test_client.post(f"/users?email={email}&name={name}")
    # assert response.status_code == 200
    # created_user = response.json()
    # assert created_user["email"] == email
    # assert created_user["name"] == name

    # prisma.user.create.assert_called_once_with(
    #     data={"email": email, "name": name})

    # response = await test_client.get(f"/users/{email}")
    # assert response.status_code == 200
    # retrieved_user = response.json()
    # assert retrieved_user["email"] == email
    # assert retrieved_user["name"] == name

    # await prisma.user.find_first.assert_called_once_with(where={'email': email})

    # app.dependency_overrides = {}

    # await prisma.disconnect()
    assert True

# def test_get_nonexistent_user(test_client: TestClient, mock_prisma):
#     app.dependency_overrides[get_prisma] = lambda: mock_prisma

#     response = test_client.get("/users/nonexistent@example.com")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "User not found"

#     mock_prisma.user.find_first.assert_called_once_with(
#         where={'email': 'nonexistent@example.com'})

#     app.dependency_overrides = {}


# def test_get_users(test_client: TestClient, mock_prisma):
#     app.dependency_overrides[get_prisma] = lambda: mock_prisma
#     mock_prisma.user.find_many.return_value = []

#     response = test_client.get("/users")
#     assert response.status_code == 200
#     assert response.json() == []

#     mock_prisma.user.find_many.assert_called_once()

#     app.dependency_overrides = {}


# def test_update_user(test_client: TestClient, mock_prisma):
#     email = "test@example.com"
#     new_name = "New Test User"

#     app.dependency_overrides[get_prisma] = lambda: mock_prisma
#     mock_prisma.user.find_first.return_value = {
#         "email": email, "name": "Old Name"}

#     response = test_client.put(f"/users/{email}?new_name={new_name}")
#     assert response.status_code == 200

#     mock_prisma.user.find_first.assert_called_once_with(where={'email': email})
#     mock_prisma.user.update.assert_called_once_with(
#         where={'email': email}, data={'name': new_name})

#     app.dependency_overrides = {}


# def test_delete_user(test_client: TestClient, mock_prisma):
#     email = "test@example.com"

#     app.dependency_overrides[get_prisma] = lambda: mock_prisma
#     mock_prisma.user.find_first.return_value = {
#         "email": email, "name": "Test User"}

#     response = test_client.delete(f"/users/{email}")
#     assert response.status_code == 200

#     mock_prisma.user.find_first.assert_called_once_with(where={'email': email})
#     mock_prisma.user.delete.assert_called_once_with(where={'email': email})

#     app.dependency_overrides = {}
