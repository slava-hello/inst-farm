import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='564738Hej29Slav',
                             database='accounts_vtope',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        sql = "SELECT User_id, User_Token FROM test WHERE Dialog_id = %s"
        cursor.execute(sql, message.chat.id)
        result = cursor.fetchone()

    connection.commit()

    print(result)