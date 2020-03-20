# Create your tests here.

from django.test import TestCase
from .models import LeaderBoard

class ViewsTest(TestCase):

    def setUp(self):
        LeaderBoard.objects.create(client="客户端1",score=10)
        LeaderBoard.objects.create(client="客户端2",score=20)
        LeaderBoard.objects.create(client="客户端3",score=30)

    def test_leader_board_get(self):
        response = self.client.get('/api/client/leader_board',data={
            "start":0,
            "end":10,
            "client":"客户端3",
        })
        self.assertEqual(response.status_code, 200)

    def test_leader_board_post(self):
        response = self.client.post('/api/client/leader_board',data={
            "client":"客户端4",
            "score":50,
        })
        self.assertEqual(response.status_code, 200)



