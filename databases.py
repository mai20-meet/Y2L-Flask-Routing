
from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def con():
  engine = create_engine('sqlite:///database.db')
  Base.metadata.create_all(engine)
  DBSession = sessionmaker(bind=engine)
  return DBSession()

def add_product(session, name, price, picture_link, description):
    product_object = product(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)
    session.add(product_object)
    session.commit()
add_product(con(), "hamburger",20, "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/165384.jpg", "this is the most tasty burger in the world' the one that you just want to bite it and eat 20 of it")

def update_lab_status(session, name, finished_lab):

   product_object = session.query(
       product).filter_by(
       product_id=product_id).first()
   product_object.finished_lab = finished_lab
   session.commit()


def delete_product(session, their_name):

   session.query(product).filter_by(
       product_id=product_id).delete()
   session.commit()


def query_all(session):

  products = session.query(product).all()
  return products



def query_by_id(session):

  products = session.query(product_id=product_id)
  return products

def Add_To_Cart(session, cart):
    product_object = product(
         cart=cart)
    session.add(product_object)
    session.commit()



print(query_all(con()))