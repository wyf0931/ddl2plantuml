from typing import Text

from lark import Lark

from .transformer import DdlSqlTransformer
from .visitor import translate

with open('core/grammar/ddl_create_sql.lark', 'r', encoding='utf-8') as f:
    grammar = f.read()

dsl_parser = Lark(grammar, parser="lalr", transformer=DdlSqlTransformer())


def ddl_to_class(create_table_sql: Text) -> Text:
    """
    convert DDL SQL to PlantUML code.
    :param create_table_sql:
    :return:
    """
    try:
        ddl = dsl_parser.parse(create_table_sql)
        return translate(ddl)
    except Exception as e:
        print(e)
        raise Exception("SQL Parse fail.")
