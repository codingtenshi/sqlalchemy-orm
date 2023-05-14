from models import Session, User
#  odczyt użytkowników z bazy danych


def main():
    session = Session()

    query = session.query(User).order_by(User.salary.desc())  # obiekt, który inkapsuuje sql
    #query = session.query(User).filter(User.salary > 9000)
    # print(query)
    for row in query.order_by(User.salary.desc()):
        print(row)


if __name__ == '__main__':
    main()
