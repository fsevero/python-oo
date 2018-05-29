from database import Database

if __name__ == '__main__':
    db = Database()
    db.connect()
    db.make_schema()

    db.insert_client('Severo', '11111111111', 'severo.fabricio@gmail.com')
    db.insert_client('Fabrício', '00000000000', 'severo.fabricio@gmail.com')

    db.disconnect()