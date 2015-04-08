import string, random
import datetime

def generate_random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_project_name():
	return datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")