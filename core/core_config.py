import ConfigParser
import os


class CoreConfig(object):

    def __init__(self, input_path, output_path):
    
        self.path = input_path
        self.hostapd_conf_path = output_path

        self.config = ConfigParser.ConfigParser()
        self.config.read(self.path)

    def sections(self):
        
        for section in self.config.sections():
            yield section

    def items(self, section=None):

        if section is not None:

            for item in self.config.items(section):
                yield item
            raise StopIteration

        for section in self.sections():
            for item in self.items(section=section):
                yield item

    def get(self, section, setting):
        return self.config.get(section, setting)

    def update(self, section, setting, value):
        
        self.config.set(section, setting, value)

        with open(self.path, 'wb') as fd:
            self.config.write(fd)

    def write(self):

        with open(self.hostapd_conf_path, 'w') as fd:
            for key,val in self.items():
                fd.write('%s=%s\n' % (key,val))

    def delete(self, section, setting=None):

        if setting is not None:
            self.config.remove_option(section, setting)
        else:
            for key,val in self.items(section):
                self.config.remove_option(section, key)

        with open(self.path, 'wb') as fd:
            self.config.write(fd)

if __name__ == '__main__':

    conf = HostapdConfig()

    conf.delete('static')



