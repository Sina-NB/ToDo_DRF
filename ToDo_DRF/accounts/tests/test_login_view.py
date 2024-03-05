from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def user():
    user = User.objects.create_superuser(username="test_user", password="1234")
    return user


@pytest.fixture
def url():
    url = reverse("accounts:api-v1:login-api")
    return url


@pytest.mark.django_db
class TestLoginView:
    def test_post_status200(self, client, url, user):
        data = {"username": "test_user", "password": "1234", "remember_me": True}
        response = client.post(url, data)
        assert response.status_code == 200

    def test_post_status302(self, client, url, user):
        client.force_login(user=user)
        data = {"username": "test_user", "password": "1234", "remember_me": True}
        response = client.post(url, data)
        assert response.status_code == 302
