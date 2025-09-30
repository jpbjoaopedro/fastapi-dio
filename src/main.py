from fastapi import FastAPI

app = FastAPI(title='WorkoutApi')

if __name__ == 'main':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8000, log_level='info', reload=True)