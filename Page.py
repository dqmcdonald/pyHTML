#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 16:40:36 2017

Page - Sets up an HTML page

@author: que
"""

class Page(object):
    """
    Defines an HTML page
    """
    
    def __init__(self,title = " "):
        self.content = []
        self.title = title
        
    
    def __repr__(self):
        """
        Return a printable represnetation of the page and all the contents
        """
        page = """<html>
            <head>
            <meta charset="utf-8">
            <title>%s</title>
            </head>
            <body>
            """ % self.title
        for c in self.content:
            page += c
        page += """
          </body>
          </html>
          """
        return page
          
          
    def addConent(self, content):
        self.content.append(content)
        
    
if __name__ == "__main__":
    
    p = Page("Test Page")
    p.addConent("<H1>Heading 1</H1>")
    
    assert str(p) == """<html>
            <head>
            <meta charset="utf-8">
            <title>Test Page</title>
            </head>
            <body>
            <H1>Heading 1</H1>
          </body>
          </html>
          """
