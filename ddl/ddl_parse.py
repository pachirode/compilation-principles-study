from simple_ddl_parser import DDLParser


class DDLParse:
    CLASS_TEMPLATE = "class {class_name}(db.Model):\n    __tablename__ = '{table_name}'\n"
    PRIMARY_FIELD_TEMPLATE = "    {field_name} = db.Column(db.{field_type}, primary_key=True, autoincrement=True)\n"
    FIELD_TEMPLATE = "    {field_name} = db.Column(db.{field_type})\n"

    DB_TYPE_TO_PY = {
        "varchar": "String",
        "int": "Integer",
        "bigint": "BigInteger",
        "datetime": "DateTime",
        "date": "Date",
        "decimal": "Numeric",
        "text": "Text",
    }

    def __init__(self, ddl):
        self.ddl = ddl
        self.tables = DDLParser(ddl).run()

    @staticmethod
    def to_camel_case(s: str) -> str:
        parts = s.split("_")
        return "".join([p.capitalize() for p in parts])

    @staticmethod
    def get_field_length(column_def) -> str:
        if "(" in column_def and ")" in column_def:
            return column_def.split("(")[1].split(")")[0]
        return ""

    def transfer_field(self, column: dict, primary=False) -> str:
        field_name = column["name"].replace("`", "")
        field_type = column["type"].lower()
        py_type = self.DB_TYPE_TO_PY.get(field_type, "String")

        if field_type == "varchar":
            length = column.get("size") or ""
            py_type = f"{py_type}({length})" if length else py_type

        template = self.PRIMARY_FIELD_TEMPLATE if primary else self.FIELD_TEMPLATE
        return template.format(field_name=field_name, field_type=py_type)

    def transfer(self) -> str:
        py_model = ""

        for table in self.tables:
            table_name = table["table_name"].replace("`", "")
            class_name = self.to_camel_case(table_name)

            py_model += self.CLASS_TEMPLATE.format(class_name=class_name, table_name=table_name)

            primary_keys = table.get("primary_key", [])
            for column in table["columns"]:
                is_primary = column["name"] in primary_keys
                py_model += self.transfer_field(column, primary=is_primary)

        return py_model


if __name__ == '__main__':
    ddl_file = "demo.sql"

    with open(ddl_file, "r", encoding="utf-8") as f:
        ddl = f.read()

    parser = DDLParse(ddl)
    python_model = parser.transfer()
    print(python_model)
