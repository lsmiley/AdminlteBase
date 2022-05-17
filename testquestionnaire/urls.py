from django.urls import path
# from django.conf.urls import url
from . import views
from .views import (TestquestionnaireUpdateView, CreateTestquestionnaireView

                    )


urlpatterns = [

    path('update/<int:pk>/', TestquestionnaireUpdateView.as_view(), name='update_testquestionnaire'),

    path('', views.TestquestionnaireListView.as_view(), name='testquestionnaire'),
    path('testquestionnaire/new', views.TestquestionnaireCreateView.as_view(), name='new-testquestionnaire'),
    path('testquestionnaire/<pk>/edit', views.TestquestionnaireUpdateView.as_view(), name='edit-testquestionnaire'),
    path('testquestionnaire/<pk>/delete', views.TestquestionnaireDeleteView.as_view(), name='delete-testquestionnaire'),

    # # ***** Questionnaire URL Section  ***
    # path('questionnaire', QuestionnaireView.as_view(), name='questionnaire'),
    # path('dashboard-questionnaire/', DashboardQuestionnaireView.as_view(), name='dashboard_questionnaire'),
    path('create_questionnaire/', CreateTestquestionnaireView.as_view(),name='create-questionnaire'),
    path('update_testquestionnaire/<int:pk>/', TestquestionnaireUpdateView.as_view(), name='update_testquestionnaire'),

    # path('testpdf/', views.TestGeneratePdf.as_view()),
    # path('testgeneratequestionnairepdf/', Testgeneratequestionnairepdf.as_view()),
]
