"""The App class is defined inside this module."""
import sys
import platform
import tkinter as tk
import tkutil
from gaspium import error
from gaspium import misc
from cyberpunk_theme import get_theme


class App:
    """This class is the entry point of your Gaspium app"""
    def __init__(self, title="Application", geometry="800x500",
                 theme=get_theme(), caching=False,
                 resizable=(True, True), on_stop=None, on_exit=None,
                 crash_resistant=True, navbar=misc.Navbar):
        """
        Initialization.

        [parameters]
        - title: string, the title of the app

        - geometry: str, to specify the geometry. Put "max" to maximize the window. Example: "800x400", "800x400+0+0", "+0+0", "max"

        - theme: the theme, i.e. an instance of tkstyle.Theme

        - caching: boolean to tell if whether you want pages to be cached or re-built at open.

        - resizable: 2-tuple of booleans to tell if you want the width and the height of the app to be resizable.

        - on_stop: the on_stop handler, i.e. a function that will be called when the app is going to close.
        This function should accept an argument: the app instance

        - on_exit: the on_exit handler, i.e. a function that will be called when the app is going to exit.
        This function should accept an argument: the app instance

        - crash_resistant: boolean, set it to True if you don't want the GUI to close when a random exception is raised

        - navbar: navigation bar class. The constructor must accept the app instance.
        The class must have an "add" method that accepts these arguments: pid, title, and category
        """
        self._title = title
        self._geometry = geometry
        self._theme = theme
        self._caching = caching
        self._resizable = resizable
        self._on_stop = on_stop
        self._on_exit = on_exit
        self._root = None
        self._init_root()
        self._pages = {}
        self._pid = None
        self._navbar = navbar(self) if navbar else None
        self._started = False
        self._stopped = False
        self._i = 0
        self._data = dict()
        self._crash_resistant = crash_resistant
        self._cached_report_callback_exception = None
        self._home_pid = None
        self._opening_pages_count = 0
        self._closing_page = False
        self._opening_page = False
        self._delayed_open_request = []
        self._setup()

    @property
    def title(self):
        """
        Return the title of the app
        """
        return self._title

    @title.setter
    def title(self, val):
        """
        Set the title of the app
        """
        if self._started and self._title:
            raise error.AlreadyDefinedError
        self._title = val

    @property
    def geometry(self):
        """
        Return the geometry of the app
        """
        return self._geometry

    @geometry.setter
    def geometry(self, val):
        """
        Set the geometry of the app
        """
        if self._started and self._geometry:
            raise error.AlreadyDefinedError
        self._geometry = val

    @property
    def theme(self):
        """
        Return the current theme
        """
        return self._theme

    @theme.setter
    def theme(self, val):
        """
        Set a theme, i.e., a tkstyle.Theme instance
        """
        self._theme = val
        self._apply_theme()

    @property
    def caching(self):
        """
        Return a boolean to indicate if the caching option is set to True or False.
        """
        return self._caching

    @caching.setter
    def caching(self, val):
        """
        Set True if you want pages to be cached. Cached pages retains their data.
        """
        if self._started and self._caching:
            raise error.AlreadyDefinedError
        self._caching = val

    @property
    def resizable(self):
        """
        Return the resizable booleans tuple
        """
        return self._resizable

    @resizable.setter
    def resizable(self, val):
        """
        Set the resizable booleans tuple
        """
        if self._started:
            raise error.AlreadyDefinedError
        self._resizable = val

    @property
    def on_stop(self):
        """
        Return the on_stop callback
        """
        return self._on_stop

    @on_stop.setter
    def on_stop(self, val):
        """
        Set the on_stop handler. The handler is a function that accepts the app instance as argument
        """
        if self._started and self._on_stop:
            raise error.AlreadyDefinedError
        self._on_stop = val

    @property
    def on_exit(self):
        """
        Return the on_exit callback
        """
        return self._on_exit

    @on_exit.setter
    def on_exit(self, val):
        """
        Set the on_exit handler. The handler is a function that accepts the app instance as argument
        """
        if self._started and self._on_exit:
            raise error.AlreadyDefinedError
        self._on_exit = val

    @property
    def crash_resistant(self):
        """Get the crash_resistant boolean"""
        return self._crash_resistant

    @crash_resistant.setter
    def crash_resistant(self, val):
        """Set the crash_resistant boolean"""
        self._crash_resistant = val

    @property
    def pid(self):
        """
        Return the currently opened Page ID
        """
        return self._pid

    @property
    def pages(self):
        """
        Return the copy of an internal dictionary that contains pages information.
        Note: Keys are PIDs (Page ID)
        """
        return self._pages.copy()

    @property
    def root(self):
        """
        Return the root, i.e. the Tkinter's Tk instance that serves as the root of this app.
        """
        return self._root

    @property
    def data(self):
        """
        This is an empty dictionary linked to this app.
        Use it to store whatever you want.
        Example: you can use it to retain the information about whether
         the user is authenticated or not.
        """
        return self._data

    def add(self, view, pid=None, title=None, category=None,
            indexable=True, on_open=None, on_close=None):
        """
        Add a new page to the app. This method will generate a new page instance then
        will call the layout function to complete the process

        [parameters]
        - view: either a structured view class (a Viewable subclass) or a plain view function (returning a widget).
        The view takes the page instance as argument.

        - pid: str, the Page ID. A PID will be automatically generated if you don't set one.
         Note that the first added page is de facto the home page and if you don't assign a PID,
          the PID "home" will be assigned to it.

        - title: the title of the page. By default, it is the pid of the page

        - category: string, the menu category name under which the page is indexed

        - indexable: boolean, to tell if you want the page to be indexed on the menu bar or not.

        - on_open: function to call when the page is opened.
        It should accept an argument: the context (namedtuple)

        - on_close: function to call when the page is closed.
        It should accept an argument: the context (namedtuple)

        [exceptions]
        - gaspium.error.DuplicatePageError: raised if the page name already exists

        [return]
        Returns the pid (Page ID)
        """
        if pid and pid in self._pages:
            raise error.DuplicatePageError
        if not pid:
            if not self._pages:
                pid = "home"
            else:
                pid = self._new_pid()
        if not self._pages:
            self._home_pid = pid
        view_type = misc.get_view_type(view)
        title = title if title else pid
        self._pages[pid] = {"view": view, "title": title, "view_type": view_type,
                            "category": category, "indexable": indexable,
                            "on_open": on_open, "on_close": on_close,
                            "body": None}
        if indexable and self._navbar:
            self._navbar.add(pid, title, category)
        return pid

    def open(self, pid, data=None):
        """
        Open a page specified by its PID (Page ID).

        [parameters]
        - pid: PID

        - data: Associated data. This data is passed to the 'on_open' callback of the page.
         Note: If you open this page from the command line, the data passed to the page
          is split into a tuple.

        [exceptions]
        - gaspium.error.PageNotFoundError: raised if not page is associated to this PID.
        - gaspium.error.PageStateError: raised if you try to open a new page inside 'on_close' callback.

        [return]
        None
        """
        if not self._started:
            cache = (pid, data)
            self._delayed_open_request.append(cache)
            return
        if self._closing_page:
            msg = "Don't open a new page inside 'on_close' callback"
            raise error.PageStateError(msg)
        if pid not in self._pages:
            raise error.PageNotFoundError
        self._opening_pages_count += 1
        cache_opening_pages_count = self._opening_pages_count
        on_open = self._pages[pid]["on_open"]
        if self._pid and not self._opening_page:
            on_close = self._pages[self._pid]["on_close"]
            body = self._pages[self._pid]["body"]
            if on_close:
                context = misc.create_context_2(self, self.root, self._pid, body)
                self._closing_page = True
                on_close(context)
                self._closing_page = False
            self._close_page(self._pid)
        if on_open:
            context = misc.create_context_1(self, self._root, pid, data)
            self._opening_page = True
            on_open(context)
            self._opening_page = False
        if cache_opening_pages_count == self._opening_pages_count:
            self._pid = pid
            self._open_page(pid, data)
            self._edit_app_title(pid)

    def start(self):
        """
        Start the app. Mainloop here.
        """
        if self._started:
            message = "This method shouldn't be called twice. Please use 'restart' instead"
            raise error.AppStateError(message)
        # add "help" page
        if self._pages and "help" not in self._pages:
            self.add(misc.default_help_page, pid="help", indexable=False)
        self._started = True
        self._set_title()
        self._apply_window_config()
        # check cli request
        pid, data = misc.check_cli_request()
        if pid:
            cache = (pid, data)
            self._delayed_open_request = [cache]
            if pid not in self.pages:
                print("This Page doesn't exist.")
                self.exit()
        else:
            data = None
            pid = self._home_pid
            if pid and not self._delayed_open_request:
                cache = (pid, data)
                self._delayed_open_request.append(cache)

        for pid, data in self._delayed_open_request:
            self.open(pid, data=data)
        self._delayed_open_request = []
        # main loop
        try:
            self._root.mainloop()
        except KeyboardInterrupt:
            self.exit()

    def stop(self):
        """
        Stop the app, i.e. destroy the window
        """
        if self._stopped:
            return
        if self._on_stop:
            try:
                self._on_stop(self)
            except error.AppStateError as e:
                return
        if self._root.winfo_exists():
            self._root.destroy()
        self._stopped = True

    def clear_cache(self, *pid):
        """
        Clear the cache.

        [parameters]
        - *pid: the PID(s) which cache should be erased.
        If you don't set any PID, the entire cache will be purged

        [return]
        Returns True or False
        """
        if pid:
            page_info = self._pages.get(pid)
            if not page_info:
                return False
            page_info["body"] = None
            return True
        for pid, page_info in self._pages:
            page_info["body"] = None
        return True

    def exit(self):
        """
        Exit the app after calling the stop method
        """
        self.stop()
        if self._on_exit:
            try:
                self._on_exit(self)
            except error.AppStateError as e:
                return
        sys.exit()

    def _setup(self):
        self._root.config(background="white")
        self._cached_report_callback_exception = self._root.report_callback_exception
        self._root.report_callback_exception = self._on_report_callback_exception
        self._root.protocol("WM_DELETE_WINDOW", self.exit)
        misc.EnhanceTk(self._root)

    def _init_root(self):
        self._root = tk.Tk()
        if self._theme:
            self._theme.apply(self._root)

    def _new_pid(self):
        """
        Generate a new valid PID (Page ID).
        A PID value follows this pattern: 'pid-x', with x being an integer

        [return value]
        A new valid PID
        """
        while True:
            self._i += 1
            pid = "pid-{}".format(self._i)
            if pid not in self._pages:
                return pid

    def _set_title(self):
        if not self._title:
            self._title = "Application"
        text = "{} | built with Gaspium".format(self._title)
        self._root.title(text)

    def _apply_theme(self):
        if not self._theme:
            return
        self._root.option_clear()
        self._theme.apply(self._root)

    def _apply_window_config(self):
        # geometry
        if self._geometry == "max":
            self._maximize_window()
        else:
            self._root.geometry(self._geometry)
            if "-" not in self._geometry and "+" not in self._geometry:
                self._center_window()
        # resizable width and height
        resizable_width, resizable_height = self._resizable
        self._root.resizable(width=resizable_width, height=resizable_height)

    def _on_report_callback_exception(self, exc, val, tb):
        self._cached_report_callback_exception(exc, val, tb)
        if not self._crash_resistant:
            self.exit()

    def _maximize_window(self):
        """
        Maximize the window
        """
        system = platform.system()
        if system == "Linux":
            self._root.attributes("-zoomed", True)
        else:  # for "Darwin" (OSX) and "Window"
            self._root.state("zoomed")

    def _center_window(self):
        """
        Center the window
        """
        tkutil.center_window(self._root)

    def _close_page(self, pid):
        page_info = self._pages[pid]
        body = page_info["body"]
        if self._caching:
            if body:
                body.pack_forget()
        else:
            if body:
                body.pack_forget()
                body.destroy()
            self._pages[pid]["body"] = None

    def _open_page(self, pid, data):
        page_info = self._pages[pid]
        view = page_info["view"]
        body = page_info["body"]
        view_type = page_info["view_type"]
        if not self._caching or (self._caching and not body):
            context = misc.create_context_1(self, self._root, pid, data)
            cache = view(context)
            if view_type == "class":
                body = cache.build()
            else:
                body = cache
        if body:
            body.pack(fill=tk.BOTH, expand=1, padx=0, pady=0)
            self._update_root_background(body)
        self._pages[pid]["body"] = body

    def _update_root_background(self, body):
        background = body.cget("background")
        self._root.config(background=background)

    def _edit_app_title(self, pid):
        page_info = self._pages[pid]
        page_title = page_info["title"] if page_info["title"] else pid
        cache = "{}  -  {}"
        cache = cache.format(self._title, page_title)
        self._root.title(cache)

    def _restart(self):  # TODO: make it public
        self._pid = None
        #_menubar.delete(0, "end")
        #self._root.config(menu="")
        for pid, page_info in self._pages.items():
            body = page_info["body"]
            if body:
                body.destroy()
                page_info["body"] = None
        if self._home_pid:
            self.open(self._home_pid)
