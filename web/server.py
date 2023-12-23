from fastapi import FastAPI
from pydantic import BaseModel

from core import ddl_to_class

app = FastAPI()


class InputData(BaseModel):
    ddl_sql: str


class ResponseData(BaseModel):
    code: int
    data: str
    message: str


@app.post("/api/ddl_to_class/", response_model=ResponseData)
def process_sql_ddl(input_data: InputData):
    try:
        ddl_statement = input_data.ddl_sql
        print(f"ddl sql: \n {ddl_statement}")
        code = ddl_to_class(ddl_statement)
        print(f"plantuml code: \n {code}")
        # 创建并返回响应
        response = ResponseData(code=200, data=code, message="ok")
        return response

    except Exception as e:
        # 处理可能的错误
        error_message = str(e)
        response = ResponseData(code=500, data="", message=f"Error processing DDL statement: {error_message}")
        return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
