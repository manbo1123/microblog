from django.test import TestCase, Client
# トップページへのアクセス
class BlogTestCase(TestCase):
  def setUp(self):
    self.c = Client()

  def test_index_access(self):
    res = self.c.get('/')
    # status code => 200（成功）、404(見つからない場合)、302(リダイレクト)
    self.assertEqual(200, res.status_code)

  def test_fail_access(self):
    res = self.c.get('/unknown')
    self.assertEqual(404, res.status_code)