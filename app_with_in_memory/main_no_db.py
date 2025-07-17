"""
This file contains endpoints for all the CRUD operation but without any use of SQL, database and SqlAlchemy.
This is simple in memory representation."""


from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool


posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
         {"title": "favorite foods", "content": "I like pizza", "id": 2},
         {"title": "title of post 3", "content": "content of post 3", "id": 3}]



# welcome endpoint
@app.get('/')
def root():
    return {'message': 'Welcome to my API!'}


# get all posts
@app.get("/posts")
def get_posts():
    return {"data": posts}

def find_post(id: int):
    for post in posts:
        if post['id'] == id:
            return post
    return None


# get single post
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        return {"message": f"post with id: {id} was not found"}
    return {"post_detail": post}


# create a post
@ app.post('/posts')
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    posts.append(post_dict)
    return {"data": post_dict}


def find_index_post(id: int):
    for i, p in enumerate(posts):
        if p['id'] == id:
            return i
    
    return None


# delete a post
@app.delete('/posts/{id}')
def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        return {"message": f"post with id: {id} does not exist"}
    
    posts.pop(index)
    return {"message": f"post with id: {id} was successfully deleted"}


# update a post
@app.put('/post/{id}')
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        return {"message": f"post with id: {id} does not exist"}
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    posts[index] = post_dict
    return {"data": post_dict}






