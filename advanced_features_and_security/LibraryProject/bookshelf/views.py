
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import YourModel

@permission_required('bookshelf.can_view', raise_exception=True)
def your_view(request):
    # view logic
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_view(request, pk):
    obj = get_object_or_404(YourModel, pk=pk)
    # edit logic

