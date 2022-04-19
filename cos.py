# Just for the funnies, but can check version and status.
class cos:
  def __init__(self, version, stat):
    self.version = version
    self.stat = stat
  def version():
    print("Version 3.5 Dev")
  def stat():
    works = True # Changes
    if works != True:
      print("Down --> Dev ENV")
    else:
      print("Up && Running --> Dev ENV")

cos.version() #if want to check version
cos.stat() #if want to check status of operation