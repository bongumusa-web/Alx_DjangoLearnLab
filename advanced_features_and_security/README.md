# 🛡️ Permissions and Groups Setup in Django

This Django project demonstrates how to manage **custom permissions** and **user groups** to control access to different parts of the application.

---

## 👥 Groups & Permissions Configuration

### Groups Created:

- **Viewers** – can only view model instances (`can_view`)
- **Editors** – can view and modify content (`can_view`, `can_edit`, `can_create`)
- **Admins** – full access (`can_view`, `can_edit`, `can_create`, `can_delete`)

### Custom Permissions Defined:
Defined in the `Meta` class of a model (e.g., `models.py`):

- `can_view` – View permission
- `can_create` – Add/create permission
- `can_edit` – Edit/change permission
- `can_delete` – Delete/remove permission

---

## 🔐 Enforcing Permissions

Relevant views are protected using the `@permission_required` decorator in `views.py`, like so:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    ...
