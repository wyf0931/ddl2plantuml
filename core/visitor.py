from typing import Text, Dict


def translate(ddl: Dict) -> Text:
    """
    translate MySQL DDL(create table) SQL to PlantUML Class diagram code.
    :return: PlantUML Class diagram code.
    """
    class_name = ddl['name']
    code = f"entity {class_name} {{ \n"
    for f in ddl['fields']:
        code += f"    {f['name']} : {f['type']} \n"
    code += "}\n"
    return code
