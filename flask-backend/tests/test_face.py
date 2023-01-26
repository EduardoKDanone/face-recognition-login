"""FaceReco Flask integration test"""

import unittest
from src.app import create_app

class TestFace(unittest.TestCase):
    """This class represents the integration test for the Flask Sites"""

    @classmethod
    def setUpClass(self):
        """This method is called before all the tests"""
        self.app = create_app()

        self.app.config.update(
            {
                "TESTING": True,
            }
        )
        self.client = self.app.test_client()

    def test_get_request(self):
        """This method tests the request status code"""
        request = self.client.post("/authenticate")
        print(request.data)
        print(request.status_code)
        self.assertTrue(b'True' in request.data)
        self.assertTrue(request.status_code==200)


if __name__ == "__main__":
    unittest.main()
