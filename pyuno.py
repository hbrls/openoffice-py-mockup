# -*- coding: utf-8 -*-
import logging


_logger = logging.getLogger(__name__)


class Placeholder():
    pass


class ServiceManager():

    def createInstanceWithContext(self, resolver_name, local_context):
        return Placeholder()

class ComponentContext():

    def __init__(self):
        self.ServiceManager = ServiceManager()


def getComponentContext():
    return ComponentContext()


def getConstantByName():
    pass


def getTypeByName():
    pass


def getClass(typeName):
    _logger.info(typeName)
    return Placeholder


def isInterface():
    pass


def generateUuid()        :
    pass


def systemPathToFileUrl():
    pass


def fileUrlToSystemPath():
    pass


def absolutize():
    pass


def getCurrentContext():
    pass


def setCurrentContext():
    pass


def checkEnum():
    pass


def checkType():
    pass


def invoke():
    pass
