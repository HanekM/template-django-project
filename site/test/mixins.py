from django.http import HttpResponse

from . import status


class TestCheckMixin():

    def perform_common_check(
            self, response: HttpResponse,
            expected_type='text/html', expected_status=status.HTTP_200_SUCCESS
        ):
        self.assertIn(
            expected_type, response.get('content-type'), 'Unexpected content type.'
        )
        self.assertEquals(response.status_code, expected_status)
