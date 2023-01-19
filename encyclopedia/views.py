from django.shortcuts import redirect, render
from markdown2 import markdown
from random import choice

from . import util



def index(request):
    if request.method == "POST":
        all_entries = util.list_entries()
        search_string = request.POST.get("new_search")
        search_result = []
        for entry in all_entries:
            if search_string.lower() == entry.lower():
                return redirect("encyclopedia:entry", entry)
            if search_string.lower() in entry.lower():
                search_result.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": search_result,
            "title": "Search results"
        })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    if request.method=="POST":
        return render(request, "encyclopedia/new_page.html", {
            "edit_name": name,
            "edit_content": util.get_entry(name)
        })
        
    else:
        # method is GET
        if name.lower() in [title.lower() for title in util.list_entries()]:
            content = markdown(util.get_entry(name))
        else:
            content = None
        return render(request, "encyclopedia/entry.html", {
            "title": name,
            "content": content
        })


def random_entry(request):
    name = choice(util.list_entries())
    return redirect("encyclopedia:entry", name)


def new_page(request):
    if request.method == "POST":
        entry_title = request.POST.get("new_title")
        entry_content = request.POST.get("new_content")
        edit = request.POST.get("edit")

        if edit == "Submit entry" and entry_title.lower() in [title.lower() for title in util.list_entries()]:
            return render(request, "encyclopedia/new_entry_error.html")
        else:
            util.save_entry(entry_title, entry_content)
            return redirect("encyclopedia:entry", entry_title)
    else:
        # method is GET
        return render(request, "encyclopedia/new_page.html", {
            "edit_name": None,
            "edit_content": None
        })