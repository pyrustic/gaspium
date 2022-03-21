"""Errors classes"""


class Error(Exception):
    pass


class AppError(Error):
    pass


class AlreadyDefinedError(AppError):
    pass


class AppStateError(AppError):
    pass


class PageError(Error):
    pass


class PageNotFoundError(PageError):
    pass


class DuplicatePageError(PageError):
    pass


class PageStateError(PageError):
    pass
