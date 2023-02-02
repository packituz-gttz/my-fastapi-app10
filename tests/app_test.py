import jsonfrom fastapi import FastAPIapp = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
def test_read_root():
    response = app.test_client().get('/')
    assert response.status_code == 200    assert json.loads(response.content) == {"Hello": "World"}
def test_read_item():
    response = app.test_client().get('/items/42?q=test')
    assert response.status_code == 200    assert json.loads(response.content) == {"item_id": 42, "q": "test"}
