import wavedrom
svg = wavedrom.render("""
{
"signal" : 
 [
  { "name": "Row address @ DRE output", "wave": "=.......=...................=...........", "period": 1, "node": "........a" },
  { "name": "FAS position @ FPA", "wave": "3.........4...................5.........", "data": ["TES 34", "TES 1", "TES 2"], "period": 1, "node": "..........b" },
  {}, 
  { "name": "DEMUX ADC clk", "wave": "p.......................................", "period": 1 },
  { "name": "SYNC @ DEMUX input", "wave": "0.........1.0...........................", "node": "..........c.d", "period": 1 },
  { "name": "Feedback in DEMUX", "wave": "4...........5...................2.......", "data": ["FB 1", "FB 2", "FB 3"], "node": "............e", "period": 1 },
  { "name": "Feedback delayed in DEMUX", "wave": "3.......4...................5...........", "data": ["FB 34", "FB 1", "FB 2"], "node": "............................f", "period": 1 },
  { "name": "Feedback @ FPA", "wave": "3.........4...................5.........", "data": ["FB 34", "FB 1", "FB 2"], "node": "..............................g", "period": 1 }
 ],
"edge":
 [
 "a~>b", "a~>c", "d-e", "e~>f", "f~>g"
 ],
"config" : { "hscale" : 0.5, "skin": "narrow" }
} 
""")
svg.saveas("synchro-RA-FB.svg")