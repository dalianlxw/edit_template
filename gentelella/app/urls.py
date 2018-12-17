from django.conf.urls import url
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    url(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    url(r'^$', views.index, name='index'),
    url(r'^form_upload$',views.form_upload),
    url(r'^form_info$',views.form_info),
    url(r'^singe_submit$',views.singe_submit),
    url(r'^chapter$',views.chapter),
    url(r'^get_chapter$',views.get_chapter),
    url(r'^form_test$',views.form_test),
]
