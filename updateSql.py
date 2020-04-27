# ------------------------------------------
# 批量更新数据库的SQL语句用代码编写
# ------------------------------------------

# 批量更新方法一，数据量小与500条时效率高
def update(tableName, fieldName, datas):
    rows = ["CASE"]
    field = []

    for data in datas:
        row = "WHEN id=%s THEN %s" % (data['id'], data[fieldName])
        rows.append(row)
        field.append(data['id'])

    rows.append("END")
    rows = tuple(rows)
    field = tuple(field)
    rows = str(rows)
    field = str(field)

    rows = rows.replace("\'", "")
    field = field.replace("\'", "")
    rows = rows.replace(",", "")

    sql = 'UPDATE %s SET %s=%s WHERE id IN %s;' % (tableName, fieldName, rows,
                                                   field)
    print(sql)


# 批量更新方法二，数据量大于与1000条时效率高
def update2(tableName, fieldName, datas):
    rows = []

    for data in datas:
        row = "SELECT %s AS id, %s AS %s UNION" % (data['id'], data[fieldName],
                                                   fieldName)
        rows.append(row)

    strRows = str(tuple(rows))

    strRows = strRows.replace("\'", "")
    strRows = strRows.replace("UNION,", "!")
    strRows = strRows.replace("UNION", "")
    strRows = strRows.replace("!", "UNION")

    sql = "UPDATE %s a JOIN %s b USING(id) SET a.%s=b.%s;" % (
        tableName, strRows, fieldName, fieldName)
    print(sql)


datas = [{
    'id': 1,
    'name': 'shj',
    'sex': 'man',
    'year': 27
}, {
    'id': 2,
    'name': 'touot',
    'sex': 'woman',
    'year': 25
}, {
    'id': 3,
    'name': 'kouok',
    'sex': 'man',
    'year': 18
}]
update('test', 'name', datas)
update2('test', 'name', datas)
