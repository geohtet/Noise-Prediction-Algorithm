# -*- coding: utf-8 -*-

"""
/***************************************************************************
 NoisePrediction
                                 A QGIS plugin
 This plugin estimates the noisel level by distances and barriers as BS:5228 standard.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-02-19
        copyright            : (C) 2022 by Htet Arkar Soe
        email                : htetarkar.env.2016@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Htet Arkar Soe'
__date__ = '2022-02-19'
__copyright__ = '(C) 2022 by Htet Arkar Soe'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon,QDesktopServices

from qgis.core import QgsProcessingAlgorithm, QgsApplication
import processing
from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .Noise_Prediction_provider import NoisePredictionProvider
from .urls import DOC_PLUGIN_URL
cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class NoisePredictionPlugin(object):

    def __init__(self, iface):
        self.provider = None
        self.iface = iface
        
    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = NoisePredictionProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()
        icon = os.path.join(os.path.join(cmd_folder, 'logo.png'))
        self.action = QAction(
          QIcon(icon),
          u"Noise Prediction From Point Source", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu(u"&NoisePrediction", self.action)
        self.iface.addToolBarIcon(self.action)
        
        icons = os.path.join(os.path.join(cmd_folder, 'help.png'))
        self.actionAide= QAction(QIcon(icons),u"Help",self.iface.mainWindow())
        self.actionAide.triggered.connect(self.showHelp)
        self.iface.addPluginToMenu(u"&NoisePrediction", self.actionAide)
        self.iface.addToolBarIcon(self.actionAide)
        
    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
        self.iface.removePluginMenu(u"&NoisePrediction", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        self.iface.removePluginMenu(u"&NoisePrediction", self.actionAide)
        self.iface.removeToolBarIcon(self.actionAide)
        
    def showHelp(self):  ### Help window
        #QMessageBox.information(self.iface.mainWindow(),"Important Note", 
        #"All of model input CRS and project CRS must be Project Coordinate System (PCS), except Dem File. Please Get Sample Data and run the test for first look")
        QDesktopServices.openUrl(QUrl(DOC_PLUGIN_URL))
        
    def run(self):
        processing.execAlgorithmDialog("Estimate Noise Level By Distance:Calculate-BS:5228")