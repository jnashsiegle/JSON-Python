'''
Jana Nash-Siegle
10/2/2015
DPW - 01
Event Survey Form - Project 2
'''
import webapp2
from pages import Form #from pages.py import the page class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        event_form = Form()        
        #print event_form.print_out()#this will print out in the google engine console
        if self.request.GET:
        	#storing our info from the user inputs
        	attendee = self.request.GET['attendee']
        	email = self.request.GET['email']
        	self.response.write(event_form.head + attendee + ' ' + email + event_form.close)
        else:	    	
        	self.response.write(event_form.print_out())# this will print out in browser
        #DO NOT DELETE ABOVE LINE










app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)