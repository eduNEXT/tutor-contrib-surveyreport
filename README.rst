Survey Report plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

**Installing this plugin is a clear sign of the intention to send the report**,
this report will be sent every first day of january and june unless you set another value by settings.

More information about Survey Report:
https://openedx.atlassian.net/wiki/spaces/OEPM/pages/3872948238/Problem+Very+few+are+going+to+generate+and+send+the+Survey+Report.

Installation
------------


.. code-block:: bash

   pip install git+https://github.com/eduNEXT/tutor-contrib-surveyreport

Usage
-----

.. code-block:: bash

   tutor plugins enable surveyreport


Tutor settings
-----------------------

These variables will be settled by default if you want to make override you can set it in `config.yml` file.

.. code-block:: yaml

   SURVEYREPORT_ENABLE: True
   SURVEYREPORT_SCHEDULE: "0 0 1 1,6 *"
   SURVEYREPORT_AUTO_SEND: True
   SURVEYREPORT_ANONYMOUS: False

**Note:**

* By default the surveyreport will be sent, if you dont want to send it automatically you should set the value of **SURVEYREPORT_AUTO_SEND** to False.
* If you want to send the report anonymously, you must set the value of **SURVEYREPORT_ANONYMOUS** to True.

License
-------

This software is licensed under the terms of the AGPLv3.
