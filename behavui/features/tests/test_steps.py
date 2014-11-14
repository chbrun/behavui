from django.test import TestCase
from ..models import Feature, Scenario, Step
from projects.models import Project


class StepTest(TestCase):

    def setUp(self):
        project1 = Project.objects.create(name="project1")
        feature1 = Feature.objects.create(name="feature1",
                                          description="description1",
                                          project=project1)
        scenario1 = Scenario.objects.create(title="scenario1",
                                            feature=feature1,
                                            precondition="",
                                            auto=True,
                                            scenario="")
        Step.objects.create(scenario=scenario1,
                            order=1,
                            action="",
                            result="")

    def test_str(self):
        step1 = Step.objects.get(pk=1)
        self.assertEqual(str(step1), "step 1 de scenario1")
