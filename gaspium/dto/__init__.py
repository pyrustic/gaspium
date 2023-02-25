from collections import namedtuple


Context = namedtuple("Context", ("app", "root", "pid", "manager"))

Page = namedtuple("Page", ("pid", "view_class", "view", "title",
                           "category", "indexable", "kwargs"))
