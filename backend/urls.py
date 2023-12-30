from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from main.api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.api.urls')),

    path('send_otp/', send_otp, name='send_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),

    path('register_user/', register_user, name='register_user'),
    path('user_login/', user_login, name='user_login'),

    path('user/<str:username>/', user_profile, name='user_profile'),
    path('get_user_reviews/<str:user_email>/', get_reviews_of_user, name='get_reviews_of_user'),
    path('get_reviews/<str:to_user_email>/', get_reviews_for_user, name='get_reviews_for_user'),
    path('get_profile/<str:email>/', get_profile, name='get_profile'),
    
    path('check_profile/<str:email>/', check_profile_completion, name='check_profile'),
    path('search-suggestions/', search_suggestions, name='search_suggestions'),

    path('update_bio/<str:email>/', update_bio, name='update_bio'),
    path('update_image/<str:email>/', update_image, name='update_image'),

    path('upvote_review/<int:review_id>', upvote_review, name='upvote_review'),
    path('downvote_review/<int:review_id>', downvote_review, name='downvote_review'),

    path('delete_review/<int:review_id>', delete_review, name='delete_review'),
    path('edit_review/<int:review_id>', edit_review, name='edit_review'),
    path('has_reviewed/<str:to_user_email>/', has_reviewed, name='has_reviewed'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

### deployment changes to handle static and media files ###
else:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
### end of deployment changes ###