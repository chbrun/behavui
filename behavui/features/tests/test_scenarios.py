from django.test import TestCase
from ..models import Scenario, Feature
from projects.models import Project


class ScenarioTest(TestCase):

    def setUp(self):
        project1 = Project.objects.create(name="project1")
        feature1 = Feature.objects.create(name="feature1",
                                          description="test",
                                          project=project1)
        scenario1 = Scenario.objects.create(title="scenario1",
                                            feature = feature1,
                                            precondition="",
                                            auto = True,
                                            scenario = "")

    def test_str(self):
        scenario1 = Scenario.objects.get(pk=1)
        self.assertEqual(str(scenario1), "scenario1")

