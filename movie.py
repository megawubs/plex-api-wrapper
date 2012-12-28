from info import Info

class Movie(object):
    
    def __init__(self, element, server):
        self.server = server
        self.element = element
        # browse element and extract some information
        self.key = element.attrib['key']
        self.type = 'movie'
        info = Info(self).info
        for k in info:
            setattr(self.__class__, k,  info[k])
    
    def __str__(self):
        return "<Movie: %s (%s)>" % (self.title, self.year)
    
    def __repr__(self):
        return "<Movie: %s (%d)>" % (self.title, self.year)
    
    
