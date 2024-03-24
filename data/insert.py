import database as db

def Insert(object, tabela):
    atributes = [attr for attr in dir(object) if not callable(getattr(object, attr)) and not attr.startswith("__")]

    # Monta a string SQL dinamicamente
    colunas = ', '.join(atributes)
    valores = ', '.join(['%s'] * len(atributes))

    query = f"""
        INSERT INTO "{tabela}" ({colunas}) 
        VALUES ({valores})
    """

    # Obtém os valores dos atributes do object
    object_value = [getattr(object, attribute) for attribute in atributes]

    with db.conn, db.conn.cursor() as cursor:
        cursor.execute(query, object_value)

    count = db.cur.rowcount