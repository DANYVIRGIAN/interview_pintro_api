import pytest

def test_get_post(post_service):
    response = post_service.get_single_post(1)
    
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_list_posts(post_service):
    response = post_service.get_all_posts()
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post(post_service):
    response = post_service.create_new_post(title="foo", body="bar", user_id=1)
    
    assert response.status_code == 201
    assert response.json()["title"] == "foo"

def test_patch_post(post_service):
    response = post_service.update_post_title(post_id=1, new_title="updated title")
    
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"

def test_delete_post(post_service):
    response = post_service.delete_post(1)
    
    assert response.status_code == 200