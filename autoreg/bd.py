import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='my_user',
                             password='password',
                             database='acc_info',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "select * From accounts;"
        cursor.execute(sql)
        result = cursor.fetchone()

    connection.commit()

    print(result)