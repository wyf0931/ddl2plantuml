# ddl2plantuml
DDL Create SQL convert to PlantUML Class disgram code.

## Usage

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