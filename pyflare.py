'''

'''
import urllib
import urllib2
import sys
import ConfigParser, os

cloudflare_api_url = "https://www.cloudflare.com/api_json.html"

def usage():
    print "----"
    print "PyFlare is a script to automate CloudFlare's purge."
    print "Usage --"
    print "Configure the pyflare.conf file in this directory with your credentials."
    print "--full-purge : Do a Full Purge"
    sys.exit()

#Load configs from pyflare.conf
def load_conf(conf_file, parameters_a, parameters_v):

    conf_path = conf_path = os.path.dirname(os.path.realpath(__file__)) + conf_file

    config = ConfigParser.RawConfigParser()
    config.readfp(open(conf_path))

    parameters = {
        'a': parameters_a,
        'tkn': config.get("credentials", "CLOUDFLARE_API_KEY"),
        'email':config.get("credentials", "EMAIL"),
        'z':config.get("credentials", "SITE"),
        'v': parameters_v
    }

    return parameters

def full_purge():

    parameters = load_conf("/pyflare.conf", "fpurge_ts", "1")

    print ("Doing a Full Purge of: %s" % (parameters['z']) )

    answer_continue = raw_input("Continue?(Y/N)")

    if answer_continue == "y" or answer_continue == "Y":

        print ("Sending: %s" % (urllib.urlencode(parameters)))
        status_feedback = urllib2.urlopen(cloudflare_api_url, urllib.urlencode(parameters))
        print status_feedback.read()

def main():
    if len(sys.argv) > 1:

        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            usage()

        elif sys.argv[1] == "--full-purge":
            full_purge()

        else:
            print ("%s is not a valid argument." % (sys.argv[1]))
            print ("Use -h or --help for more information")
            sys.exit()

    else:
        print "You need to specify and argument."
        usage()

if __name__ == "__main__":
    main()
