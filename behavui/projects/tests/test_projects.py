from django.test import TestCase
from django.core.urlresolvers import reverse
from ..models import Project


class ProjectTest(TestCase):

    def test_str(self):
        project1 = Project.objects.create(name="test")
        self.assertEqual(str(project1), "test")

    def test_indexView_with_no_projects(self):
        response = self.client.get(reverse('projects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
