# created by hualai.deng , 2013-04-01
########################################################################
# configure the url route
urls = (
    ('/hello', 'interface.hello.hello'),
    ('/mymem', 'interface.mymem.Main'),
)


#########################################################################
# methods
#########################################################################
# return urls map
def getUrlsMap ():
    global urls
    urlsMap = []
    for urlInfo in urls:
        urlsMap.append( urlInfo[0] )
        urlsMap.append( urlInfo[1] )

    return urlsMap
        
    
########################################################################
# test
if __name__ == "__main__" :
    print str(urls)
