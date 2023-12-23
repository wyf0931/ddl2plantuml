# ddl2plantuml
DDL Create SQL convert to PlantUML Class disgram code.

## Quickstart
1. clone this repo.
2. install dependencies: `pip install -r requirements.txt`
3. Start server:
    ```shell
    uvicorn main:app --reload
    ```
### Hello World
Example in `example.py`:
```python 
from core import ddl_to_class

if __name__ == '__main__':
    
    ddl_sql = """
    create table user (
      id INT PRIMARY key comment "user id" 
      nick_name text PRIMARY key not null comment "user nick"
    ) comment "user info"
    """
    
    code = ddl_to_class(ddl_sql)
    print(code)
```
output:
```plantuml
entity user { 
    id : INT 
    nick_name : text 
}
```

### HTTP Call
use `curl` send post request:
```shell
curl -X POST "http://127.0.0.1:8000/api/ddl_to_class/" \
     -H "Content-Type: application/json" \
     -d '{"ddl_sql": "CREATE TABLE example_table (id INT, name VARCHAR)"}'
```

response:
```json
{
    "code": 200,
    "data": "entity example_table { \n    id : INT \n    name : VARCHAR \n}\n",
    "message": "ok"
}
```

## Similar projects
- [dbsql2puml](https://github.com/deadbok/py-puml-tools/tree/master/)

## Dependencies
- [lark](https://github.com/lark-parser/lark)
- [fastapi](https://github.com/tiangolo/fastapi)

## License
ddl2plantuml is completely free and open-source and licensed under the MIT license.