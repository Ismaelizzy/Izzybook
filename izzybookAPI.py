from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field

from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models

app = FastAPI()

# Enable CORS to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to "*" to allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




def get_db():
    
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

    models.Base.metadata.create_all(bind=engine)

class PostCreate(BaseModel):
    postId: str
    userId: str
    content: str


class PostUpdate(BaseModel):
    postId: str
    userId: str
    content: str
    
@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

@app.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    

    post_model = models.Post()
    post_model.postId = post.postId
    post_model.userId = post.userId
    post_model.content = post.content
   

    db.add(post_model)
    db.commit()
   
    return post

@app.put("/{post_id}")
def update_post(post_id: int, updated_post: PostUpdate, db: Session = Depends(get_db)):

    # Retrieve the existing post from the database
    post_model = db.query(models.Post).filter(models.Post.id == post_id).first()

    if post_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Post with ID {post_id} does not exist"
        )
    
    # Update the attributes of the existing post
    post_model.postId = updated_post.postId
    post_model.userId = updated_post.userId
    post_model.content = updated_post.content
    
    # Commit the changes to the database
    db.commit()

    # Return the updated post
    return updated_post

