from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.NoteListView.as_view(), name="note_list"),
]