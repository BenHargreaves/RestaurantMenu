from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#myFirstRestaurant = Restaurant(name = 'Pizza Palace')
#session.add(myFirstRestaurant)
#session.commit()
#restaurants = session.query(Restaurant).all()

#for restaurant in restaurants:
#    print(restaurant)

#cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with Cheese, duh",
#    course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
#session.add(cheesepizza)
#session.commit()
#firstResult = session.query(MenuItem).first()

#print(firstResult.name)
#print(session.query(Restaurant).all())

VeggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')

for veggieBurger in VeggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print('\n')