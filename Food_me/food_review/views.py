from django.shortcuts import render, redirect
from datetime import date
from django.views import View
from food_review.models import Restaurant, Tag, TypeOfFood, Comment 
from food_review.forms import AddRestaurant, AddRestaurantTags, AddRestaurantReview


def RenderRestaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    tags = restaurant.tags.all()
    comments = Comment.objects.all().filter(restaurant_id=restaurant_id)

    return render(
        request,
        "restaurant_profile.html",
        context={
            "restaurant_id": restaurant_id,
            "restaurant": restaurant,
            "tags": tags,
            "comments": comments
        })
# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, "index.html")

class SearchView(View):
    '''Search for a restaurant'''

    def get(self, request):

        try:
            search = request.GET['q']
            restaurants = Restaurant.objects.filter(
                name__startswith=str(search))

            context = {
                "search": search,
                "restaurants":  restaurants
            }

            return render(request, "search.html", context)

        except:
            context = {
                "restaurants":  Restaurant.objects.all()
            }

            return render(request, "search.html", context)

class RestaurantProfile(View):
    pass

class AddRestaurantView(View):
    '''Add a restaurant'''

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "add_restaurant.html", {"AddRestaurant": AddRestaurant, "tags": tags,  "AddRestaurantTags": AddRestaurantTags})

    def post(self, request):
        restaurant = {
            "name": request.POST["resturant_name"],
            "street_address": request.POST["address"],
            "city": request.POST["city"],
            "state": request.POST["state"],
            "zip": request.POST["zip_code"],
            "phone": request.POST["phone_number"],
            "type_food": TypeOfFood(id=int(request.POST["type_food"]))
            
        }
        new_restaurant = Restaurant.objects.create(**restaurant)
        new_restaurant.tags.set(request.POST.getlist("tag"))
        new_restaurant_id = new_restaurant.id

        return redirect(f'/restaurant/{new_restaurant_id}')

    
class RestaurantProfile(View):
    '''View comments and details of restaurant'''

    def get(self, request, restaurant_id):
        return RenderRestaurant(request, restaurant_id)

    def post(self, request, restaurant_id):
        comment = {
            'body': request.POST['review'],
            'rating': request.POST['rating'],
            'date_updated': date.today(),
            'restaurant_id': restaurant_id
        }
        Comment.objects.create(**comment)
        return RenderRestaurant(request, restaurant_id)    

class Comments(View):
    '''Modifying comments of a restaurant'''

    def post(self, request, restaurant_id, comment_id):

        comment = Comment.objects.get(pk=comment_id)

        if 'patch' in request.POST:
            comment.body = request.POST['review']
            comment.date_updated = date.today()
            comment.rating = request.POST['rating']
            comment.save()

        # DELETE A COMMENT
        if 'delete' in request.POST:
            comment.delete()
            return redirect(f'/restaurant/{restaurant_id}')

        return RenderRestaurant(request, restaurant_id)

