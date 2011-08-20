from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage


class Hello(BrowserPage):

    template = ViewPageTemplateFile('hello.pt')

    def __call__(self):
        return self.template()
