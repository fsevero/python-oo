from database import Database

if __name__ == '__main__':
    db = Database()
    db.connect()
    db.make_schema()

    db.insert_client('Severo', '11111111111', 'severo.fabricio@gmail.com')
    db.insert_client('Fabrício', '22222222222', 'severo.fabricio@gmail.com')

    db.search_client('11111111111')
    db.search_client('22222222222')
    db.search_client('33333333333')

    db.disconnect()