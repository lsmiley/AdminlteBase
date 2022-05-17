from django.urls import path
# from django.conf.urls import url
from . import views
from .views import (QuestionnaireUpdateView, QuestionnaireListView, QuestionnaireCreateView, QuestionnaireDeleteView,
                    CreateQuestionnaireView, )


urlpatterns = [

    path('update/<int:pk>/', QuestionnaireUpdateView.as_view(), name='update_questionnaire'),

    path('', views.QuestionnaireListView.as_view(), name='questionnaire'),
    path('questionnaire/new', views.QuestionnaireCreateView.as_view(), name='new-questionnaire'),
    path('questionnaire/<pk>/edit', views.QuestionnaireUpdateView.as_view(), name='edit-questionnaire'),
    path('questionnaire/<pk>/delete', views.QuestionnaireDeleteView.as_view(), name='delete-questionnaire'),

    # # ***** Questionnaire URL Section  ***
    # path('questionnaire', QuestionnaireView.as_view(), name='questionnaire'),
    # path('dashboard-questionnaire/', DashboardQuestionnaireView.as_view(), name='dashboard_questionnaire'),
    path('create_questionnaire/', CreateQuestionnaireView.as_view(),name='create-questionnaire'),
    path('update_questionnaire/<int:pk>/',QuestionnaireUpdateView.as_view(), name='update_questionnaire'),


]
