from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadModelForms, LeadForm
from django.views import generic


class IndexPageView(generic.TemplateView):
    template_name = "index.html"

# def index_page(request):
#     return render(request, "index.html")



class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"




# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         'leads' : leads
#     }
#     return render(request, "leads/lead_list.html", context)



class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, "leads/lead_detail.html", context)



class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForms

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_create(request):
#     form = LeadModelForms()
#     if request.method == "POST":
#         print("Receiving a post request")
#         form = LeadModelForms(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Lead has been created")
#             return redirect("/leads")
#     context = {
#         'form': form
#     }
#     return render(request, "leads/lead_create.html", context)


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForms
    queryset = Lead.objects.all()


    def get_success_url(self):
        return reverse("leads:lead-list")

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForms(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForms(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form" : form,
#         'lead' : lead
#     }
#     return render(request, "leads/lead_update.html", context)


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
