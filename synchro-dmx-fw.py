import wavedrom
svg = wavedrom.render("""
{
"signal" : 
 [
  { "name": "CLK_REF  (20 MHz)", "wave": "h..l....h....l....h....l....h....l....h....l....", "period": 1 },
  { "name": "SYNC", "wave": "l.......h.........l.............................", "node": "..........a" ,"period": 1 },
  {},
  { "name": "CLK_ADC (100 MHz)", "wave": "P.......................", "node": ".....b", "period": 2 },
  { "name": "PIX", "wave": "=.....=.......=.......=.", "data": ["34", "1", "2", "3"], "node": "......c", "period": 2, "phase": 0 }
 ],
"edge":
 [
 "a~>c", "b~>c"
 ],
"config" : { "hscale" : 0.5, "skin": "narrow" }
} 
""")
svg.saveas("synchro-dmx-fw.svg")