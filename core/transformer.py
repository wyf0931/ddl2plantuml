from lark import Transformer, v_args


@v_args(inline=True)
class DdlSqlTransformer(Transformer):
    """
    Parse DDL Create syntax and convert to Dict.
    """
    def STRING(self, s):
        # 移除字符串周围的双引号
        return s[1:-1]

    def CNAME(self, c):
        return str(c)

    def TYPE(self, t):
        return str(t)

    def primary_key(self, *args):
        return "pk"

    def autoincrement(self, *args):
        return "incr"

    def not_null(self, *args):
        return "not null"

    def table(self, table_name, *fields_and_comment):
        fields = []
        comment = None
        for item in fields_and_comment:
            if isinstance(item, dict):
                fields.append(item)
            else:
                comment = item
        return {
            "name": table_name,
            "comment": comment,
            "fields": fields
        }

    def column(self, name, type, *constraints_and_comment):
        constraints = []
        comment = None
        for item in constraints_and_comment:
            if isinstance(item, tuple):
                constraints.append(item)
            else:
                comment = item

        return {
            "name": name,
            "type": type,
            "constraints": constraints,
            "comment": comment
        }

    def comment(self, comment):
        return comment

    def constraint(self, *args):
        return args

    def start(self, table):
        return table
