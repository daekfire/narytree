from django.core.exceptions import ValidationError
from django.test import TestCase

from tree.models import Node, Tree


class TestTree(TestCase):

    def test_create_child(self):
        parent = Node.objects.create()
        tree = Tree.objects.create(parent_node=parent)

        child = Node.objects.create(parent=parent)

        self.assertEqual(child.parent, parent)
        self.assertEqual(parent.children.all()[0], child)

    def test_create_too_many_children(self):
        parent = Node.objects.create()
        tree = Tree.objects.create(parent_node=parent)

        child = Node.objects.create(parent=parent)
        child2 = Node.objects.create(parent=parent)
        child3 = Node.objects.create(parent=parent)
        with self.assertRaises(ValidationError):
            child4 = Node.objects.create(parent=parent)

    def test_create_re_save_3_children(self):
        parent = Node.objects.create()
        tree = Tree.objects.create(parent_node=parent)

        child = Node.objects.create(parent=parent)
        child2 = Node.objects.create(parent=parent)
        child3 = Node.objects.create(parent=parent)

        child3.save()

    def test_create_re_save_parent_with_3_children(self):
        parent = Node.objects.create()
        tree = Tree.objects.create(parent_node=parent)

        child = Node.objects.create(parent=parent)
        child2 = Node.objects.create(parent=parent)
        child3 = Node.objects.create(parent=parent)

        parent.save()

