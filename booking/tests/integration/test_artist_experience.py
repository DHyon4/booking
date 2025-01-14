from django.urls import reverse

from tests.utils import OpusTestCase

import sure
from sure import expect

from unittest import skip


class ArtistExperienceTest(OpusTestCase):

    @skip("This will need to be tested in React. Leaving as a reminder.")
    def test_logo_link(self):

        url = reverse('musician_dash')
        result = self.app.get(url, user=self.m.user.username)

        href = result.html.find_all("a", class_='logo')[0].attrs['href']
        href.should.equal(reverse('musician_dash'))

