from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def welcome():
    return {'message': 'welcome to my fast api'}

#get all tasks
@app.get('/api/tasks')
async def get_tasks():
    return 'all tasks'
#create tasks 
@app.post('/api/tasks')
async def crate_task():
    return 'create task'
 
@app.get('/api/tasks/{id}')
async def get_task():
    return 'single task'
 
@app.put('/api/tasks/{id}')
async def update_task():
    return 'update tasks'
 
@app.delete('/api/tasks/{id}')
async def delete_task():
    return 'delete tasks' 