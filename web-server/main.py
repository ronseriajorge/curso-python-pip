import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,23,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola soy platzi</h1>
    <p>Hola soy un parrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()    