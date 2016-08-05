from django.core.urlresolvers import reverse

from oscar.test.testcases import WebTestCase


class ViewTests(WebTestCase):
    is_staff = True

    def test_pages_exist(self):
        urls = [reverse('oscar:dashboard:promotion-list'),
                reverse('oscar:dashboard:promotion-create-rawhtml'),
                reverse('oscar:dashboard:promotion-create-singleproduct'),
                reverse('oscar:dashboard:promotion-create-image'),
               ]
        for url in urls:
            self.assertIsOk(self.get(url))

    def test_create_redirects(self):
        base_url = reverse('oscar:dashboard:promotion-create-redirect')
        types = ['rawhtml', 'singleproduct', 'image']
        for p_type in types:
            url = '%s?promotion_type=%s' % (base_url, p_type)
            self.assertIsRedirect(self.get(url))
