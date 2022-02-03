from sqlalchemy import func

from .db import session
from .models import Order, OrderItem, PriceTag

################################ PriceTags ####################################
# All pricetags ordered by title
pricelist_query = PriceTag.query.order_by(PriceTag.title)

# All unique job types
jobtypes_query = PriceTag.query.with_entities(PriceTag.job_type).distinct()

# All unique measurement units
units_query = PriceTag.query.with_entities(PriceTag.unit).distinct()

# Get pricetag
pricetag_query = lambda id: PriceTag.query.get(id)
###############################################################################

################################# Orders ######################################
# Get single order
order_query = lambda id: Order.query.get(id)

# Orders merged with order items
sum_by_order_id = Order.query.outerjoin(OrderItem).group_by(
    Order.id, Order.client, Order.description, Order.date)

# Orders list with totals
orders_query = sum_by_order_id.with_entities(
    Order.id, Order.client, Order.description, Order.date).add_columns(
        func.sum(OrderItem.price * OrderItem.quantity).label("total"))

###############################################################################

################################ OrderItems ###################################
# Get single item
item_query = lambda id: OrderItem.query.get(id)

# Get items by order id
order_items_query = lambda id: OrderItem.query.filter_by(order_id=id)

# Joined table
order_items_prices = lambda id: order_items_query(id).join(
    PriceTag).with_entities(OrderItem.job_id, OrderItem.price, OrderItem.
                            quantity, OrderItem.id).add_columns(
                                PriceTag.title, PriceTag.unit)

###############################################################################


################################# Actions #####################################
# Add to db
def add_item(item):
    session.add(item)
    session.commit()


# Delete from db
def delete_items(*items):
    for item in items:
        session.delete(item)
    session.commit()


###############################################################################
