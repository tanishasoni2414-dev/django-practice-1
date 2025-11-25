from django.shortcuts import render
from django.http import HttpResponse
from addCourses.models import Courses
from addInstructors.models import Instructors
from contactApp.models import Contact
from mediaApp.models import Media
# from addCourses.models import Course
# from addInstructors.models import Instructor
# from testimonial.models import Testimonial
from django.core.mail import send_mail
from django.template.loader import render_to_string
from tanisha.settings import DEFAULT_FROM_EMAIL
from django.conf import settings
import requests

from testimonial.models import Testimonial
# Create your views here.


def api_product(request):
    url = 'https://dummyjson.com/products'
    product = []
    response = requests.get(url)
    if response.status_code == 200:
        product = response.json()
    return render(request, 'product.html', {'product': product})
def hello_message(request):
    courses = Courses.objects.all()
    instructors = Instructors.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, "index.html", {'courses': courses, 'instructors': instructors, 'testimonials': testimonials})
def about(request):
    return render(request, "about.html")  
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        alldata = Contact(name=name, email=email, subject=subject, message=message)
        alldata.save()

        # Prepare reply email (plain + HTML)
        reply_subject = f"Thanks for contacting us, {name}"
        plain_message = (
            f"Dear {name},\n\n"
            "Thank you for contacting us. We have received your message and will get back to you shortly.\n\n"
            f"{message}\n\n"
            "Best regards,\n"
            "Tannu Support Team"
        )
        html_message = render_to_string("email_send.html", {"name": name, "message": message})

        # Send confirmation to user
        send_mail(
            reply_subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
            html_message=html_message,
        )

        # Send copy to admin
        admin_subject = f"New Contact Form Submission from {name}"
        admin_message = (
            f"New message received from contact form:\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Subject: {subject}\n\n"
            f"Message:\n{message}\n"
        )
        send_mail(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)

    return render(request, "contact.html")
def courses(request):
    courses = Courses.objects.all()
    instructors = Instructors.objects.all()
    return render(request, "courses.html", {'courses': courses, 'instructors': instructors})
def team(request):
    return render(request, "team.html")
def testimonial(request):
    return render(request, "testimonial.html")  
def error404(request):
    return render(request, "404.html")
def blog(request):
    medias = Media.objects.order_by('-upload_date')
    return render(request, "blog.html", {'medias': medias})


def test_mail(request):
    send_mail(
        subject = "Testing mail",
        message = "this is test mail",
        from_email = "tanishasoni2414@gmail.com",
        recipient_list = ["devendrakhatik412@gmail.com"],
        fail_silently =False,
             
    )
    return HttpResponse("<h1>send</h1>")

