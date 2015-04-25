import sys
import xbmcgui
import xbmcplugin
# We include the things we need.


addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')
# Put this in the audio category.


url = 'http://50.7.99.155:7382/' # Rather straightforward, here.
li = xbmcgui.ListItem('Tune Into Orbital.FM', iconImage='http://i.imgur.com/4y7S20F.png')  #Name, then the icon. I'm pleasantly surprised it accepts URLs!
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
#Bleh. It's a hacky hack to use Imgur, but it'll work for now.




xbmcplugin.endOfDirectory(addon_handle) # Here we tell the system that this is the end for now.