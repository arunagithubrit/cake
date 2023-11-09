from django.urls import path
from cakeapp.views import SignUpView,SignInView,CategoryCreateView,remove_category,CakeCreateView,CakeListView,CakeUpdateView,\
remove_cakeview,CakeVarientCreateView,CakeDetailView,CakeVarientUpdateView,remove_varient,OfferCreateView,\
offer_delete_view,sign_out_view,IndexView




urlpatterns=[
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cakes/add",CakeCreateView.as_view(),name="cake-add"),
    path("cakes/all",CakeListView.as_view(),name="cake-list"),
    path("cakes/<int:pk>/change",CakeUpdateView.as_view(),name="cake-change"),
    path("cakes/<int:pk>/remove",remove_cakeview,name="cake-remove"),
    path("cakes/<int:pk>/varients/add",CakeVarientCreateView.as_view(),name="add-varient"),
    path("cakes/<int:pk>",CakeDetailView.as_view(),name="cake-detail"),
    path("varients/<int:pk>/change/",CakeVarientUpdateView.as_view(),name="update-varient"),
    path('varients/<int:pk>/remove/',remove_varient,name="remove-varient"),
    path("varients/<int:pk>/offers/add",OfferCreateView.as_view(),name="offers-add"),
    path('offers/<int:pk>/remove',offer_delete_view,name="remove-offer"),
    path('logout/',sign_out_view,name="signout"),
    path('index/',IndexView.as_view(),name="index")

]