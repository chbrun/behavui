from django.test import TestCase
from django.core.urlresolvers import reverse
from ..models import Campaign
from projects.models import Project


class CampaignTest(TestCase):

    def test_str(self):
        project1 = Project.objects.create(name="project1")
        campaign1 = Campaign.objects.create(name="campaign1",
                                            description="description1",
                                            project=project1)
        self.assertEqual(str(campaign1), "campaign1")

    def test_indexView_with_no_campaigns(self):
        response = self.client.get(reverse('campaigns_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
