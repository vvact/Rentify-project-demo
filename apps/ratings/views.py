from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.profiles.models import Profile
from .models import Rating

User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    try:
        agent_profile = Profile.objects.get(id=profile_id, is_agent=True)
    except Profile.DoesNotExist:
        return Response(
            {"message": "Agent not found"}, status=status.HTTP_404_NOT_FOUND
        )

    profile_user = User.objects.get(pkid=agent_profile.user.pkid)

    if profile_user.email == request.user.email:
        return Response(
            {"message": "You can't rate yourself"}, status=status.HTTP_403_FORBIDDEN
        )

    already_exists = agent_profile.agent_review.filter(
        agent__pkid=profile_user.pkid
    ).exists()

    if already_exists:
        return Response(
            {"message": "You have already rated this agent"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    data = request.data

    if data.get("rating") == 0:
        return Response(
            {"message": "Please select a rating"}, status=status.HTTP_400_BAD_REQUEST
        )

    review = Rating.objects.create(
        agent=agent_profile,
        user=request.user,
        rating=data["rating"],
        comment=data["comment"],
    )

    reviews = agent_profile.agent_review.all()
    agent_profile.num_reviews = reviews.count()

    total = sum(review.rating for review in reviews)
    agent_profile.average_rating = total / agent_profile.num_reviews
    agent_profile.save()

    return Response({"message": "Review Added"}, status=status.HTTP_201_CREATED)
