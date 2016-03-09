from django.conf.urls import url
import views

# pay attention to app_name, will lead change to url part in templates/polls/index.html
#app_name = 'polls'
# <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	# ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]