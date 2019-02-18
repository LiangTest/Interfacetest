import json
class WXTextMessage:
    def __init__(self):
        self.touser=''
        self.toparty=''
        self.totag=''
        self.msgtype=''
        self.agentid=''
        self.Text=''
        self.safe=''

    def getTouser(self):
        return self.touser


    def setTouser(self,touser):
        self.touser = touser


    def getTotag(self):
        return self.totag

    def setTotag(self,totag):
        self.totag = totag


    def getSafe(self):
        return self.safe

    def setSafe(self,safe):
        self.safe = safe

    def getToparty(self):
        return self.toparty

    def setToparty(self,toparty):
        self.toparty = toparty

    def getMsgtype(self):
        return self.msgtype

    def setMsgtype(self, msgtype):
        self.msgtype = msgtype

    def getAgentid(self):
        return self.agentid;


    def setAgentid(self, agentid):
        self.agentid = agentid

    def getText(self):
        return self.Text

    def setText(self, text):
        self.Text = text

    def toJson(self):
        data = {'touser':self.touser,'toparty':self.toparty,'totag':self.totag,'msgtype':self.msgtype,'agentid':self.agentid,'Text':self.Text,'safe':self.safe}
        jdata = json.dumps(data).encode('UTF-8')
        return jdata
