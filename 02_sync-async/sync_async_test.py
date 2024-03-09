import time
import asyncio

from fastapi import APIRouter

router = APIRouter()


@router.get('/slow-async-ping')
async def slow_async_ping():
    time.sleep(10)
    return {'msg': 'pong'}


@router.get('/fast-async-ping')
async def fast_async_ping():
    await asyncio.sleep(10)  # REST API 호출, 무거운 작업 X - EventLoop를 잡아먹기 때문(성능저하)
    return {'msg': 'pong'}


@router.get('/cpu-bound-async')
async def cpu_bound_async():
    result = await cpu_intensive_task()
    return {'msg': result}


def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    result = fibonacci(35)
    return result


from concurrent.futures import ProcessPoolExecutor


@router.get('/cpu-bound-task')
async def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        result = await asyncio.get_event_loop().run_in_executor(
            executor, cpu_intensive_task)
    return {'result': result}
