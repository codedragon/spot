import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser  = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_enter_names_photo_and_search(self):

        # Emily has heard of a cool new site that lets her upload a photo of her
        # dog and look at pictures of her friend's dogs. She goes to check it out.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention the site's name 'spot'
        self.assertIn('Spot', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter her name and her dogs name

        # She types "Emily Elizabeth" into a text box

        # She types "Clifford" into the second text box

        # When she hits enter, the page updates, and the page shows
        # "owner: Emily Elizabeth"
        # "dog: Clifford"

        # There is now a button inviting her to upload a photo of her dog.

        # She presses the button and an upload file dialog box appears.

        # She navigates to a photo of her dog and hits the upload button.

        # The page updates again, and now shows the picture of her dog,
        # along with her name and dog's name.

        # She notices a link to the index, and clicks that.

        # She sees a list of dogs with their name and a resized thumbnail image

        # When she clicks on a dog name display light box that shows:
        # the dog name
        # the dog owner name
        # the original image

        # She sees a search box, and searches for a dog by dog name
 
        # She sees a search box, and searches for a dog by dog owner name.
        
if __name__ == '__main__':
    unittest.main()

