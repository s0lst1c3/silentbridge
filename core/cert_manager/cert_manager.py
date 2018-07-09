import os
import cert_manager_templates as cnf_templates

import settings.paths

class cert_cnf(object):

    @classmethod
    def configure(cls,
            country=None,
            state=None,
            locale=None,
            org=None,
            email=None,
            cn=None):
    
        with open(cls.path, 'w') as fd:
            fd.write(cls.template %\
                (country, state, locale, org, email, cn))

class client_cnf(cert_cnf):

    path = settings.paths.CLIENT_CNF
    template = cnf_templates.client_cnf

class server_cnf(cert_cnf):

    path = settings.paths.SERVER_CNF
    template = cnf_templates.server_cnf

class ca_cnf(cert_cnf):

    path = settings.paths.CA_CNF
    template = cnf_templates.ca_cnf

def bootstrap(): 
    os.system(settings.paths.BOOTSTRAP_FILE)

