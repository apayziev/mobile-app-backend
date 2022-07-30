
from rest_framework.response import Response
from rest_framework import views
from rest_framework.permissions import IsAuthenticated

from common.models import User 
from course.models import Course, CourseAuthor, Category


class HomePageView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        greeting = f"Hola,  {user.first_name}"

        # popular categories
        popular_categories = Category.objects.filter(is_popular=True)

        # most viewed categories
        most_viewed_categories = Category.objects.filter(is_most_viewed=True)

        # top authors
        top_authors = CourseAuthor.objects.filter(is_top=True)

        # best selling and new courses
        best_selling_courses = Course.objects.filter(is_best_seller=True)
        new_courses = Course.objects.filter(is_new=True)


        context = {
            "greeting": greeting,
            "popular_categories": popular_categories,
            "most_viewed_categories": most_viewed_categories,
            "top_authors": top_authors,
            "best_selling_courses": best_selling_courses,
            "new_courses": new_courses,
        }

        return Response(context)