import ConfigParser	
import getpass

class Config:

    config = ConfigParser.ConfigParser()

    @classmethod
    def init(cls, configFileName='sikuliftb.cfg'):
        cls.config.readfp(open('/Users/%s/Documents/%s' % (getpass.getuser(), configFileName)))

    @classmethod
    def get_app_path(cls):
        return cls.config.get('Paths', 'app') 

    @classmethod
    def get_reports_path(cls):
        return cls.config.get('Paths', 'reports')

    @classmethod
    def get_user_data_path(cls):
    	return '/Users/%s/Library/Application Support/com.myheritage.FTBmac' % (getpass.getuser())