from fastapi import FastAPI

app = FastAPI ()

@app.get('/')
def index():
    return {'message '  :  'hello world'}


@app.get('/get_id/{id}')
def get_id(id:int):
    return {'Your id': f'{id}'}
