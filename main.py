from core import ddl_to_class

if __name__ == '__main__':
    ddl_sql = """
    create table user (
      id INT PRIMARY key comment "xxxx" 
      nick_name text PRIMARY key not null comment "用户昵称"
    ) comment "用户"
    """
    code = ddl_to_class(ddl_sql)
    print(code)