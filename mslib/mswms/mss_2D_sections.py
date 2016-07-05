"""2D cross-section style super classes for use with the
   MSSPlotDriver subclasses.

********************************************************************************

   Copyright 2008-2014 Deutsches Zentrum fuer Luft- und Raumfahrt e.V.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

********************************************************************************

This file is part of the DLR/IPA Mission Support System Web Map Service
(MSS-WMS).

AUTHORS:
========

* Marc Rautenhaus (mr)

"""

# standard library imports
import logging
from abc import ABCMeta, abstractmethod

"""
Horizontal Section Styles
"""


class Abstract2DSectionStyle(object):
    """Abstract 2D section super class. Use this class as a parent
       for classes implementing horizontal and vertical cross sections.
    """
    __metaclass__ = ABCMeta

    # Name and title of each derived style have to be defined if the style
    # should be used with the WMS WSGI module.
    name = None
    title = None
    abstract = None
    queryable = False
    styles = None

    # Define the datafields required by a style with this property.
    required_datafields = []

    def __init__(self, driver=None):
        self.driver = driver

    def required_datatypes(self):
        """Returns a list containing the datatypes required by the
           data fields requested by the style.
        """
        return [datafield[0] for datafield in self.required_datafields]

    def _prepare_datafields(self):
        """Optional re-implementation: Use this function to process some
           input data before the plotting starts (e.g. to derive potential
           temperature from pressure and temperature).
        """
        pass

    def supported_epsg_codes(self):
        """Returns a list of supported EPSG codes, if available.
        """
        return []

    @abstractmethod
    def supported_crs(self):
        """Returns a list of the coordinate reference systems supported by
           this style.
        """
        pass

    def set_driver(self, driver):
        """Set the driver object for this layer.
        """
        self.driver = driver

    def get_init_times(self):
        """Returns a list of available forecast init times (base times).
        """
        if self.driver is not None:
            return self.driver.get_init_times()
        else:
            return []

    def get_all_valid_times(self):
        """Returns a list containing the combined forecast valid times of
           all available init times.
        """
        valid_times = set()
        if self.driver is not None:
            for vartype, varname in self.required_datafields:
                vtimes = self.driver.get_all_valid_times(varname, vartype)
                if len(valid_times) == 0:
                    valid_times.update(vtimes)
                else:
                    valid_times.intersection_update(vtimes)
        valid_times = list(valid_times)
        valid_times.sort()
        return valid_times

    def uses_time_dimensions(self):
        """Returns whether this layer uses the WMS time dimensions. If False,
           valid_time and init_time do not have to be specified to
           plot_hsection().

        Currently implemented by testing whether the style requires data fields
        from the ECMWF forecast.
        """
        return len(self.required_datafields) > 0

    def get_elevations(self):
        """Returns a list of available elevations for this layer.

        Assumes that the same elevation levels are available for all time
        steps.
        """
        logging.debug("checking vertical dimensions for layer %s.." % self.name)
        successful = False
        if self.driver is not None:
            # Get the latest init time.
            init_times = self.driver.get_init_times()
            if len(init_times) == 0:
                logging.error("ERROR: cannot determine initialisation time(s) "
                              "of this dataset. Check that file structure is "
                              "in accordance with the used access class in mss_wms_settings.py!")
                return []
            time = init_times[-1]

            # Open the data files for the analysis (valid time = init time).
            # It can happen that not all required files are available for
            # all init times. The try..except block takes care of this
            # problem and tries to find a time at which all required
            # files are available.
            for i in range(len(init_times)):
                try:
                    time = init_times[i]
                    self.driver.set_plot_parameters(self,
                                                    init_time=time,
                                                    valid_time=time)
                except (IOError, ValueError) as e:
                    logging.debug("WARNING: unsuccessfully examined data for "
                                  "init time %s.. trying next time." % time)
                    logging.debug("(Error message: %s)" % e)
                else:
                    successful = True
                    break

            # If the analysis time is not available try to extract the available
            # valid times for the datafield required by this style.
            if not successful:
                vartype, varname = "", ""
                if len(self.required_datafields) > 0:
                    vartype, varname = self.required_datafields[0]
                for it in init_times:
                    valid_times = self.driver.get_valid_times(varname, vartype, it)
                    for vt in valid_times:
                        try:
                            time = init_times[i]
                            self.driver.set_plot_parameters(self,
                                                            init_time=it,
                                                            valid_time=vt)
                        except (IOError, ValueError) as e:
                            logging.debug("WARNING: unsuccessfully examined data for "
                                          "init time %s, valid time %s.. trying next "
                                          "time." % (it, vt))
                            logging.debug("(Error message: %s)" % e)
                        else:
                            successful = True
                            break

            # If we're still not successful..
            if not successful:
                logging.error("ERROR: cannot determine whether there's a "
                              "vertical coordinate.. something is wrong with "
                              "this dataset!!")
                return []

            # Get a list of the available levels.
            if self.driver.vert_data is not None:
                return ["%i" % lvl for lvl in sorted({int(_x) for _x in self.driver.vert_data})]
            else:
                return []
        else:
            return []

    def get_elevation_units(self):
        """Returns the units of the elevation values.
        """
        if self.driver is not None:
            return self.driver.vert_units
        else:
            return ""
