from django.test import TestCase
from django.core.urlresolvers import reverse
from ..models import Feature
from projects.models import Project


class FeatureTest(TestCase):

    def setUp(self):
        project1 = Project.objects.create(name="Project1")
        Feature.objects.create(name="feature1",
                               description="description feature",
                               project = project1)

    def test_str(self):
        feature1 = Feature.objects.get(name='feature1')
        self.assertEqual(str(feature1), "feature1")

    def test_indexView_feature(self):
        response = self.client.get(reverse('features_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "feature1")

    def test_detailView_feature(self):
        feature1 = Feature.objects.get(name='feature1')
        response = self.client.get(reverse('feature_detail',
                                           args=(feature1.id,)))
        response = self.assertContains(response, "feature1")
