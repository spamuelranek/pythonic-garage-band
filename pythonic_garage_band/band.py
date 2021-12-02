# def make_json_band():
  
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

  def __str__(self):
    intros = f"Hello, we are {self.name}"
    for member in self.members:
      intros = intros + "\n" + str(member)
    return intros

  def __repr__(self):
    intros = f"{self.name} Members: {len(self.members)}"
    for member in self.members:
      intros = intros + "\n" + repr(member)
    return intros

  @classmethod
  def to_list(cls):
    return cls.instances

if __name__ == "__main__":
  def one_band():
    members = [
        Guitarist("Kurt Cobain"),
        Bassist("Krist Novoselic"),
        Drummer("Dave Grohl"),
    ]

    some_band = Band("Nirvana", members)

    return some_band
  
  new_band = one_band()
  print(str(new_band))

