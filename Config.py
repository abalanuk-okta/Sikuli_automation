import ConfigParser	

class Config:

	config = ConfigParser.ConfigParser()

	@classmethod
	def init(cls, configFileName='/Users/bohdanivanov/Projects/Demos/Sikuli_automation/sikuliftb.cfg'):
		cls.config.readfp(open(configFileName))
		
	@classmethod
	def get_app_path(cls):
		return cls.config.get('Paths', 'app') 

	@classmethod
	def get_reports_path(cls):
		return cls.config.get('Paths', 'reports')