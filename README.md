openoffice-py-mockup
==

I'm running an OpenERP project. I have OpenOffice installed on my dev and production dockers. But I cannot manage to make it run on my mac.

However, I seldom need to debug report problems with IDE on mac. A mockup will be enough.

[And, they are not using `report_aeroo_ooo` in v8.](https://github.com/ingadhoc/odoo-addons/issues/1#issuecomment-72063539)


Where is the code from?
==

> The OpenOffice python module unfortunately does not have a Python package to install it into the virtual environment, so for now you need to copy it manually. You have to find the two files uno.py and unohelper.py in your OpenOffice installation.
> http://invenio-software.org/wiki/Installation/InvenioInVirtualenv#a2.6InstallPythondependencies

    // enter the docker container
    $ cp /usr/lib/python2.7/dist-packages/uno.py ...here
    $ cp /usr/lib/python2.7/dist-packages/unohelper.py ...here

    // pyuno is `/usr/lib/libreoffice/program/pyuno.so`
    $ vim pyuno.py
    // implement only the minimal methods


How to use it?
==

    // http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#add2virtualenv
    $ workon openerp
    (openerp)$ cd /path/to/github/openoffice-py-mockup
    (openerp)$ add2virtualenv .


Reference
==

1. [pyuno](https://wiki.openoffice.org/wiki/Python)
2. [pyuno-bridge](http://www.openoffice.org/udk/python/python-bridge.html)


MIT License
==
