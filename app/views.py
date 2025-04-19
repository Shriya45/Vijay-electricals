from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib import messages  # ✅ Add this
from .form import ContactForm
from django.http import JsonResponse
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            phone = form.cleaned_data['phone']

            html = render_to_string('app/emails/contactform.html', {
                'name': name,
                'phone': phone,
                'email': email,
                'message': message
            })

            send_mail(
                subject="The contact form subject",
                message="This is the message",
                from_email="vijayelectricals727@gmail.com",
                recipient_list=["vijayelectricals727@gmail.com"],
                fail_silently=False,
                html_message=html
            )

            messages.success(request, "Message sent successfully!")  
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'app/index.html', {
        'form': form
    })
def chatbot_response(request):
    user_message = request.GET.get("message", "").lower()

    responses = {
        "how are you": "I'm just a bot, but I'm doing great! 😊",
        "bye": "Goodbye! Have a great day! 👋",
    }

    # Handling specific questions about services
    if "service" in user_message:
        reply = "We offer electrical repairs, installations, fan fitting, wiring, lighting, generator installation, and more!"
    elif "schedule" in user_message or "appointment" in user_message:
        reply = "You can schedule an appointment by filling out the contact form on our website or calling us at [9372735170]."
    elif "emergency" in user_message:
        reply = "Yes, we provide 24/7 emergency electrical services. Call us anytime for urgent assistance!"
    elif "appliance installation" in user_message or "installing" in user_message:
        reply = "Absolutely! We can install electrical appliances like air conditioners, ovens, and more. Just let us know your needs."
    elif "rates" in user_message or "price" in user_message:
        reply = "Our rates depend on the type of service you need. For a more accurate estimate, feel free to contact us and we’ll provide a quote based on your requirements."
    elif "contact" in user_message:
        reply = "You can reach us at vijayelectricals727@gmail.com or call on +91 9372735170."
    elif "license" in user_message or "insured" in user_message:
        reply = "Yes, we are fully licensed and insured to provide professional electrical services."
    elif any(word in user_message for word in ["hi", "hey", "hello"]):
        reply = "Hi! How can I assist you?"
    
    # Default response if the question doesn't match any of the predefined ones
    else:
        reply = responses.get(user_message, "Sorry, I don't understand. for any queries fell free to contact us at vijayelectricals727@gmail.com or call on +91 9372735170")
    
    return JsonResponse({"reply": reply})
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://vijay-electricals-hkwv.onrender.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")