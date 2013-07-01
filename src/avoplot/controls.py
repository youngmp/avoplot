#Copyright (C) Nial Peters 2013
#
#This file is part of AvoPlot.
#
#AvoPlot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#AvoPlot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with AvoPlot.  If not, see <http://www.gnu.org/licenses/>.
import wx

class AvoPlotControlPanelBase(wx.ScrolledWindow):
    def __init__(self, parent, name):
        self.name = name
        self.__sizer = wx.BoxSizer(wx.VERTICAL)
        self.old_parent = parent
        super(AvoPlotControlPanelBase, self).__init__(parent, wx.ID_ANY)
        
        self.SetScrollRate(2, 2)
        self.SetSizer(self.__sizer)
        self.__sizer.Fit(self)
        self.SetAutoLayout(True)
    
    
    def Add(self,*args, **kwargs):
        self.__sizer.Add(*args, **kwargs)
        