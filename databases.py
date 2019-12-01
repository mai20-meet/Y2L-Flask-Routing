
from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

cart = []

def add_product(name, price, picture_link, description):
    product_object = product(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)
    session.add(product_object)
    session.commit()
#add_product( "hamburger",20, "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/165384.jpg", "this is the most tasty burger in the world' the one that you just want to bite it and eat 20 of it")

def update_product_status(name, price, picture_link, description):

   product_object = session.query(
       product).filter_by(
       name=name).first()
   product_object.price = price
   session.commit()


def delete_product(their_name):

   session.query(product).filter_by(
       name=name).delete()
   session.commit()


def query_all():

  products = session.query(product).all()
  return products



def query_by_name():

  products = session.query(name=name)
  return products

def Add_To_Cart(product_id):
  product = session.query(id = product_id)
  cart.append(product)
  return product

print(query_all())