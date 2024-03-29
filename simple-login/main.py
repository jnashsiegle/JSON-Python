'''
Jana Nash-Siegle
9/28/2015
DPW - 01
Simple Log-In Form B
So, in essence this page is using links rather than a form.  IOW if you know the information you can use the information this way rather than requesting the information from the user via a form.
'''
import webapp2 #use the webapp2 library - needed for basic functionality

class MainHandler(webapp2.RequestHandler): #Declares a class
    def get(self): #function that starts everything, catalyst, invokes
    	
		page_head = '''<!DOCTYPE HTML>
    <html>
    	<head>
    		<title>Simple Form!</title>
    	</head>
    		<body>'''

		page_body = '''
		<a href = "?email=mickey@disney.com&user=Mickey">Mickey</a><br />
		<a href = "?email=donald@disney.com&user=Donald">Donald</a><br />
		<a href = "?email=minnie@disney.com&user=Minnie">Minnie</a><br />
		<a href = "?email=daisy@disney.com&user=Daisy">Daisy</a>



		'''
		page_close = '''
    		</form>
    	</body>
    </html>'''


   		if self.request.GET: #same as adding == True: to the end of it.  We are giving it a condition of if the variable exists then print out the following information
   		#print self.request.GET['user'] #gets the information that will be entered into the page, has to match the name of the element
   		#print "hello there" testing of print
   		#the two lines below store the information into variables
	    		user = self.request.GET['user'] #if we want more than the above console printing let's store it in a variable called user
	    		email = self.request.GET['email']
	    		self.response.write(page_head + user + ' ' + email + page_close)#print  if you don't want to print form again just results, take out the page_body and it will print only the user inputs
	    	else:
	    		self.response.write(page_head + page_body + page_close)#print


    #self.response.write(page) #prints our information out onto the page

        

        






#leave alone, DO NOT TOUCH BELOW THIS LINE
app = webapp2.WSGIApplication([ 
    ('/', MainHandler)
], debug=True)
