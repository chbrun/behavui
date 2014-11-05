from django.test import TestCase
from ..models import Project


class ProjectTest(TestCase):

    def setUp(self):
        Project.objects.create(name="test")

    def test_str(self):
        project1 = Project.objects.get(name="test")
        self.assertEqual(str(project1), "test")
