class Error(Exception):
    pass


class PageNotFoundError(Error):
    pass


class DuplicatePageError(Error):
    pass


class PageStateError(Error):
    pass


class AlreadyDefinedError(Error):
    pass


class DuplicateComponentError(Error):
    pass


class ComponentNotFoundError(Error):
    pass


class ComponentInterfaceError(Error):
    pass
