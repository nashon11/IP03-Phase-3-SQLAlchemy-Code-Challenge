from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Review, Customer

# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///restaurant_reviews.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create sample instances
restaurant1 = Restaurant(name='Restaurant 1', price=2)
restaurant2 = Restaurant(name='Restaurant 2', price=3)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

# Add instances to the session
session.add(restaurant1)
session.add(restaurant2)
session.add(customer1)
session.add(customer2)

# Commit the changes to the database
session.commit()

# Create reviews
review1 = Review(star_rating=4, customer=customer1, restaurant=restaurant1)
review2 = Review(star_rating=5, customer=customer2, restaurant=restaurant2)

# Add reviews to the session
session.add(review1)
session.add(review2)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
