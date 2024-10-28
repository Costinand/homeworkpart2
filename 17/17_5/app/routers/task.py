from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import Task
from app.models import User
from app.schemas import CreateUser, UpdateUser
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete

from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(
        db: Annotated[Session, Depends(get_db)],
    task_id: int
):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        return task
    raise HTTPException(
        status_code=404,
        detail="Task was not found"
    )


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = db.scalars(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='There is no user found')
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   user_id=user_id,
                                   slug=slugify(create_task.title)))
    db.commit()
    return {
        'status-code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)],
        task_id: int,
        task_update_model: UpdateTask
):
    task = db.scalar(select(Task).where(Task.id == task_id))

    if task is not None:
        db.execute(update(Task).where(Task.id == task_id).values(
            title=task_update_model.title,
            content=task_update_model.content,
            priority=task_update_model.priority
        ))
        db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Task update is successful!'
        }

    raise HTTPException(
        status_code=404,
        detail="There is no task found"
    )


@router.delete('/delete')
async def delete_task(
    db: Annotated[Session, Depends(get_db)],
    task_id: int,
):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Task delete is successful!'
        }

    raise HTTPException(
        status_code=404,
        detail="Ther is task no found"
    )

