class Musician:
  instrument =""
  title = ""

  def __init__(self,name):
    self.name = name
  
  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"

  def __repr__(self):
    return f"{self.title} instance. Name = {self.name}"

  def get_instrument(self):
    return f"{self.instrument}"

  pass

class Guitarist(Musician):
  instrument = "guitar"
  title = "Guitarist"
  
  def play_solo(self):
    return "face melting guitar solo"




class Bassist(Musician):
  instrument = "bass"
  title = "Bassist"
  
  def play_solo(self):
    return "bom bom buh bom"



class Drummer(Musician):
  instrument = "drums"
  title = "Drummer"

  def play_solo(self):
    return "rattle boom crash" 


class Band:

  instances = []

  def __init__(self,name,band_members):
    self.name = name
    self.members = band_members
    Band.instances.append(self)

  def play_solos(self):
    solo_list = []
    for member in self.members:
      solo_list.append(member.play_solo())
    return solo_list

  @classmethod
  def to_list(cls):
    return cls.instances
  pass