from django.urls import path

from .views import (
    AgentListAPIView,
    GetProfileAPIView,
    TopAgentsListAPIView,
    UpdateProfileAPIView,
)

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("agents/all/", AgentListAPIView.as_view(), name="agent_list"),
    path("me/update/", UpdateProfileAPIView.as_view(), name="update_profile"),
    path("agents/top/", TopAgentsListAPIView.as_view(), name="top_agents_list"),
]
