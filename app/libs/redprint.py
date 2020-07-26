"""
  *@ClassName redprint
  *@Description TODO
  *@Author to2bage
  *@Date 2020-07-26 10:30
  *@Version 1.0
 """
from flask import Blueprint


class Redprint:

    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((rule, f, options))
            return f
        return decorator

    def register(self, blueprint: Blueprint, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for rule, f, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            blueprint.add_url_rule(url_prefix + rule, endpoint, f, **options)
        pass
