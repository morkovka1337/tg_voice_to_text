from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")  # bot token
WEBAPPURL = env.str("WEBAPPURL")  # application domain
WEBAPPHOST = env.str("WEBAPPHOST")  # application host
WEBAPPPORT = env.str("WEBAPPPORT")  # application port