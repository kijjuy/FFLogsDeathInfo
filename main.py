
import requests
import json

def getFightInfo(reportId):
    url = "https://www.fflogs.com:443/v1/report/fights/" + reportId + "?api_key=7dfd1f689da2f2091929c85a01ac4e47"
    response = requests.get(url) # get response from fflogs api
    return response.json()["fights"] # extract 

def getDeathInfo(reportId):
    url = "https://www.fflogs.com:443/v1/report/events/deaths/" + reportId +"?end=10519380&api_key=7dfd1f689da2f2091929c85a01ac4e47"
    response = requests.get(url)
    return response.json()["events"]

def addDeathsToPlayerList(deathsList):
    playerArr = []
    noKillAbilCount = 0
    for death in deathsList:
        try:
            if(playerArr["targetID"]):
                if(playerArr["targetID"]["killingAbility"]):
                    playerArr["targetID"]["killingAbility"] += 1 # add 1 deaths to killingAbility type
                else:
                    playerArr["targetID"].append(death["killingAbility"]) # user did not have killingAbility registered, add ability and set number of deaths to one
            

def main():
    reportId = "pn86HaP4BcjAYRZ1" #input("Paste report Id: ") # Get id of report. report ID is the key at the end of a url while viewing a report.

    fightInfo = getFightInfo(reportId)
    fightAmount = len(fightInfo)
    endTime = fightInfo[len(fightInfo)-1]["end_time"]


    deathsArr = getDeathInfo(reportId)
    print(len(deathsArr))
    count = 0
    index = 0
    noKillAbilCount = 0
    print(deathsArr[0]["killingAbility"]["name"])
    while(index < len(deathsArr)):
        index += 1
        try:
            if deathsArr[index]["killingAbility"]["name"] == "Bleeding":
                count = count + 1
        except:
            noKillAbilCount += 1

    print(count)


if(__name__ == "__main__"):
    main()

class Player:

    def __init__(self, id):
        self.id = id
        self.deaths = []

    def checkIfHasDeath(self, killingAbility):
        if self.deaths[killingAbility]:
            return True
        return False

    def addDeath(self, killingAbility):
        if self.checkIfHasDeath:
            self.deaths[killingAbility, 1]