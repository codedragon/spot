import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Spot', header_text)

        # She is invited to enter her name and her dogs name and hit a submit button
        inputbox = self.browser.find_element_by_id('id_new_first_name')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your first name'
            )
        # She types "Emily" into the text box
        inputbox.send_keys('Emily')
        
        inputbox = self.browser.find_element_by_id('id_new_last_name')        
        self.assertEqual(        
            inputbox.get_attribute('placeholder'),
            'Enter your last name'
            )
        # She types "Elizabeth" into the second text box
        inputbox.send_keys('Elizabeth')

        inputbox = self.browser.find_element_by_id('id_new_dog_name')        
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "Enter your dog's name"
            )
        # She types "Clifford" into the third text box
        inputbox.send_keys('Clifford')        
        
        # When she hits the submit button, the page updates, and the page shows
        # "owner: Emily Elizabeth"
        # "dog: Clifford"
        
        submitbutton = self.browser.find_element_by_id('id_submit')
        self.assertEqual(
            submitbutton.get_attribute('placeholder'),
            "Click to Continue"
            )
        submitbutton.click()
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Owner: Emily Elizabeth', [row.text for row in rows])
        self.assertIn('Dog: Clifford', [row.text for row in rows])

        # There is now a button inviting her to upload a photo of her dog, 

        self.fail('Finish the test!')
        
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

