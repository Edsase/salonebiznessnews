from django.conf.urls import url


from news import views

urlpatterns = [
    url(r'^$', views.index , name = "index"),
    url(r'^about/$', views.about, name = "about"),
    url(r'^feed/(?P<feed_name_slug>[\w\-]+)/$', views.show_feed, name = 'show_feed'),
    #url(r'^add_category/$', views.add_category, name="add_category"),
    #url(r'^add_page/$', views.add_page, name="add_page"),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name = 'add_page'),
    #url(r'^register/$', views.register, name="register"),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^restricted/$', views.restricted, name='restricted'),
    #url(r'logout/$', views.user_logout, name='logout'),
    #url for counting the number of clicks on article urls
    url(r'^goto/$', views.track_article_url, name='goto'),
    url(r'^goto/$', views.track_article_url, name='goto'),
    url(r'^updatearticles/$', views.update_articles),

    ]
