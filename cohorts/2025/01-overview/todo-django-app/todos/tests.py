from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoWorkflowTests(TestCase):
    def test_create_edit_toggle_delete(self):
        # Create a todo (omit 'completed' so it defaults to False)
        create_resp = self.client.post(
            reverse('todo_add'),
            {
                'title': 'Test Task',
                'description': 'A test todo',
                'due_date': '2025-12-31',
            },
        )
        self.assertEqual(create_resp.status_code, 302)

        todo = Todo.objects.get(title='Test Task')
        self.assertIsNotNone(todo)
        self.assertFalse(todo.completed)
        self.assertEqual(str(todo.due_date), '2025-12-31')

        # Edit the todo: change title, mark completed and change due date
        edit_resp = self.client.post(
            reverse('todo_edit', args=[todo.pk]),
            {
                'title': 'Updated Task',
                'description': 'Edited description',
                'due_date': '2026-01-01',
                'completed': 'on',
            },
        )
        self.assertEqual(edit_resp.status_code, 302)

        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated Task')
        self.assertTrue(todo.completed)
        self.assertEqual(str(todo.due_date), '2026-01-01')

        # Toggle completion (should flip to False)
        toggle_resp = self.client.get(reverse('todo_toggle', args=[todo.pk]))
        self.assertEqual(toggle_resp.status_code, 302)
        todo.refresh_from_db()
        self.assertFalse(todo.completed)

        # Delete the todo via the confirm-delete POST
        delete_resp = self.client.post(reverse('todo_delete', args=[todo.pk]))
        self.assertEqual(delete_resp.status_code, 302)
        self.assertFalse(Todo.objects.filter(pk=todo.pk).exists())
