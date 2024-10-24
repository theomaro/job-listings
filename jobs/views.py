from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q
from .models import Job, Application
from .forms import JobApplicationForm, JobSearchForm

# Create your views here.


def index(request):
    try:
        query_set = Job.objects.all()

        # FILTERING
        employment_type = request.GET.get("employment_type", None)
        query_set = (
            query_set.filter(employment_type=employment_type)
            if employment_type
            else query_set
        )

        job_type = request.GET.get("job_type", None)
        query_set = query_set.filter(job_type=job_type) if job_type else query_set

        min_salary = request.GET.get("min_salary", "0")
        max_salary = request.GET.get("max_salary", "1000000")
        query_set = (
            query_set.filter(salary__range=(float(min_salary), float(max_salary)))
            if min_salary and max_salary
            else query_set
        )

        # SORTING
        sort_by = request.GET.get("sort_by", "title")
        sort_in = request.GET.get("sort_in", "asc")
        query_set = (
            query_set.order_by("title", "company")
            if sort_by == "title" and sort_in == "asc"
            else (
                query_set.order_by("-title", "-company")
                if sort_by == "title" and sort_in == "desc"
                else query_set
            )
        )

        query_set = (
            query_set.order_by("company", "title")
            if sort_by == "company" and sort_in == "asc"
            else (
                query_set.order_by("-company", "-title")
                if sort_by == "company" and sort_in == "desc"
                else query_set
            )
        )

        query_set = (
            query_set.order_by("posted_at")
            if sort_by == "posted_at" and sort_in == "asc"
            else (
                query_set.order_by("-posted_at")
                if sort_by == "posted_at" and sort_in == "desc"
                else query_set
            )
        )

        query_set = (
            query_set.order_by("submission_deadline")
            if sort_by == "submission_deadline" and sort_in == "asc"
            else (
                query_set.order_by("-submission_deadline")
                if sort_by == "submission_deadline" and sort_in == "desc"
                else query_set
            )
        )

        query_set = (
            query_set.order_by("is_urgent")
            if sort_by == "is_urgent" and sort_in == "asc"
            else (
                query_set.order_by("-is_urgent")
                if sort_by == "is_urgent" and sort_in == "desc"
                else query_set
            )
        )

        # SEARCHING
        search_form = JobSearchForm(request.GET or None)
        if search_form.is_valid():
            keyword = search_form.cleaned_data.get("keyword")
            location = search_form.cleaned_data.get("location")

            query_set = (
                query_set.filter(
                    Q(title__icontains=keyword)
                    | Q(overview__icontains=keyword)
                    | Q(description__icontains=keyword)
                )
                if keyword
                else query_set
            )

            query_set = (
                query_set.filter(location__icontains=location)
                if location
                else query_set
            )

        return render(
            request,
            "jobs/index.html",
            {
                "jobs": list(query_set),
                "total_jobs": query_set.count(),
                "search_form": search_form,
            },
        )

        # PAGINATION
    except:
        raise Http404()


@login_required
def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        categories = job.categories.all()
        has_applied = False

        applied_job = (
            Application.objects.filter(user=request.user).filter(job=job).count()
        )
        if applied_job:
            has_applied = True

        if request.method == "POST":
            application_form = JobApplicationForm(request.POST)

            if application_form.is_valid():
                application = application_form.save(commit=False)
                application.user = request.user
                application.job = job
                application.save()
                return redirect("jobs:applications")
        else:
            application_form = JobApplicationForm()

        return render(
            request,
            "jobs/detail.html",
            {
                "job": job,
                "categories": categories,
                "application_form": application_form,
                "has_applied": has_applied,
            },
        )
    except:
        raise Http404()


@login_required
def applications(request):
    query_set = Application.objects.filter(user=request.user)
    return render(
        request,
        "jobs/applications.html",
        {"applications": list(query_set), "total_applications": query_set.count()},
    )
