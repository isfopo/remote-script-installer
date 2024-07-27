from .RemoteScriptInstaller import RemoteScriptInstaller


def create_instance(c_instance):
    ''' Creates and returns Remote Script instance '''
    return RemoteScriptInstaller(c_instance)
