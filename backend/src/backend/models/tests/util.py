import random
from typing import List

from ..models import Customer

def random_customer(customers: List[Customer]) -> Customer:
    return customers[random.randint(0, (len(customers)-1))]

