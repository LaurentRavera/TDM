import wavedrom
svg = wavedrom.render("""
{
"signal" : 
 [
  { "name": "Row address @ DRE output",   "wave": "=.....=......................=....", "period": 1, "node": "......a" },
  { "name": "Pixel sequence in DEMUX", "wave": "=.........=......................=", "period": 1, "node": "..........b" },
  { "name": "Error signal @ DEMUX input", "wave": "=.......=......................=..", "period": 1, "node": "........c" },
  { "name": "BOXCAR", "wave": "0...1...0..................1...0..", "node": "...........................d", "period": 1 },
 {}, 
  { "name": "CLK_ADC",              "wave": "p.................................", "period": 1 },
  { "name": "CLK_REF",                    "wave": "p................", "period": 2 }
 ],
"edge":
 [
 "a~>b", "a~>c", "b~>d"
 ],
"config" : { "hscale" : 0.5, "skin": "narrow" }
} 
""")
svg.saveas("synchro-RA-ADC.svg")