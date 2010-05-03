# desktopcover - displays Exaile album covers on the desktop
# Copyright (C) 2006-2010  Johannes Sasongko <sasongko@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from xlgui.preferences import widgets
from xl.nls import gettext as _

name = _('Desktop Cover')
_basedir = os.path.dirname(os.path.realpath(__file__))
ui = os.path.join(_basedir, "prefs.ui")

_SETTINGS_PREFIX = 'plugin/desktopcover/'

class AnchorPreference(widgets.ComboPreference):
    default = 0
    name = _SETTINGS_PREFIX + 'anchor'
    def __init__(self, prefs, widget):
        widgets.ComboPreference.__init__(self, prefs, widget, use_index=True)

class XPreference(widgets.SpinPreference):
    default = 0
    name = _SETTINGS_PREFIX + 'x'

class YPreference(widgets.SpinPreference):
    default = 0
    name = _SETTINGS_PREFIX + 'y'

class SizePreference(widgets.SpinPreference):
    default = 200
    name = _SETTINGS_PREFIX + 'size'

# vi: et sts=4 sw=4 tw=80
