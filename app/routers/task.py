from fastapi import APIRouter,HTTPException,Depends
from pydantic import BaseModel
router=APIRouter()
class TaskCreate(BaseModel):
      title:str
      completed:bool
class TaskResponse(BaseModel):
      title:str
      completed:bool
      id:int
tasks=[]
next_task_id = 1
def find_task_id(task_id:int):
      for task in tasks:
            if task_id ==task.id:
                return task
      raise HTTPException(status_code=404, detail="Task not found")

@router .post("/task",description="welcom")
def root(task: TaskCreate):
    global next_task_id
    new_task = TaskResponse(
        title=task.title,
        completed=task.completed,
        id=next_task_id
    )
    tasks.append(new_task)
    next_task_id+=1
    return new_task


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_by_id(task:TaskResponse=Depends(find_task_id)):
            return task
    

@router .put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(updated_task: TaskCreate,task:TaskResponse=Depends(find_task_id) ):
    
            task.title = updated_task.title
            task.completed =updated_task.completed
            return task


@router.delete("/tasks/{task_id}")
def delete_task(task:TaskResponse=Depends(find_task_id)):
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    