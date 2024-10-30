from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# 成功時のレスポンス
class FibonacciResponse(BaseModel):
    result: int

# エラー時のレスポンス
class ErrorResponse(BaseModel):
    status: int
    message: str

# フィボナッチ数列を計算
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

# フィボナッチ数列の値を返すエンドポイント
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
                "message": "入力が無効です。整数を入力してください。"
            }
        )

    # 負の数のチェック
    if n < 0:
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "message": "負の整数が入力されています。正の整数を入力してください。"
            }
        )

    # フィボナッチ数列の計算
    fib_value = fibonacci(n)
    return {"result": fib_value}
