import wavedrom
svg = wavedrom.render("""
{
"signal" : 
 [
  { "name": "CLK_REF  (60 MHz)", "wave": "P.............", "period": 2 },
  { "name": "SYNC", "wave": "l...h.l.....................", "node": ".....a" ,"period": 1 },
  {},
  { "name": "CLK_ADC (120 MHz)", "wave": "P...........................", "node": ".....b", "period": 1 },
  { "name": "PIX (6.66 MHz)", "wave": "=.....=..................=..", "data": ["34", "1", "2"], "node": "......c", "period": 1, "phase": 0 }
 ],
"edge":
 [
 "a~>c", "b~>c"
 ],
 "foot":
 {
 "tick": 0
 },
"config" : { "hscale" : 0.5, "skin": "narrow" }
} 
""")
svg.saveas("synchro-dmx-fw.svg")