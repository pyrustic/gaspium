"""The App class is defined inside this module."""
import os
import os.path
import sys
import platform
import tkinter as tk
import tkutil
from gaspium import error
from gaspium import util
from gaspium import dto
from gaspium.navbar import Navbar
from viewstack import ViewStack


USER_CACHE_DIR = os.path.join(os.path.expanduser("~"),
                              "PyrusticHome", "gaspium")


class App:
    """This class is the entry point of your Gaspium app"""
    def __init__(self, name="app", title="Application", manager=None,
                 geometry="800x500", remember_geometry_change=True,
                 resizable=(True, True), caching=True, on_stop=None,
                 on_exit=None, failfast=True, show_page_title=True,
                 navbar=Navbar, page_from_cli=True):
        """
        Initialization.

        [parameters]
        - name: string, unique name of this app

        - title: string, the title of the app

        - manager: the instance of a manager

        - geometry: str, to specify the geometry. Put "max" to maximize the window. Example: "800x400", "800x400+0+0", "+0+0", "max"

        - remember_geometry_change: boolean, to specify if the window's geometry should be remembered.

        - resizable: 2-tuple of booleans to tell if you want the width and the height of the app to
         be resizable.

        - theme: the theme, i.e. an instance of tkstyle.Theme

        - caching: boolean to tell if whether you want pages to be cached or re-built at open.

        - on_stop: the on_stop handler, i.e. a function that will be called when the app is going to close.
        This function should accept an argument: the app instance

        - on_exit: the on_exit handler, i.e. a function that will be called when the app is going to exit.
        This function should accept an argument: the app instance

        - failfast: boolean, set it to True if you don't want the GUI to close when a random exception is raised

        - show_page_title: boolean, set True to allow the app to update the window title to show the current page title.

        - navbar: navigation bar class. The constructor must accept the app instance.
        The class must have an "add" method that accepts these arguments: pid, title, and category

        - page_from_cli: boolean, specify if pages can be opened directly from cli or not.

        """
        self._name = name
        self._title = title
        self._manager = manager
        self._geometry = geometry
        self._remember_geometry_change = remember_geometry_change
        self._resizable = resizable
        self._caching = caching
        self._on_stop = on_stop
        self._on_exit = on_exit
        self._failfast = failfast
        self._show_page_title = show_page_title
        self._navbar = navbar
        self._page_from_cli = page_from_cli
        
        self._root = None
        self._pages = {}
        self._pid = None
        self._pid_from_cli = None
        self._started = False
        self._stopped = False
        self._pre_started = False
        self._clargs = None
        self._i = 0
        self._data = dict()
        self._cached_report_callback_exception = None
        self._home_pid = None
        self._opening_pages_count = 0
        self._closing_page = False
        self._opening_page = False
        self._history = list()
        self._previously_mapped = False
        self._on_destroy_root_i = 0
        self._viewstack = None
        self._setup()

    @property
    def name(self):
        """
        Return the name of the app
        """
        return self._name

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
    def manager(self):
        return self._manager

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
    def failfast(self):
        """Get the failfast boolean"""
        return self._failfast

    @failfast.setter
    def failfast(self, val):
        """Set the failfast boolean"""
        self._failfast = val

    @property
    def pid(self):
        """
        Return the currently opened Page ID
        """
        return self._pid

    @property
    def page(self):
        """
        Return the currently opened page DTO representation
        """
        if not self._pid:
            return None
        page_info = self._pages.get(self._pid)
        if not page_info:
            return None
        return self._create_page_info_dto(page_info)

    @property
    def view(self):
        """Returns the current view"""
        if not self._pid:
            return None
        page_info = self._pages.get(self._pid)
        if not page_info:
            return None
        return page_info["view"]

    @property
    def pages(self):
        """
        Return a dictionary of DTOs that contain pages information.
        Note: Keys are PIDs (Page ID)
        """
        cache = dict()
        for pid, page_info in self._pages.items():
            cache[pid] = self._create_page_info_dto(page_info)
        return cache

    @property
    def root(self):
        """
        Return the root, i.e. the Tkinter's Tk instance that serves as the root of this app.
        """
        return self._root

    @property
    def viewstack(self):
        return self._viewstack

    @property
    def data(self):
        """
        This is an empty dictionary linked to this app.
        Use it to store whatever you want.
        Example: you can use it to retain the information about whether
         the user is authenticated or not.
        """
        return self._data

    @property
    def clargs(self):
        """Command line arguments"""
        return self._clargs

    @property
    def history(self):
        return self._history.copy()

    def attach(self, view_class, pid=None, title=None, category=None,
               indexable=True, kwargs=None):
        """
        Attach a new page to the app. This method will generate a new page instance then
        will call the layout function to complete the process

        [parameters]
        - view_class: a view class (i.e. a class that subclassed gaspium.Page).
        The Context instance is passed to the constructor of the view.

        - pid: str, the Page ID. A PID will be automatically generated if you don't set one.
         Note that the first added page is de facto the home page and if you don't assign a PID,
          the PID "home" will be assigned to it.

        - title: the title of the page. By default, it is the pid of the page

        - category: string, the menu category name under which the page is indexed

        - indexable: boolean, to tell if you want the page to be indexed on the menu bar or not.

        - kwargs: dict representing the keyword-arguments to pass to the view_class constructor.

        [exceptions]
        - gaspium.error.DuplicatePageError: raised if the page id already exists

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
        title = title if title else pid
        kwargs = kwargs if kwargs else dict()
        self._pages[pid] = {"pid": pid, "view_class": view_class, "view": None,
                            "title": title, "category": category,
                            "indexable": indexable, "kwargs": kwargs}
        if indexable and self._navbar:
            self._navbar.attach(pid, title, category)
        return pid

    def detach(self, pid):
        if pid in self._pages:
            del self._pages[pid]
            self._navbar.detach(pid)

    def open(self, pid):
        """
        Open a page specified by its PID (Page ID).

        [parameters]
        - pid: PID

        [exceptions]
        - gaspium.error.PageNotFoundError: raised if not page is associated to this PID.
        - gaspium.error.PageStateError: raised if you try to open a new page inside 'on_close' callback.

        [return]
        the view opened
        """
        if not self._pre_started:
            self._pre_start()
        if self._closing_page:
            msg = "Don't open a new page inside 'on_close' callback"
            raise error.PageStateError(msg)
        if pid not in self._pages:
            raise error.PageNotFoundError
        self._opening_pages_count += 1
        cache_opening_pages_count = self._opening_pages_count
        if self._pid:
            self._close_page(self._pid)
        if cache_opening_pages_count != self._opening_pages_count:
            return
        self._pid = pid
        view = self._open_page(pid)
        if self._show_page_title:
            self._edit_app_title(pid)
        self._history.append(pid)
        return view

    def start(self):
        """
        Start the app. Mainloop here.
        """
        if self._started:
            message = "This method shouldn't be called twice. Please use 'restart' instead"
            raise error.AppStateError(message)
        if not self._pre_started:
            self._pre_start()
        self._started = True
        if self._home_pid:
            self.open(self._home_pid)
        if self._pid_from_cli:
            if self._pid_from_cli in self._pages:
                self.open(self._pid_from_cli)
            else:
                print("Undefined page '{}'".format(self._pid_from_cli))
                self.exit()
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
            page_info["container"] = None
            return True
        for pid, page_info in self._pages:
            page_info["container"] = None
        return True

    def exit(self):
        """
        Exit the app after calling the stop method
        """
        if self._remember_geometry_change:
            try:
                tkutil.save_geometry(self._root, name=self._name)
            except Exception as e:
                print(e)
        self.stop()
        if self._on_exit:
            try:
                self._on_exit(self)
            except error.AppStateError as e:
                return
        sys.exit()

    def _setup(self):
        self._init_root()
        self._viewstack = ViewStack(self._root)
        self._navbar = self._navbar(self) if self._navbar else None
        self._root.config(background="white")
        self._cached_report_callback_exception = self._root.report_callback_exception
        self._root.report_callback_exception = self._on_report_callback_exception
        self._root.protocol("WM_DELETE_WINDOW", self._root.destroy)
        util.EnhanceTk(self._root)

    def _init_root(self):
        self._root = tk.Tk()
        tkutil.WinfoUpdater(self._root).activate()
        self._root.bind("<Destroy>", self._destroy_root, True)

    def _destroy_root(self, event):
        if event.widget is not self._root:
            return
        self.exit()

    def _new_pid(self):
        """
        Generate a new valid PID (Page ID).
        A PID value follows this pattern: 'pid-x', with x being an integer

        [return value]
        A new valid PID
        """
        while True:
            self._i += 1
            pid = "page{}".format(self._i)
            if pid not in self._pages:
                return pid

    def _set_title(self):
        if not self._title:
            self._title = "Application"
        self._root.title(self._title)

    def _apply_window_config(self):
        # geometry
        #saved_geometry = self._get_saved_window_geometry()
        if self._remember_geometry_change:
            default = "" if self._geometry == "max" else self._geometry
            tkutil.restore_geometry(self._root, name=self._name,
                                    default=default)
        elif self._geometry == "max":
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
        if not self._failfast:
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
        tkutil.center(self._root)

    def _open_page(self, pid):
        page_info = self._pages[pid]
        view = self._viewstack.views.get(pid)
        if view:
            self._viewstack.lift(pid)
            return view
        view_class = page_info["view_class"]
        kwargs = page_info["kwargs"]
        context = dto.Context(self, self._root, pid, self._manager)
        view = view_class(context, **kwargs)
        self._viewstack.add(pid, view)
        self._pages[pid]["view"] = view
        return view

    def _close_page(self, pid):
        cache = self._viewstack.views.get(pid)
        if not cache:
            return
        if not self._caching:
            self._viewstack.destroy(pid)
            self._pages[pid]["view"] = None
            return
        self._pages[pid]["container"] = None

    def _edit_app_title(self, pid):
        page_info = self._pages[pid]
        page_title = page_info["title"] if page_info["title"] else pid
        cache = "{}  -  {}"
        cache = cache.format(self._title, page_title)
        self._root.title(cache)

    def _pre_start(self):
        # add "help" page
        if self._pages and "help" not in self._pages:
            self.attach(util.default_help_page, pid="help", indexable=False)
        self._set_title()
        self._apply_window_config()
        # check cli request
        if self._page_from_cli:
            pid, data = util.check_cli_request()
            self._pid_from_cli = pid
            self._clargs = data
        self._pre_started = True

    # not used at all
    def __restart(self):  # TODO: make it public, improve it
        self._pid = None
        #_menubar.delete(0, "end")
        #self._root.config(menu="")
        for pid, page_info in self._pages.items():
            view = page_info["view"]
            if view.body.winfo_exists():
                view.body.destroy()
                page_info["view"] = None
        if self._home_pid:
            self.open(self._home_pid)

    def _create_page_info_dto(self, page_info):
        page_dto = dto.Page(page_info["pid"], page_info["view_class"],
                            page_info["view"],
                            page_info["title"], page_info["category"],
                            page_info["indexable"], page_info["kwargs"])
        return page_dto

    """
    def _save_window_geometry(self):
        if not self._remember_geometry_change:
            return
        geometry = "{}x{}+{}+{}".format(self._root.winfo_width(),
                                        self._root.winfo_height(),
                                        self._root.winfo_x(),
                                        self._root.winfo_y())
        geometry_dir = os.path.join(USER_CACHE_DIR, "geometry")
        geometry_filename = os.path.join(geometry_dir, self._name)
        if not os.path.isdir(geometry_dir):
            os.makedirs(geometry_dir)
        if geometry.startswith("0") or geometry.startswith("1x1"):
            return
        with open(geometry_filename, "w") as file:
            file.write(geometry)

    def _get_saved_window_geometry(self):
        geometry_dir = os.path.join(USER_CACHE_DIR, "geometry")
        geometry_filename = os.path.join(geometry_dir, self._name)
        if not os.path.isfile(geometry_filename):
            return None
        with open(geometry_filename, "r") as file:
            data = file.read()
        return data.strip()
    """

# TODO: add to App constructor a cache_size (int) param to set max number of pages that can be cached
