def announce(line, terminus, station, transfers, door, curved):
  next = ["この電車は{0}、{1}行きです".format(line, terminus)]
  this = []

  # terminus?
  if station == terminus:
    next.append("次は、{0}、終点です".format(station))
    this.append("{0}終点に到着です".format(station))
  else:
    next.append("次は、{0}".format(station))
    this.append("{0}に到着です".format(station))

  # interchange?
  if transfers:
    next.append("{0}はお乗り換えです".format(transfers))
    this.append("{0}はお乗り換えです".format(transfers))

  # door
  this.append("{0}のドアが開きます".format(door))

  # mind the gap, if the platform is curved
  if curved:
    this.append("降りるかたは足元にご注意ください")

  # thank you at the end of the line
  if station == terminus:
    this.append("えんまる鉄道ご利用くださいまして、ありがとうございました")

  # return
  return ["、、".join(next), "、、".join(this)]



line = "中央線"
terminus = "南角"
stationlist = [
["虹", "", "右側", False],\
["三ノ輪", "りぱん線", "左側", False],\
["桜見町", "地方鉄道", "右側", False],\
["八千代", "南北線、上り木綿急行線", "右側", False],\
["水族館", "天王寺線、下り木綿急行線", "右側", False],\
["えんまるはねみやいちば", "地方鉄道", "左側", True],\
["にしはねみや", "木綿急行線", "左側", False],\
["烏丸センター", "地方鉄道", "左側", False],\
["烏丸緑地", "", "左側", False],\
["にしじま", "", "左側", False],\
["えんまる中央", "東海道線、東山方面の円丸線、地方鉄道", "右側", False],\
["日本橋", "福野空港方面の電車", "左側", False],\
["福野", "", "右側", False],\
["ポートランドトンネル", "", "右側", False],\
["紫陽花ちょう", "とりこ方面の円丸線", "左側", True],\
["草津", "", "右側", False],\
["えんしま大橋", "", "左側", False],\
["南角", "", "左側", False],\
]

for s in stationlist:
  a = announce(line, terminus, s[0], s[1], s[2], s[3])
  print(a[0])
  print(a[1])
