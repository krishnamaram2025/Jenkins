def get_plugin_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for plugin in server.get_plugins().values():
        print ("Short Name:%s" % (plugin.shortName))
        print ("Long Name:%s" % (plugin.longName))
        print ("Version:%s" % (plugin.version))
        print ("URL:%s" % (plugin.url))
        print ("Active:%s" % (plugin.active))
        print ("Enabled:%s" % (plugin.enabled))
