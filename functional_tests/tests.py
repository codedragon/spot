from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser  = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def test_can_enter_names_photo_and_search(self):

        # Emily has heard of a cool new site that lets her upload a photo of her
        # dog and look at pictures of her friend's dogs. She goes to check it out.
        self.browser.get(self.live_server_url)

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
        
        # When she hits the submit button, she is re-directed to a page that 
        # shows the info she just submitted
        # "owner: Emily Elizabeth"
        # "dog: Clifford"
        
        submitbutton = self.browser.find_element_by_id('id_submit')
        self.assertEqual(
            submitbutton.get_attribute('placeholder'),
            "Click to Continue"
            )
        submitbutton.click()
        
        emily_elizabeth_url = self.browser.current_url
        self.assertRegexpMatches(emily_elizabeth_url, '/stats/.+')
        
        table = self.browser.find_element_by_id('id_owner_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Owner: Emily Elizabeth', [row.text for row in rows])
        self.assertIn('Dog: Clifford', [row.text for row in rows])

        # Fred Flinstone now visits the home page. 
        self.browser.quit()
        ## We use a new browser session to make sure that no info is 
        ## coming through from cookies, etc.
        self.browser = webdriver.Firefox()
        
        # There is no sign of Elizabeths stats.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Emily', page_text)
        self.assertNotIn('Elizabeth', page_text)
        self.assertNotIn('Clifford', page_text)

        # Fred enters his name and his dogs name and hit a submit button
        inputbox = self.browser.find_element_by_id('id_new_first_name')
        inputbox.send_keys('Fred')
        inputbox = self.browser.find_element_by_id('id_new_last_name')        
        inputbox.send_keys('Flinstone')
        inputbox = self.browser.find_element_by_id('id_new_dog_name')        
        inputbox.send_keys('Dino')        
        
        # When he hits the submit button, he is re-directed to a page with
        # a unique URL that shows the info he just submitted
        # "owner: Fred Flinstone"
        # "dog: Dino"
        
        submitbutton = self.browser.find_element_by_id('id_submit')
        submitbutton.click()
        fred_flinstone_url = self.browser.current_url
        self.assertRegexpMatches(fred_flinstone_url, '/stats/.+')
        self.assertNotEqual(fred_flinstone_url, emily_elizabeth_url)
        
        # again, there is no trace of Emily's info
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Emily', page_text)
        self.assertNotIn('Elizabeth', page_text)
        self.assertNotIn('Clifford', page_text)
        
        # There is now a button inviting her to upload a photo of her dog, 

        element = self.browser.find_element_by_id('file_upload')
        element.send_keys('~/Desktop/sebastian.JPG')
        #Assert that we have something returned as expected
        self.assertNotEqual(element,None)

        self.fail('Finish the test!')
        
        # She presses the button and an upload file dialog box appears.

        # She navigates to a photo of her dog and hits the upload button.

        # The page updates, and now shows the picture of her dog,
        # along with her name and dog's name.

        # She notices a link to the index, and clicks that.

        # She sees a list of dogs with their name and a resized thumbnail image,
        # including hers and Fred Flinstone's.

        # When she clicks on a dog name display light box that shows:
        # the dog name
        # the dog owner name
        # the original image

        # She sees a search box, and searches for a dog by dog name
 
        # She sees a search box, and searches for a dog by dog owner name.
        

