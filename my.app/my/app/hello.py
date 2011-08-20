from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage


class Hello(BrowserPage):
    """
    Wire up some goo
    """

    template = ViewPageTemplateFile('hello.pt')

    def __call__(self):
        return self.template()
