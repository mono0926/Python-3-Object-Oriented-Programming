import datetime
import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = "article"
    rowid = sqa.Column(sqa.Integer, primary_key=True)
    title = sqa.Column(sqa.String)
    message = sqa.Column(sqa.String)
    pub_date = sqa.Column(sqa.DateTime)

    def __init__(self, title, message):
        self.title = title
        self.message = message
        self.pub_date=datetime.datetime.now()

class Comment(Base):
    __tablename__ = "comment"
    rowid = sqa.Column(sqa.Integer, primary_key=True)
    article_id = sqa.Column(sqa.Integer,
            sqa.ForeignKey('article.rowid'))
    article = sqa.orm.relationship(Article, backref="comments")
    name = sqa.Column(sqa.String)
    message = sqa.Column(sqa.String)

    def __init__(self, article_id, name, message):
        self.article_id = article_id
        self.name = name
        self.message = message


engine = sqa.create_engine('sqlite:///blog.db')
Base.metadata.create_all(engine)
Session = sqa.orm.sessionmaker(bind=engine)

import jinja2
templates = jinja2.Environment(loader=jinja2.FileSystemLoader(
        'blog_templates'))

import cherrypy
class Blog:
    @cherrypy.expose
    def index(self):
        session = Session()
        articles = session.query(Article).all()
        template = templates.get_template("index.html")
        content = template.render(articles=articles)
        session.close()
        return content

    @cherrypy.expose
    def add(self):
        template = templates.get_template("add.html")
        return template.render()

    @cherrypy.expose
    def process_add(self, title=None, message=None):
        session = Session()
        article = Article(title, message)
        session.add(article)
        session.commit()
        session.close()
        raise cherrypy.HTTPRedirect("/")

    @cherrypy.expose
    def process_comment(self, article_id, name=None,
            message=None):
        session = Session()
        comment = Comment(article_id, name, message)
        session.add(comment)
        session.commit()
        session.close()
        raise cherrypy.HTTPRedirect("/")

cherrypy.quickstart(Blog())
