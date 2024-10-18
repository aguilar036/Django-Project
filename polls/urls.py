from django.urls import path
from . import views

urlpatterns = [
	path( "", views.index, name = "index" ),
    path("create", views.question_view, name="create"),
    path("<int:question_id>", views.question_details, name="view"),

]

