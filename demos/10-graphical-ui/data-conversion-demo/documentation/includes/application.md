## Configuring your project for the application

You will need to associate the code to a project if not
already done. If you don't have a project, just opening the folder
with PyCharm should suffice.

However, you need to have a `virtualenv` for your project (for good
practice), that uses Python 3.6+.

In this virtualenv, you'll have to install :

- `pyside6`

Note that Qt has issues with theming; if PySide6 is installed, using `pip` or
another medium, it won't follow the system theme. However, if PySide2 is
installed globally on the system (via `apt-get` or `pacman`), programs seem to
follow the system theme. One would then have to revert to importing from
`PySide2` instead of `PySide6` (with no other changes).

## How to run the application

The application is very simple to run in PyCharm.
To do it, right-click on the source file content pane, somewhere where
there is an empty space.

Then, click the `Run <application>...`.
