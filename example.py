from core import ddl_to_class

if __name__ == '__main__':
    ddl_sql = """
    create table user (
      id INT PRIMARY key comment "user id" 
      nick_name text PRIMARY key not null comment "user nick name"
    ) comment "user info table"
    """
    code = ddl_to_class(ddl_sql)
    print(code)