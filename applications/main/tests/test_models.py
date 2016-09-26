import pytest
from mixer.backend.django import mixer

#Don't try to write in the database
pytestmark = pytest.mark.django_db

class TestClubEvent:
    def test_init(self):
        obj=mixer.blend('main.ClubEvent')
        assert obj.pk == 1, 'Should save an isntance'

    #TODO Create other test ....
