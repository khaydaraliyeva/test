from database import db


def add_category():
    category = input('\033[36m{}'.format("Kategoriyani kiriting: "))
    db.insert_category(category)
    yes_no = input('\033[38m{}'.format("Yana kategoriya qo'shasizmi?: ha/yoq: "))
    if yes_no == 'ha':
        add_category()


def view_categories():
    categories = db.view_all_categories()
    for category in categories:
        category_id, category_name = category
        print('|', str(category_id).center(5, ' '), '|', category_name.center(50, ' '), '|')


def delete_category():
    view_categories()
    category_id = int(input('\033[33m{}'.format("Kategoriya id sini kiriting: ")))
    db.delete_category_by_id(category_id)
    yes_no = input('\033[35m{}'.format("Yana kategoriya o'chirasizmi?: ha/yoq: "))
    if yes_no == 'ha':
        delete_category()


def update_category():
    view_categories()
    category_id = int(input('\033[36m{}'.format("Kategoriya id sini kiriting: ")))
    db.update_category_by_id(category_id)
    yes_no = input('\033[39m{}'.format("Yana kategoriyani o'zgartirasizmi?: ha/yoq: "))
    if yes_no == 'ha':
        update_category()

def add_article():
    article = input('\033[33m{}'.format('Article id sini kiriting : '))
    db.insert_article(article)
    yes_or_no = input('\033[36m{}'.format('Yana article kiritasizmi ? yes/no'))
    if yes_or_no == 'yes':
        add_article()

def view_articles():
    articles = db.view_article()
    for i in articles:
        a,b,c,d,e = i
        print('|',str(a).center(5,' '),'|',str(b).center(5,' '),'|',str(c).center(5,' '),'|',str(d).center(5,' '),'|',str(e).center(5,' '))
def delete_article_by_id():
    view_articles()
    article = int(input('\033[36m{}'.format('Ochirmoqchi bolgan article id sini kiriting')))
    db.delete_article_by_id(article)
    yeah = input('\033[32m{}'.format('Yana article ochirishni istaysizmi ? yes/no :'))
    if yeah == 'yes':
        delete_article_by_id()

def update_article():
    article = int(input('\033[37m{}'.format('article id sini kiriting : ')))
    db.update_article_by_id(article)
    yeah = input('\033[38m{}'.format('Yana article ozgartirmoqchimisz ? yes/no :'))
    if yeah == 'yes':
        update_article()
def run():
    while True:
        command = input('\033[36m{}'.format("Buyruqni kiriting: "))
        if command == 'stop':
            break
        elif command == 'add category':
            add_category()
        elif command == 'del category':
            delete_category()
        elif command == 'view categories':
            view_categories()
        elif command == 'update category':
            update_category()
        elif command == 'add article':
            add_article()
        elif command == 'del article':
            delete_article_by_id()
        elif command == 'view article':
            view_articles()
        elif command == 'update article:':
            update_category()




if __name__ == 'homework_11_4oy':
    db.create_table_categories()
    db.create_table_articles()
    db.drop_table_articles()
    run()