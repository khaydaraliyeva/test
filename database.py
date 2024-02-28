import psycopg2


class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='kun_uz',
            user='postgres',
            password='123456',
            host='localhost'
        )

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                fetchmany: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result

    def create_table_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER GENERATED ALWAYS AS IDENTITY PRiMARY KEY,
            category_name VARCHAR(50) UNIQUE NOT NULL
        )'''
        self.manager(sql, commit=True)

    def drop_table_articles(self):
        sql = '''DROP table articles'''
        self.manager(sql, commit=True)

    def insert_category(self, category):
        sql = '''INSERT INTO categories(category_name) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.manager(sql, (category,), commit=True)

    def delete_category_by_id(self, category_id):
        sql = '''DELETE FROM categories WHERE category_id = %s'''
        self.manager(sql, (category_id,), commit=True)

    def update_category_by_id(self, category_id):
        sql = '''UPDATE categories SET category_name = %s WHERE category_id = %s'''
        self.manager(sql, ('test', category_id), commit=True)

    def view_all_categories(self):
        sql = '''SELECT * FROM categories'''
        return self.manager(sql, fetchall=True)

    def create_table_articles(self):
        sql = '''CREATE TABLE IF NOT EXISTS articles(
            article_id INTEGER GENERATED ALWAYS AS IDENTITY PRiMARY KEY,
            title VARCHAR(250),
            content TEXT,
            created TIMESTAMP DEFAULT NOW(),
            views INTEGER
        )'''
        self.manager(sql, commit=True)

    def insert_article(self,article):
        sql = '''insert into articles(title,content,views) values (%s,%s,%s) on conflict do nothing'''
        self.manager(sql,(article,),commit=True)

    def delete_article_by_id(self,article_id):
        sql = '''delete from articles where article_id = %s'''
        self.manager(sql, (article_id,), commit=True)


    def update_article_by_id(self,article_id):
        sql = '''update articles set title,contet,views where article_id = %s'''
        self.manager(sql,(article_id,),commit=True)

    def view_article(self,):
        sql = '''select * from articles'''
        self.manager(sql,fetchall=True)

db = DataBase()