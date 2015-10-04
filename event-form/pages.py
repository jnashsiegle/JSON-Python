class Form(object):
	def __init__(self):
		self.head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>Event Planning Survey</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>"""

		self.header = '''
		<header><h1>Acme Web Workshop Event Planning Survey</h1>
		<p><a href = "bing.com">Exit Survey</a></p>
		</header>'''
		self.body = '''<article id = "wrapper">
									
						<h3>Thank you for signing up for our next workshop.</h3> <p> Would you take a moment to fill out this survey so we may learn how to better serve you?</p>
					
					
					<form method = "GET">
						<div id = "personalInfo">
							<label>Name: </label><input type = "text" placeholder = "Enter Your Name" name = "attendee" />
							<label>Email: </label><input type = "text" placeholder = "yourname@domain.com" name = "email" />
						</div>
						<div id = "workshops">
							<label>Which workshop will you be attending?</label>
								<select name = "workshops">
									<option value = "">Click here to see options</option>
									<option value = "css">CSS</option>
									<option value = "html">HTML</option>
									<option value = "js">JavaScript</option>
									<option value = "python">Python</option>
								</select>
							
						</div>

						<div id = "registration">
						<label>How did you hear about this event?</label><input type = "text" placeholder = "I heard about this..." name = "hear" />
						<p>How easy was the registration process for this event?></p>
						<label>Very Easy</label><input type = "radio" name = "rp" value = "very easy" checked/>
						<label>Easy</label><input type = "radio" name = "rp" value = "easy"/>
						<label>Slightly Confusing</label><input type = "radio" name = "rp" value = "slightly confusing"/>
						<label>Hard</label><input type = "radio" name = "rp" value = "hard"/>
						<label>Very Hard</label><input type = "radio" name = "rp" value = "very hard" />
						<label>Comments about the registration process: </label><input type = "text" placeholder = "Make comments here" name = "rpComments" />
						</div>
						<p>Do you have any dietary restrictions?</p>
						<label>Yes</label><input type = "radio" name = "diet" value = "Yes I have diet restrictions"/>
						<label>No</label><input type = "radio" name = "diet" value = "No, I have no diet restrictions" checked/>
						<p>if yes, please enter details: </p>
						<label>Details: </label><input type = "text" placeholder = "I have the following restrictions..." name = "dietDetails" />
						<label>Who will be paying for you to attend this event?</label><input type = "text" placeholder = "...will be paying for this event" name = "payment">
						<p>What is the preferred method of contacting you in regards to this event?</p>
						<label>E-Mail</label><input type = "radio" name = "communication" value = "email" checked/>
						<label>Phone</label><input type = "radio" name = "communication"  value = "phone"/>
						<label>Snail Mail</label><input type = "radio" name = "communication" value = "snail mail" />
						<p>What is your interest in these workshops?</p>
						<label>Career</label><input type = "checkbox" name = "purpose" value = "career" checked />
						<label>Passion</label><input type = "checkbox" name = "purpose" value = "passion" />
						<label>Hobby</label><input type = "checkbox" name = "purpose" value = "hobby" />

						
						<input type = "submit" value = "Submit" />
		'''
		self.close = '''
					</form>
				</article>
	</body>
</html>'''
		
	    
	
	def print_out(self):
		all =  self.head + self.header +  self.body + self.close
		all = all.format(**locals())
		return all