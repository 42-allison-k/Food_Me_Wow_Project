from datetime import date
from django.core.management.base import BaseCommand
import sys
import random
from food_review.models import TypeOfFood, Tag, Restaurant, Comment
# Seed database
# run 'python manage.py seed --mode=refresh' in CL to clear DB and repopulate with data
# run 'python manage.py seed --mode=clear' in CL to clear DB

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    """
    Creates command to seed database
    Allowing use of 'python manage.py seed'
    """

    help = "seed database for testing and development."

    # adds ability to add arguments
    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    # handle call
    def handle(self, *args, **options):
        # print when seeding data
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        # write when completed
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    
    sys.stdout.write("Deleting TypeOfFood")
    TypeOfFood.objects.all().delete()

    sys.stdout.write("Deleting Tags")
    Tag.objects.all().delete()

    sys.stdout.write("Deleting Restaurants")
    Restaurant.objects.all().delete()



def create_typeoffoods():
    """Seeds TypeOfFood Table"""

    sys.stdout.write("Populating TypeOfFoods...")

    type_of_foods = ["mexican", "italian", "indian", "cajun", "soul",
    "thai","greek", "chinese","vegan","lebanese",
    "japanese","american","moroccan","mediterranean","french",
    "spanish", "german","korean","vietnamese","turkish","caribbean"]

    for food in type_of_foods:

        type_food = TypeOfFood(
            type_of_food = food
        )
        type_food.save()
    
    return

def create_tags():
    """Seeds Tag Table"""

    sys.stdout.write("Populating Tags...")

    tags = ["vegan", "spicy", "ovo lacto", "gluten-free", 
    "family style", "breakfast", "lunch", "dinner",
    "dessert","happy hour","paleo"]

    for tag in tags:

        tag_to_save = Tag(
            tag_name = tag
        )
        tag_to_save.save()
    
    return

def create_restaurants():
    """Seeds Restaurant Table"""

    sys.stdout.write("Populating Restaurants...")
    restaurants = [
        {
            "name":"serial grillers",
            "street_address":"5737 e speedway blvd",
            "city":"tucson",
            "state":"AZ",
            "zip": "85712",
            "phone":"(520)546-2160",
            "tags": ["lunch", "dinner"],
            "comments":[
            {
                "body":"hannibal! best sandwich EVER!",
                "rating":10,
            },
            ]
        },
        {
            "name":"crescent city bourbon & bbq",
            "street_address":"19 salem ave",
            "city":"roanoke",
            "state":"VA",
            "zip": "24011",
            "phone":"(540)342-2990",
            "tags": ["spicy", "dinner"],
            "comments":[
            {
                "body":"best brisket ever",
                "rating":9
            },
            ]
        },
    ]

    type_of_food_ids = TypeOfFood.objects.values_list("id", flat=True)

    for restaurant_data in restaurants:

        resturant = Restaurant.objects.create(
            name = restaurant_data["name"],
            street_address = restaurant_data["street_address"],
            city = restaurant_data["city"],
            state = restaurant_data["state"],
            zip = restaurant_data["zip"],
            phone = restaurant_data["phone"],
            type_food_id = random.choice(type_of_food_ids)
        )

        resturant.tags.add(*Tag.objects.filter(tag_name__in = restaurant_data["tags"]))


        id = resturant.id
    

        for comment in restaurant_data["comments"]:
            
            Comment.objects.create(
                body = comment["body"],
                rating = comment["rating"],
                date_updated=date.today(),
                restaurant_id= id
            )


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    # if only clearing, exit before populating
    if mode == MODE_CLEAR:
        return
    # populate database
    create_typeoffoods()
    create_tags()
    create_restaurants()
