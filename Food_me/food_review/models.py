from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import CharField 
from django.contrib.auth.models import User

# ------------------------------------------------------------
# -------------------- TYPE OF FOOD --------------------------
# ------------------------------------------------------------
class TypeOfFood(models.Model):
    """Type of food served by restaurant"""

    # Type of food
    type_of_food = models.CharField(
        max_length= 50,
        help_text="Type of food served by restaurant"
    )

    # Return a string
    def __str__(self) -> str:
        return self.type_of_food

# ------------------------------------------------------------
# ----------------------- TAGS -------------------------------
# ------------------------------------------------------------

class Tag(models.Model):
    """Tags that classify a restaurant"""

    # Descriptive tag 
    tag_name = models.CharField(
        max_length= 25,
        help_text="Descriptive tag"
    )

    # Return a string
    def __str__(self) -> str:
        return self.tag_name

# ------------------------------------------------------------
# ----------------- RESTAURANT MODEL  ------------------------
# ------------------------------------------------------------
# Create your models here.
class Restaurant(models.Model):
    """A restaurant and its details"""

    # Name of the Restaurant
    name = models.CharField(
        help_text="Name of the restaurant.",
        max_length=250,
            
    )
    #Street address 
    street_address = models.CharField(
        help_text="Address of the restaurant.",
        max_length=250,
    )
    # City
    city = models.CharField(
        help_text="City restaurant is located in.",
        max_length=100,
        
    )
    # State
    state = models.CharField(
        help_text="State of restaurant location.",
        max_length=2
    )
    # Zip code (5-digit)
    zip = models.CharField(
        help_text="Zip code of restaurant location.",
        max_length=5
    )
    # Phone (###)###-####
    phone = models.CharField(
        help_text="Phone Number of Restaurant",
        max_length=12
        )
    
    # Type of food restaurant serves
    type_food = models.ForeignKey(
        TypeOfFood,
        help_text="Type of food served by restaurant.",
        on_delete=models.CASCADE
    )

    # Tags describing the restaurant
    tags = models.ManyToManyField(Tag)

    # Return a string
    def __str__(self) -> str:
        return self.name

# ------------------------------------------------------------
# ----------------------- COMMENT ----------------------------
# ------------------------------------------------------------

class Comment(models.Model):
    """Comment about a experience at Restaurant"""

    # Body of the comment
    body = models.TextField(
        help_text="The comment text"
    )
    # 1 to 10 rating 
    rating = models.PositiveIntegerField(
        help_text="The rating the reviewer has given.",
        validators=[MinValueValidator(1),MaxValueValidator(10)]
    )
    # Date comment was updated
    date_updated = models.DateTimeField(
        null=True,
        help_text="The date and time the review was created or last edited"
    )
    # Restaurant comment is created for
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        help_text="The Restaurant that the review is for."
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null = False,
        help_text="The user who wrote the comment"
    )

    # Return a string
    def __str__(self) -> str:
        return self.body




