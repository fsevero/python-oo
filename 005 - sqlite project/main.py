from database import Database

if __name__ == '__main__':
    db = Database()
    db.connect()
    db.make_schema()

    print('-'*80)

    db.insert_client('Severo', '11111111111', 'severo.fabricio@gmail.com')
    db.insert_client('Fabrício', '22222222222', 'severo.fabricio@gmail.com')

    print('-'*80)

    db.search_client('11111111111')
    db.search_client('22222222222')
    db.search_client('33333333333')

    print('-'*80)

    db.search_email('severo.fabricio@gmail.com')
    db.search_email('severo.fabricio@gmail.com.br')

    print('-'*80)

    db.disconnect()