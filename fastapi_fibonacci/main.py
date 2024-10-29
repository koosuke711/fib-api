from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class FibonacciResponse(BaseModel):
    result: int

class ErrorResponse(BaseModel):
    status: int
    message: str

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

@app.get("/fib", response_model=FibonacciResponse)
async def get_fibonacci(n: str):
    # 整数かどうかをチェック
    try:
        n = int(n)
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "message": "Badrequest."
            }
        )

    # 負の数のチェック
    if n < 0:
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "message": "Badrequest."
            }
        )

    # フィボナッチ数の計算
    fib_value = fibonacci(n)
    return {"result": fib_value}
