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

    def test_post_request_true(self):
        """This method tests the request status code"""
        data={
            'face':(open('src/assets/images/juan/edu3.png','rb'),'src/assets/images/juan/edu3.png'),
        }
        request = self.client.post("/authenticate",data=data,content_type='multipart/form-data')

        self.assertTrue(b'True' in request.data)
        self.assertTrue(request.status_code==200)

    def test_post_request_false(self):
        """This method tests the request status code and face reconition result"""
        data={
            'face':(open('src/assets/images/juan/Gabe.jpg','rb'),'src/assets/images/juan/Gabe.jpg'),
        }
        request = self.client.post("/authenticate",data=data,content_type='multipart/form-data')
        self.assertTrue(b'False' in request.data)
        self.assertTrue(request.status_code==200)


if __name__ == "__main__":
    unittest.main()
